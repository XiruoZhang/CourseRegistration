class professor:

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

    def viewcourses(self):
        for c in self.sourses:
            print(c + " ")

    def chooseCourse(self, course):
        self.courses.add(course)

    def increateCourseSize(self, course):
        print()

    def remove(self):
        return "delete from professors where id = " + str(self.id)

    def insert(self):
        return "insert into professors values (" + str(self.id) + ", '"+ self.firstName +"', '"+ self.lastName + "')";


