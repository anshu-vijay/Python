sentence = "hey user, happy coding."
lst = []
word = ""
for i in sentence:
    if  i.isalpha():
        word = word + i
    elif i.isspace():
        lst.append(word)
        word = ""
if word:
    lst.append(word)
print(lst)