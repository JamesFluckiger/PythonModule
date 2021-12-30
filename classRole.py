class Student():

    course = "English"
    teacher = "James"

    def __init__(self, name, favColor, present):
        self.name = name
        self.favColor = favColor
        self.present = present




def main():

    print("Let's create the class role.")
    classRole = []
    
    while True:
        userinput = input("Add student? (y/n): ")
        if userinput == "y":
            name = input("Enter name: ")
            favColor = input("Enter favorite color: ")
            name = Student(name, favColor, False)
            classRole.append(name)
        elif userinput == "n":
            break
        else:
            print("Invalid input.")

    print("Here's all the students favorite colors!")
    for i in classRole:
        print(i.favColor)


main()