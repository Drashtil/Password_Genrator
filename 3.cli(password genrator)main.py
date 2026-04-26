import random
def genpass(a,b,c,d):
  password = ""
  l = "abcdefghijklmnopqrstuvwxyz"
  u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  s = "!@#$%^&*()_+=-"
  n = "0123456789"

  gen = l
  if(a=="y"):
    gen += u
  if(b == "y"):
    gen += s
  if(c == "y"):
    gen +=  n
    password =""

  for i in range(d):
     password += random.choice(gen)
  return password

while True:
  print("Password Generator")
  d = int(input("Enter the length of the password: "))
  a = input("Do you want to have uppercase letters in your password? (y/n): ")
  b = input("Do you want to have special characters in your password? (y/n): ")
  c = input("Do you want to have numbers in your password? (y/n): ")
  e = int(input("how many passwords do you want to generate?: "))

  for i in range(e):
    print(genpass(a,b,c,d))

  z = input("Do you want to generate more passwords? (y/n): ")
  if(z != "y"):
    break
  else:
    continue
      
    