
print("**********************************************")
fruits = ['apple','mango',1,5,'@']
print("length of fruits list",len(fruits)) #length of list
print(fruits[2]) #printing a particular element
fruits[2] = 'banana' #adding new element
print(fruits) # printing list
print("*********************************************")
paragraph = "Global         warming is a term used for the observed century-scale rise in the average temperature of " \
            "the Earth's climate system and its related effects. Scientists are more than 95% certain that nearly all of global warming is caused by increasing concentrations of greenhouse gases (GHGs) and other human-caused emissions."
print("Length of paragraph : " ,len(paragraph))
print("paragraph to list: ",list(paragraph))
print("legth of paragraph list: ",len(list(paragraph)))
print("with single space: ",list(paragraph.split(" ")))
print("Length with single space: ",len(list(paragraph.split(" "))))
print("Length with multiple spaces: ",list(paragraph.split()))
print("Length with multiple spaces : ",len(list(paragraph.split())))
print("Counting the in paragraph: ",paragraph.count("the"))
print("Does paragraph contains effects?: ",paragraph.__contains__('effects'))
print("with single space: effects?: ",'effects' in paragraph)
print("*********************************************")
print(list("computer"))
car =("audi","merc","skoda","rangerover")
print("Tuple to List: ",list(car))

