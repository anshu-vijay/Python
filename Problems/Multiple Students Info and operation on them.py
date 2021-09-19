class A:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
class B:
    def __init__(self,grade,students_list):
        self.grade = grade
        self.students_list = students_list

    def nameOfMaxMarksStudent(self):
        max = 0
        if (len(self.students_list)==0):
            return 'NONE'
        else:
            for student in self.students_list:
                if student.marks>max:
                    max = student.marks
            for student in self.students_list:
                if student.marks == max:
                    print(student.name)
                    print(student.marks)

    def sortMarks(self):
        marks_list=[]
        for student in self.students_list:
            marks_list.append(student.marks)
        marks_list.sort()
        if len(marks_list) == 0:
            return 'NONE'
        else:
            for i in marks_list:
                print(i)



lst = []
n = int(input("Enter number of entries : "))
for student in range(n):
    name = input("Enter name : ")
    marks = int(input("Enter marks : "))
    lst.append(A(name,marks))

obj = B('A',lst)
obj.nameOfMaxMarksStudent()
print("Sorted Marks List: ")
obj.sortMarks()


