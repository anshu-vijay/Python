file = open("E:\GitHub\Python\File Management\HelloWorld",'r') #put path of file in ""
data = file.read()
number_of_characters = len(data)
print("With spaces length= ",number_of_characters)

data_without_spaces = data.replace(" ","")
number_of_characters = len(data_without_spaces)
print("Without spaces length= ",number_of_characters)