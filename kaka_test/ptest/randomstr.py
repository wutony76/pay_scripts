import random

def main():
  

  str = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z",]
  print(str)
  
  rstr = random.sample(str,5)
  print(''.join(rstr))


if __name__ == '__main__':
  main()