from __future__ import print_function
import os, sys
import time
from datetime import datetime
from collections import OrderedDict
import uuid
import pandas as pd
import pymysql
import pytz

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

TZ_SHANGHAI = pytz.timezone('Asia/Shanghai')
def datetime_from_ts(ts):
  dt = datetime.utcfromtimestamp(ts).replace(tzinfo=pytz.utc)
  return dt

def ts_to_tz_shanghai(ts):
  dt = datetime_from_ts(ts)
  dt2 = dt.astimezone(TZ_SHANGHAI)
  return dt2

TABLE_TASK = 'lq_task'

TABLE_ADMIN = 'lq_admin'
TABLE_ADMIN_COLUMNS = ['id', 'pid', 'agent_id', 'user_id', 'username', 'nickname', 'order_mode', 'order_name', 'password', 'salt', 'mobile', 'avatar', 'email', 'login_time', 'login_ip', 'create_time', 'update_time', 'token', 'status', 'site_id', 'delete_time', 'secret', 'white_ip', 'alipay_rate', 'bank_rate', 'wechat_rate', 'alicode_rate', 'wemobile_rate', 'lowerhairs_rate', 'money', 'lock_money', 'bank_name', 'bank_branch', 'bank_num', 'bank_user', 'login_google_open', 'google_secret', 'bind_user', 'login_white_ip', 'lowerhairs_fee']

TABLE_ORDER = 'lq_orders'
TABLE_ORDER_COLUMNS = ['id', 'admin_id', 'agent_admin_id', 'users_id', 'sn', 'out_sn', 'money', 'pay_name', 'rate', 'brokerage', 'agent_brokerage', 'real_money', 'ip', 'user_ip', 'notify_url', 'pay_type', 'url_key', 'status', 'is_callback', 'p_remark', 'sign', 'operator', 'pay_time', 'rob_time', 'create_time', 'update_time', 'tdgroup_biaoshi', 'remark']

TABLE_LOWER = 'lq_lowerhairs'
TABLE_LOWER_COLUMNS = ['id', 'admin_id', 'agent_admin_id', 'type', 'users_id', 'money', 'rate', 'brokerage', 'user_brokerage', 'real_money', 'gold', 'bank_name', 'bank_num', 'bank_user', 'status', 'p_remark', 'create_time', 'update_time', 'notify_url', 'pay_time', 'sn', 'is_callback', 'agent_money', 'is_lock']


TABLE_ACCOUNT = 'lq_account'
TABLE_ACCOUNT_COLUMNS = ['ac_id', 'ac_code', 'agent_admin_id', 'm_id', 'ac_money', 'ac_user_money', 'ac_flow', 'ac_type', 'children_level', 'children_id', 'children_nickname', 'isdel', 'p_id', 't_id', 't_type', 'ip', 'site_id', 'remark', 'add_time']

name_by_ac_type = {
  1  : u'充值',
  2  : u'提现',

  10  : u'上架H币，冻结',
  11  : u'上架H币，冻结保证金',
  12  : u'下架H币，返还',
  13  : u'下架H币，返还保证金',
  14  : u'买家取消，返还',
  15  : u'买家取消，返还保证金',
  16  : u'卖家取消，返还',
  17  : u'卖家取消，返还保证金',
  18  : u'交易完成，返还保证金',
  19  : u'代付完成，余额到账',
  20  : u'后台下架，返还',
  21  : u'后台下架，返还保证金',
  22  : u'后台确认订单，H币到账',
  23  : u'代付完成，扣除商户余额',

  30 : u'出售H币，冻结',
  31 : u'出售H币，冻结保证金',
  32 : u'卖家取消，返还',
  33 : u'卖家取消，返还保证金',
  34 : u'后台取消，返还',
  35 : u'后台取消，返还保证金',
  36 : u'交易完成，返还保证金',
  37 : u'自动取消，返还',
  38 : u'自动取消，返还保证金',
  39 : u'后台强制成功，扣除余额',

  40 : u'下级返佣(代收)',
  41 : u'获取返佣',


  50 : u'人工存入',
  60 : u'人工扣款',
  61 : u'人工冻结',
  71 : u'人工商户充值',
  72 : u'人工商户扣款',
  73 : u'人工商户冻结',

  81 : u'代付完成，增加业务员佣金',
  82 : u'代收订单完成，增加商户余额',
  83 : u'代付订单提交，扣除商户余额',
  84 : u'代付订单取消，返还商户余额',
  85 : u'提现，扣除商户余额',
  86 : u'提现审核失败，返还商户余额',
  87 : u'出售H币，关联扣款',
  88 : u'后台取消，返还，关联扣款',
  89 : u'后台强制成功，扣除余额，关联扣款',
  90 : u'下级返佣(代付)',
  91 : u'代付强制驳回，返还商户余额',
  92 : u'代付强制驳回，扣除用户余额',
  93 : u'代付强制驳回，扣除上级业务员佣金',
  94 : u'代付强制驳回，扣除上级用户佣金',
}





def get_db_opts():
  _opts = {
    'HOST': "10.0.1.101",
    'NAME': "pays",
    'USER': "pays",
    'PASSWORD': "GEC!il1!4nha",
  }
  opts = {
    "host": _opts['HOST'],
    "port": 3306,
    "user": _opts['USER'],
    "password": _opts['PASSWORD'],
    "db": _opts['NAME'],
    "charset": "utf8",
  }
  return opts

def scan_all(cursor, table, columns):
  cmd = "SELECT %s FROM %s LIMIT %%s,%%s" % (", ".join(columns), table)

  offset = 0
  limit = 1024

  out = []

  for i in xrange(4096):
    cmd_args = [offset, limit]
    print(cmd, cmd_args)
    cursor.execute(cmd, cmd_args)
    rows = cursor.fetchall()
    offset += limit
    print(cmd, "offset=%s limit=%s" % (offset, limit), "rows", len(rows))
    if len(rows) == 0:
      break

    for row in rows:
      data = dict(zip(columns, row))
      out.append(data)
  return out

def query_data(q_admin_id):
  opts = get_db_opts()
  conn = pymysql.connect(**opts)

  ac_id_arr = []
  ac_code_arr = []
  m_id_arr = []
  ac_money_arr = []
  ac_user_money_arr = []
  ac_name_arr = []
  remark_arr = []
  ip_arr = []
  datetime_arr = []
  t_id_arr = []
  out_sn_arr = []

  with conn.cursor() as cursor:
    admins = scan_all(cursor, TABLE_ADMIN, TABLE_ADMIN_COLUMNS)
    accounts = scan_all(cursor, TABLE_ACCOUNT, TABLE_ACCOUNT_COLUMNS)
    orders = scan_all(cursor, TABLE_ORDER, TABLE_ORDER_COLUMNS)
    lowers = scan_all(cursor, TABLE_LOWER, TABLE_LOWER_COLUMNS)

    lower_by_id = {}
    order_by_id = {}
    for order in orders:
      order_by_id[order['id']] = order
    for lower in lowers:
      lower_by_id[lower['id']] = lower

    for act in accounts:
      m_id = act['m_id']
      out_sn = "-"
      if m_id == q_admin_id:
        #print("act", act)
        ac_id = act['ac_id']
        ac_type = act['ac_type']
        t_id = act['t_id']
        remark = act['remark']
        ac_money = round(act['ac_money'], 2)
        ac_user_money = round(act['ac_user_money'], 2)
        ip = act['ip']
        add_time = act['add_time']
        ac_code = act['ac_code']
        date_sec = None

        #dt = datetime.fromtimestamp(add_time)
        dt = ts_to_tz_shanghai(add_time)
        print("ac_id=%s dt" % ac_id, dt)
        date_desc = dt.strftime('%Y-%m-%d %H:%M:%S')

        ac_name = name_by_ac_type[ac_type]
        if ac_type in [23, 81, 83, 84, 91]: 
          lower = lower_by_id[t_id]
          out_sn = lower['sn']
        elif ac_type in [82]: 
          order = order_by_id[t_id]
          out_sn = order['out_sn']
          

        m_id_arr.append(m_id)
        t_id_arr.append(t_id)
        remark_arr.append(remark)

        ac_id_arr.append(ac_id)
        ac_name_arr.append(ac_name)
        ac_code_arr.append(ac_code)
        ac_money_arr.append(ac_money)
        ac_user_money_arr.append(ac_user_money)
        ip_arr.append(ip)
        datetime_arr.append(date_desc)
        out_sn_arr.append(out_sn)

  return ac_id_arr, ac_name_arr, t_id_arr, ac_code_arr, m_id_arr, remark_arr, ac_money_arr, ac_user_money_arr, ip_arr, datetime_arr, out_sn_arr

def main():
  argv = list(sys.argv)
  argv.pop(0)
  print("argv", argv)

  out_fp = argv[0]
  q_admin_id = int(argv[1])

  dirpath = os.path.dirname(out_fp)
  if not os.path.exists(dirpath):
    os.makedirs(dirpath)

  now_t = time.time()
  now = ts_to_tz_shanghai(now_t)

  #out_fp = '/var/tmp/pays/pay_accounts_%s.xlsx' % now.strftime('%Y%m%d_%H%s%S')
  #sys.stdout.write(out_fp)

  #return# out_fp

  rtn = query_data(q_admin_id)

  ac_id_arr, ac_name_arr, t_id_arr, ac_code_arr, m_id_arr, remark_arr, ac_money_arr, ac_user_money_arr, ip_arr, datetime_arr, out_sn_arr = rtn


  data = OrderedDict([
    (u'交易編號', ac_code_arr),
    (u'商戶訂單號', out_sn_arr),
    (u'商戶ID', m_id_arr),
    (u'第三方ID', t_id_arr),
    (u'变动金额', ac_money_arr),
    (u'操作后余额', ac_user_money_arr),
    (u'类型', ac_name_arr),
    (u'備註', remark_arr),
    (u'IP', ip_arr),
    (u'時間', datetime_arr),
  ])


  df = pd.DataFrame(data=data)
  
  #XlsxWriter
  with pd.ExcelWriter(out_fp, engine='xlsxwriter') as writer:
  #with pd.ExcelWriter(out_fp) as writer:
    df.to_excel(writer, index=False)

    workbook = writer.book
    print("sheets", writer.sheets)
    sheet = writer.sheets['Sheet1']
    sheet.set_column('A:A', 20)
    sheet.set_column('B:B', 28)

    sheet.set_column('E:E', 12)
    sheet.set_column('F:F', 12)
    sheet.set_column('G:G', 27)
    sheet.set_column('H:H', 30)
    sheet.set_column('I:I', 18)
    sheet.set_column('J:J', 18)
    sheet.set_column('K:K', 18)

    #writer.save()


  


if __name__ == "__main__":
  main()

