


str1 = "08:47:11 up 18 days, 22:57,  6 users,  load average: 0.03, 0.05, 0.12"
strvalue = "average"

strtake = str1[str1.index(strvalue)+8:]

strsplit = strtake.split(",")


strsplit[:] = [float(x) for x in strsplit] 

print(type(strsplit))
#print(type(x[0]))
print(type(strsplit[0]))
for item in strsplit:
  print (item)

print("float",strsplit[0])

if strsplit[0]>strsplit[1] or strsplit[0]>strsplit[2]:
  print ("up")
elif strsplit[0]<strsplit[1] and strsplit[0]<strsplit[2]:
  print ("down")
else:
  print ("Idle") 



print(strtake)
