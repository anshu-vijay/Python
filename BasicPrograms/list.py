
print("**********************************************")
fruits = ['apple','mango',1,5,'@']
print("length of fruits list",len(fruits)) #length of list
print(fruits[2]) #printing a particular element
fruits[2] = 'banana' #adding new element
print(fruits) # printing list
print("*********************************************")
paragraph = "Global         warming is a term used for the observed century-scale rise in the average temperature of " \
            "the Earth's climate system and its related effects. Scientists are more than 95% certain that nearly all of global warming is caused by increasing concentrations of greenhouse gases (GHGs) and other human-caused emissions."
print(len(paragraph))
print(list(paragraph))
print(len(list(paragraph)))
print(list(paragraph.split(" ")))
print("with single space: ",len(list(paragraph.split(" "))))
print(list(paragraph.split()))
print("with multiple spaces : ",len(list(paragraph.split())))
print(paragraph.count("the"))
print(paragraph.__contains__('effects'))
print('effects' in paragraph)
print("*********************************************")
print(list("computer"))
car =("audi","merc","skoda","rangerover")
print(list(car))

