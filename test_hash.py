import uuid
import hashlib
import random
import requests

def encode_param(text):

  base = "PXhw7UT1B0a9kQDKZsjIASmOezxYG4CHo5Jyfg2b8FLpEvRr3WtVnlqMidu6cN"
  #print("base", base, len(base))
  base_ix = list(range(len(base)))

  out = ""
  arr = [ord(c) for c in text]
  for i in range(len(text)):
    
    t = text[i]

    num0 = base.find(t)
    if num0 == -1:
      code = t
    else:
      code = base[(num0+3)%62]

    num1 = random.choice(base_ix)
    num2 = random.choice(base_ix)
    
    a = base[num1] + code + base[num2]
    out = out + a

    #print("i=%s" % i, "a", a)

  return out

if __name__ == "__main__":

  address = "THQscEopvnPmTnWSBkSgDC9HE3m5SC2yyE"
  url = "https://back.quantum-us.org/index.php/Home/Tron/rechange"
  txid = "d63a0a2e753464247d5a594d4a44d7274e70902c33c6da6eaeb0fa5a488b3555"

  post_data = {
    "unknown": encode_param(address),
    "amount": 3500,
    "day": 12,
    "txid": txid,
  }
  rep = requests.get(url, params=post_data)
  print("rep1", rep, rep.content)
  rep_data = rep.json()
  print("rep2", rep_data)


