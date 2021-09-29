import re
#Print the position (start- and end-position) of the first match occurrence
#The regular expression looks for any words that starts with an upper case "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)  #(12, 17)
print(x.span())

#Print the string passed into the function
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) #The rain in Spain
print(x.string)

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt) #Spain
print(x.group())