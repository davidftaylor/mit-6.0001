class Grades(object):

    def __init__(self):
        """ Create empty grade book """
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """ Assumes: student is of type Student
            Add student to the grade book """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """ Assumes: grade is a float
            Add grade to the list of grades for student """
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """ Return a list of grades for student """
        try: # return copy of list of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """ Return a sorted list of the students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] # return copy of list of students


