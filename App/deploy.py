import random, math
from . import database

class Place:
    def __init__(self, columnIndex, rowIndex, deskNo, holding = None):
        self.columnIndex = columnIndex
        self.rowIndex = rowIndex
        self.deskNo = deskNo
        self.holding = holding
    
    def get_place_infos(self) -> tuple:
        return self.columnIndex, self.rowIndex, self.deskNo, self.holding

    def __str__(self) -> str:
        return f"{self.columnIndex}, {self.rowIndex}, {self.deskNo}"
    

def check_all_desks(algorithm: str, options: list, deskInfos: list) -> bool:
    print()
    print(algorithm)
    print(options)
    print(deskInfos)
    print()
    return True

def get_students(exams):
    grades = list()
    for examName, gradess in exams.items():
        grades.extend(gradess)
        
    students = database.get_grade_given_students(grades)

    return students
        
def get_places(arr) -> list[Place]:
    places = list()
    for columnIndex, column in enumerate(arr):
        for rowIndex, desk in enumerate(column):
            for deskNo, holding in desk.items():
                place = Place(columnIndex, rowIndex, deskNo, holding)
                places.append(place)

    return places

def empty_count(arrangement) -> int:
    count = 0
    for columnIndex, column in enumerate(arrangement):
        for rowIndex, desk in enumerate(column):
            for deskNo, place in desk.items():
                if not place:
                    count += 1
                    
    return count
    
def seperate_students(students) -> int:
    seperatedStudents = dict()
    lastGrade = ""
    for student in students:
        grade = student[4]
        if grade != lastGrade:
            lastGrade = grade
            seperatedStudents.update({grade: list()})
        
        seperatedStudents[grade].append(student)

    for gradeName, students in seperatedStudents.items():
        random.shuffle(students)

    return seperatedStudents

def students_left(seperatedStudents: dict) -> int:
    studentsLeft = 0
    for gradeName, students in seperatedStudents.items():
        studentsLeft += len(students)
        
    return studentsLeft
            
def deploy_students(classrooms: dict, students: list, exam) -> dict:
    attempt = 5
    while attempt:
        seperatedStudents = seperate_students(students)
        for gradeName, gradeStudents in seperatedStudents.items():
            attemptGrade, ended = 2, False
            while attemptGrade and not ended:
                for classroomName, classroomsDict in classrooms.items():
                    # Buraya ????retmen masas?? kontrol?? ekle
                    arr = classroomsDict["oturma_duzeni"]
                    # E??er hala ????renci varsa ama left s??f??r ????k??yorsa ????renci say??s?? salon say??s??ndan azd??r.
                    # Bu durumda left i??in bir yaparsak her s??n??fa birer tane olacak ??ekilde ????rencileri da????tmay?? dener.
                    left = len(gradeStudents) // len(classrooms)
                    if len(gradeStudents) and not left:
                        left = 1
                        
                    emptyCount = empty_count(arr)
                    places = get_places(arr)
                    while emptyCount and left:
                        emptyCount -= 1

                        placeCount = len(places)
                        placeIndex = random.randint(0, placeCount - 1)
                        place = places[placeIndex]

                        columnIndex, rowIndex, deskNo, holding = place.get_place_infos()
                        if holding:
                            continue
                        
                        student = gradeStudents[-1]
                        
                        deskInfos = [columnIndex, rowIndex, deskNo, holding]
                        algorithmName = exam.algorithmName
                        options = exam.optionList
                        if check_all_desks(algorithm = algorithmName, options = options, deskInfos = deskInfos):
                            arr[columnIndex][rowIndex][deskNo] = student
                            gradeStudents.pop(-1)
                            left -= 1
                        
                        places.remove(place) 

                if not gradeStudents:
                    ended = True
                attemptGrade -= 1
                
        studentsLeftCount = students_left(seperatedStudents)
        if studentsLeftCount:
            attempt -= 1
        else:
            attempt = 0

    return classrooms

def print_classrooms(classrooms):
    for classroom_name, columns in classrooms.items():
        print(f"Classroom: {classroom_name}")
        for column in columns:
            for row in column:
                print(row)
        print("\n")

def print_students(seperatedStudents):
    for gradeName, students in seperatedStudents.items():
        print(gradeName)
        [print(student) for student in students]
        print()

def deploy_and_get_classrooms(exam):
    students = get_students(exam.exams)
    classroomNames = exam.classroomNames
    classrooms = database.get_name_given_classrooms(classroomNames)
    
    classrooms = deploy_students(classrooms, students, exam)
    return classrooms


if __name__ == '__main__':
    students = [("Yusuf", "11/A"), ("Ali",  "11/A"), ("Veli", "11/A"), ("Deli", "11/B"),
                ("??sta", "11/B"), ("Ahmet", "11/C"), ("Kemal", "11/C"), ("Mehmet", "11/C")]

    classrooms = {
                "classroom1": [[{1: None, 2: None}, {3: None, 4: None},  {5: None, 6: None}],
                               [{7: None, 8: None}, {9: None, 10: None}, {11: None, 12: None}],
                               [{13: None, 14: None}, {15: None, 16: None}]],
                            
                "classroom2": [[{1: None, 2: None}, {3: None, 4: None},  {5: None, 6: None}],
                               [{7: None, 8: None}, {9: None, 10: None}, {11: None, 12: None}]]
                }

    classrooms = deploy_students(classrooms, students)
    print_classrooms(classrooms)