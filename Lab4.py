"""
Christina Shafer
CIS 41A - Fall 2018
Nov 13,2018
Lab 4

Summary:
A program that maintains a class list for a student.  The student can take for-credit classes or non-credit classes
Program lets student enter data on their current classes, then the program prints out the class list, the supplies
needed for each class day and the grade record for each for-credit class

"""
from course import *

class ClassList:
    """
    object that holds a list of courses
    """
    def __init__(self):
        self._courses=[]
        self.addCourses()

    def getCourses(self):
        """
        method to return the list of courses
        :return: _courses
        """
        return self._courses

    def addCourses(self):
        """
        method to prompt user for courses for the ClassList
        :return:
        """
        numCourses=int(input("How many courses do you want to enter?"))  #can throw an exception
        """
        below is the non-Python way
        while not(numCourses.isdigit()):
            print("Number of courses must be a digit")
            numCourses=input("How many courses do you want to enter?")
            """
        for i in range(numCourses):
            choice =input("Enter 'c' for credit or 'nc' for non-credit:")
            while choice not in ("c","nc","C","NC"):
                print("Invalid Class type. ")
                choice =input("Enter 'c' for credit or 'nc' for non-credit:")
            if choice in ("c","C"):
                done=False
                while done==False:
                    info = input("Enter comma-separated class name, time, days, units: ")
                    info=info.split(",")
                    while len(info)!=4:
                        print("Incorrect number of fields entered.")
                        info = input("Enter comma-separated class name, time, days, units: ")
                        info=info.split(",")
                    try:
                        newCourse=CreditCourse(info[0],info[1],info[2],info[3])
                        done=True
                    except (ValueError):
                        print("Incorrect data entered")
                newCourse.addSupplies()
                newCourse.addGrades()
            else:
                done=False
                while done==False:
                    info = input("Enter comma-separated class name, time, days: ")
                    info=info.split(",")
                    while len(info)!=3:
                        print("Incorrect number of fields entered.")
                        info = input("Enter comma-sarated class name, time, days: ")
                        info=info.split(",")
                    try:
                        newCourse= NonCreditCourse(info[0],info[1],info[2])
                        done=True
                    except (ValueError):
                        print("Incorrect data entered")
                newCourse.addSupplies()
                newCourse.addActivities()
            self._courses.append(newCourse)

    def printSupplies(self,day):
        """
        method to print the supplies needed in all courses for a particular day
        :param day: could be M,T,W,R,F
        :return: no return, just a print
        """
        supplySet=set()
        #create a list of courses on the day
        daysClasses=[course for course in self._courses if day in course._classDays]
        for course in daysClasses:
            courseSupplies=set(course.getSupplies())
            supplySet=supplySet.union(courseSupplies)
        items= sorted(supplySet)
        if len(items)>0:
            print(day + ": " , end="")
            print(', '.join(items))


    def report(self):
        """
        method to print all info on classList. calls two methods: printSupplies, printClassList
        :return:
        """
        print("Supplies for each day of class:")
        allDays=['M','T','W','R','F']
        for day in allDays:
            self.printSupplies(day)
        self.printClassList()


    def printClassList(self):
        """
        method to print out all class info for classes in ClassList in alphabetical order
        :return:
        """
        print()
        print("Activities for each class")
        alphaList=sorted(self._courses)
        for i in range(len(alphaList)):
            print()
            print(str(alphaList[i]))
            alphaList[i].printActivities()




def main():
    """the main"""
    L=ClassList()
    L.report()

main()


