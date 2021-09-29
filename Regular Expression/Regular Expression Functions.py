import re

#findall() - function returns a list containing all matches.
txt = "The rain in Spain"
x = re.findall("ai", txt) #['ai', 'ai']
print(x)
#If no matches are found, an empty list is returned
x = re.findall("Portugal", txt) #[]
print(x)

#search() - function searches the string for a match, if there is more than one match, only the first occurrence of the match will be returned
txt = "The rain in Spain"
x = re.search("\s", txt) #3
print("The first white-space character is located in position:", x.start())
#If no matches are found, the value None is returned
x = re.search("Portugal", txt) #None
print(x)

#split() - function returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split("\s", txt) #['The', 'rain', 'in', 'Spain']
print(x)
#You can control the number of occurrences by specifying the maxsplit parameter
x = re.split("\s", txt, 1)  #['The', 'rain in Spain']
print(x)

#sub() - function replaces the matches with the text of your choice
txt = "The rain in Spain"
x = re.sub("\s", "+", txt) #The+rain+in+Spain
print(x)
#You can control the number of replacements by specifying the count parameter
x = re.sub("\s", "+", txt, 2) #The+rain+in Spain
print(x)



