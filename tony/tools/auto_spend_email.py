from __future__ import print_function

import time
import smtplib
import queue as Queue
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def new_mail( data ):
  mail = MIMEMultipart()  #建立MIMEMultipart物件
  mail["subject"] = "Learn Code With Mike"  #郵件標題
  mail["from"] = "xizhiw247@gmail.com"  #寄件者
  mail["to"] = "xizhiw247@gmail.com" #收件者
  mail.attach(MIMEText(data))  #郵件內容
  return mail
  


def main():
  print("start python test.")

  que = Queue.Queue()
  mail = new_mail("Demo python send email")
  #print("mail.", mail)


  with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
      smtp.ehlo()  # 驗證SMTP伺服器
      smtp.starttls()  # 建立加密傳輸
      #smtp.login("pydemo123@gmail.com", "應用程式密碼")  # 登入寄件者gmail
      smtp.login("xizhiw247@gmail.com", "xtafkutzufxykfzz")  # 登入寄件者gmail
      _index = 0
      while True:
        _index += 1 
        _mail_msg = "%s,Demo python send email. %s"%(str(_index), str(time.time()))
        mail = new_mail(_mail_msg)
        #smtp.send_message(mail)  # 寄送郵件
        smtp.send_message(mail)  # 寄送郵件

        print("Complete!", _index)
        try:
          que.get(timeout = 1)
        except Queue.Empty:
          pass
        

      print("Complete!")
    except Exception as e:
      print("Error message: ", e)



  #spend_mail()



if __name__ == "__main__":
  main()
