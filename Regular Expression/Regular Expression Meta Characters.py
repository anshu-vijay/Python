import re

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

#Find all lower case characters alphabetically between "a" and "m":
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)

#Find all digit characters:
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
txt = "hello world"
x = re.findall("he..o", txt)
print(x)

#Check if the string starts with 'hello':
txt = "hello world"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#Check if the string ends with 'world':
txt = "hello world"
x = re.findall("world$", txt)

if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")

#Check if the string contains "ai" followed by 0 or more "x" characters:
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains "ai" followed by 1 or more "x" characters:
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("ain+", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string contains "a" followed by exactly two "l" characters:
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("al{2}", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



#Check if the string contains either "falls" or "stays":
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")