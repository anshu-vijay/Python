import re

#Check if the string has any a, r, or n characters:
txt = "The rain in Spain"
x = re.findall("[arn]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



#Check if the string has any characters between a and n:
txt = "The rain in Spain"
x = re.findall("[a-n]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any 0, 1, 2, or 3 digits:
txt = "I have 509 dollars"
x = re.findall("[0123]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any digits:
txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any two-digit numbers, from 00 to 59:
txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any characters from a to z lower case, and A to Z upper case:
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



#Check if the string has any + characters:
txt = "1+8 times before 11:45 AM"
x = re.findall("[+]", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
