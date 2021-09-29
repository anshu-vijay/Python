import re

#Check if the string starts with "The":
txt = "The rain in Spain"
x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")


#Check if "ain" is present at the end of a WORD:
txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



#Check if "ain" is present at the beginning of a WORD:
txt = "The rain in Spain"
x = re.findall(r"\brai", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



#Check if "ain" is present, but NOT at the beginning of a word:
txt = "The rain in Spain"
x = re.findall(r"\Bain", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if "ain" is present, but NOT at the end of a word:
txt = "The rain in Spain"
x = re.findall(r"ain\B", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains any digits (numbers from 0-9):
txt="I have 59 Dollars"
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string does not contain any digits (numbers from 0-9):
txt="I have 59 Dollars"
x = re.findall("\D", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every white-space character:
txt = "The rain in Spain"
x = re.findall("\s", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every non white-space character:
txt = "The rain in Spain"
x = re.findall("\S", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
txt = "The rain in_Spain. And I have 50 Dollars."
x = re.findall("\w", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
txt = "The rain in_Spain. And I have 50 Dollars."
x = re.findall("\W", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string ends with "Spain":
txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)
print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")