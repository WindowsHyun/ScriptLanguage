class Department:
    def __init__(self, name,student):
        self.name = name
        self.student = student
    def printInfo(self):
        print("[학과] :{0} [이름] {1})".format(self.name, self.student))


class Student(Department):
    def __init__(self, name,student):
        Department.__init__(self,name,student)


def main():
    student_l = list()
    for i in range(2):
        deptName = input("학과입력:")
        studentName = input("이름입력:")
        student_l.append(\
            Student(deptName, studentName))
        for i in student_l:
            i.printInfo()
            
