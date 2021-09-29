file = open("E:\GitHub\Python\File Management\TextFile",'r') #put path of file in ""
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
print(line_count)