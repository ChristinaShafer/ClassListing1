class Course:
    """
    class that contains information for a course
    """
    def __init__(self,className,startTime,classDays):
        self._verify(className, startTime, classDays)
        self._className = className.upper()
        self._startTime = startTime
        self._classDays = classDays.upper()
        self._supplies = []

    def __str__(self):
        return self._className +', ' + self._startTime +', ' + self._classDays

    def __lt__(self, other):
        if self._className < other._className:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._className > other._className:
            return True
        else:
            return False

    def addSupplies(self,supplyList=[]):
        """
        method to add supplies to the course
        :param supplyList: list of supplies needed for class
        :return: none
        """
        done =False
        if len(supplyList)>0:
            for item in supplyList:
                self._supplies.append(item);  #use extend
            done=True
        while not done:
            supplies = input("Enter a comma-separated list of supplies:")
            if len(supplies)>0:
                new_supplies=(supplies.split(","))
                for item in new_supplies:
                    self._supplies.append(item.strip())
                done=True

    def getSupplies(self):
        """
        method to return supply list from course object
        :return: list of supplies
        """
        return self._supplies

    def _verify(self,className,startTime,classDays):
        """private method to verify startTime and classDays are formatted correctly
        :param: className (must not be empty), startTime(formatted HH:MM with MM in 00 or 30), classDays in (M,T,W,R,F)
        """
        className=className.strip()
        startTime=startTime.strip()
        classDays=classDays.strip()
        classDays=classDays.upper()
        #verifyClassname
        if not(len(className)>0):
            raise ValueError("Classname must not be empty.")

        #verify startTime format
        if not(4<=len(startTime)<=5) or not(startTime[-3]==":"):
            raise ValueError("Start time must be in the format HH:MM.")

        #verify hours and minutes in correct ranges
        colon=startTime.find(":")
        hour=startTime[0:colon]
        if not(hour.isdigit()) or not(1<=int(hour)<=12) or not(startTime[colon+1:] in ('00','30')):
            raise ValueError("Incorrect time entered. Hour must be between 1-12. Minute must be '00' or '30'")

        #verify classDays
        if len(classDays)<1:
            raise ValueError("Class Days must not be empty. Possible values are: MTWRF")
        dayList=list(classDays)
        for char in dayList:
            if char.upper() not in ('M','T','W','R','F'):
                raise ValueError("Incorrect class day. Possible values are: MTWRF")


class NonCreditCourse(Course):
    """
    child object of Course.  adds activities to object and printActivities method.
    """
    def __init__(self,className,startTime,classDays):
        super().__init__(className,startTime,classDays)
        self._activities = []

    def addActivities(self,new_activities=[]):
        """ Adds activities to Non-Credit Course
        :param new_activities: list of activities to add to non-credit course
        :return:
        """
        done =False
        if len(new_activities)>0:
            done=True
            for act in new_activities:
                    self._activities.append(act)
        while not done:
            acts = input("Enter a comma-separated list of activities:")
            if len(acts)>0:
                new_activities=acts.split(",")
                for act in new_activities:
                    self._activities.append(act)
                done=True
    def printActivities(self):
        """prints out the course activities"""
        print(', '.join(self._activities))

class CreditCourse(Course):
    """
    child class of Course.  Adds course units as well as a dictionary of activities and the scores associated
    with them (_grades)
    """

    def __init__(self,className,startTime,classDays,units):
        self._verifyUnits(units)
        super().__init__(className,startTime,classDays)
        self._units = units
        self._grades = {}

    def __str__(self):
        return self._className + ', ' + self._startTime + ', ' + self._classDays + ', ' + self._units + " units"

    def _verifyUnits(self,units):
        """verifies that the units passed to the constructor are valid.
        @:return - none, but can throw an exception
        """
        _VALID_UNITS=['0.5','1.0','1.5','2.0''2.5','3.0','3.5','4.0','4.5','5.0']
        units=units.strip()
        if units not in _VALID_UNITS:
            raise ValueError("Invalid units entered.  Please use format x.x")


    def addGrades(self,tasks=[],scores=[]):
        """Adds tasks and corresponding scores to the _grades dictionary when input is valid.
        prints an error message, but does not throw an exception in case of non-valid input
        """
        if len(tasks)!=len(scores):
            print("Incorrect data entered.  Number of tasks and corresponding scores must be the same.")
        elif len(tasks)>0:
                self._grades = dict(zip(tasks,scores))
        else:
                tasks = input("Enter a comma-separated list of tasks:")
                while len(tasks)<1:
                    tasks = input("Enter a comma-separated list of tasks:")
                tasks=tasks.split(",")
                scores = input("Enter a comma-separated list of corresponding scores:")
                while len(scores)<1:
                    scores = input("Enter a comma-separated list of corresponding scores:")
                scores=scores.split(",")
                #NEED TO TEST FOR valid input (a float)
                for i in range(len(scores)):
                    scores[i]=float(scores[i])   #can raise an exception
                if len(tasks) == len(scores):
                    self._grades = dict(zip(tasks,scores))
                else:
                    print("Incorrect data entered.  Number of tasks and corresponding scores must be the same.")

    def printActivities(self):
        """prints _grades dictionary"""
        for k,v in self._grades.items():
            print("{:10s} {:>15.1f}".format(k.lstrip()+":",v))

#function
def printActivities(obj):
    """function that calls the object method 'printActivities()' for the passed object"""
    obj.printActivities()
"""
def main() :
    c = CreditCourse("CIS 41A","9:30","MW","4.5")
    c.addSupplies(["laptop"])
    c.addGrades(["Assignments","Exams","Quizzes"],[92.5,86.0,88.4])
    print("Class:\n" + str(c))
    print("Supplies:", ', '.join(c._supplies))
    printActivities(c)

    print()
    nc = NonCreditCourse("Hiking","8:00","T")
    nc.addSupplies(["boots","sunscreen","hat"])
    nc.addActivities(["Big Sur","Coastal Trail","Mt. Diablo"])
    print("Class:\n" + str(nc))
    print("Supplies:" + ', '.join(nc._supplies))
    printActivities(nc)


main()
"""
