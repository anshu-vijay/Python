file = open("E:\GitHub\Python\File Management\HelloWorld",'r') #put path of file in ""
with open("E:\GitHub\Python\File Management\HelloWorld",'w') as newFileData:
    newFileData.write("Hello user \nHow are you doing?")
    newFileData.write("Nice to meet you.")
print(file.read())