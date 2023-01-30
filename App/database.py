### database.py
import sqlite3

db = sqlite3.connect("database.db")
cur = db.cursor()

def createTables():
    # FIRST INFOS
    """
    cur.execute(""
        CREATE TABLE IF NOT EXISTS "first_infos" (
	        "date"	TEXT)
        "")
    """
    
    # OGRENCILER
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "ogrenciler" (
	        "no" INTEGER UNIQUE,
	        "ad" TEXT,
	        "soyad"	TEXT,
	        "cinsiyet"	TEXT,
            "sinif" TEXT)
        """)
    
    # SALONLAR DUZENLERI
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "salonlar" (
	        "derslik_adi"	TEXT UNIQUE,
	        "ogretmen_yonu"	TEXT,
	        "kacli"	TEXT,
	        "oturma_duzeni"	TEXT)
        """)

    # OKUL BİLGİLERİ
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "okul_bilgileri" (
	        "okul_adi"	TEXT,
	        "mudur_adi"	TEXT,
	        "okul_turu"	TEXT,
	        "ogrenci_sayisi"	INTEGER,
	        "sinif_sayisi"	INTEGER,
	        "salon_sayisi"	INTEGER)
        """)
    
    # GEÇMİŞ SINAVLAR
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "sinavlar" (
        	"id"	INTEGER NOT NULL,
	        "tarih"	TEXT NOT NULL,
	        "salonlar"	TEXT NOT NULL,
	        PRIMARY KEY("id"))
        """)

createTables()   

######################### FONKSIYONLAR ############################

"""
# İLK AÇILIŞ MI ? 
def get_first_date():
    QUERY = "SELECT * FROM first_infos"
    try:
        date = cur.execute(QUERY).fetchall()[0][0]
    except Exception as e:
        print(e)
        return False
        
    return date

def set_first_date(date: str):
    cur.execute("INSERT OR REPLACE INTO first_infos VALUES(?)", (date,))
    db.commit()
"""

#ŞUBE İSİMLERİ
def get_all_grade_names():
    QUERY = "SELECT sinif FROM ogrenciler"
    tumSiniflar = cur.execute(QUERY)
    siniflar = set()
    [siniflar.add(sinif[0]) for sinif in tumSiniflar] 
    siniflar = list(siniflar)
    siniflar.sort()
    return siniflar

#ÖĞRENCİLER
def add_one_student(student: list):
    if len(student) != 0:
        cur.execute("INSERT OR REPLACE INTO ogrenciler VALUES(? ,?, ?, ?, ?)", student)
        db.commit()

def add_multiple_students(students: list):
    if len(students) != 0:
        for student in students:
            cur.execute("INSERT OR REPLACE INTO ogrenciler VALUES(?, ?, ?, ?, ?)", [data for data in student])
        db.commit()

def update_student(student):
    removeNo = student[0]
    # NUMARAYI BULUP O OGRENCIYI SIL VE YENISINI EKLE YAPABILIRSIN
    # YA DA NUMARAYI BULUP DIGER DEGERLERINI DEGISTIREBILIRSIN

def get_student_counts_per_every_grade():
    QUERY_9 = "SELECT * FROM ogrenciler WHERE sinif LIKE '%9%'"
    QUERY_10 = "SELECT * FROM ogrenciler WHERE sinif LIKE '%10%'"
    QUERY_11 = "SELECT * FROM ogrenciler WHERE sinif LIKE '%11%'"
    QUERY_12 = "SELECT * FROM ogrenciler WHERE sinif LIKE '%12%'"
    QUERY_TOTAL = "SELECT ad FROM ogrenciler"
    totalCount = str(len(cur.execute(QUERY_TOTAL).fetchall()))
    count9 = str(len(cur.execute(QUERY_9).fetchall()))
    count10 = str(len(cur.execute(QUERY_10).fetchall()))
    count11 = str(len(cur.execute(QUERY_11).fetchall()))
    count12 = str(len(cur.execute(QUERY_12).fetchall()))
    return [totalCount, count9, count10, count11, count12]
    
def get_all_students(number = False, fullname = False, grade = False, withGrades = False):
    QUERY = "SELECT * FROM ogrenciler ORDER BY sinif, no"
    QUERY_NUM = "SELECT * FROM ogrenciler WHERE no = ? ORDER BY sinif, no"
    QUERY_CLASS = "SELECT * FROM ogrenciler WHERE sinif = ? ORDER BY sinif, no"
    students = cur.execute(QUERY).fetchall()

    if withGrades:
        students = cur.execute(QUERY).fetchall()
        grades = {}
        for grade in get_all_grade_names():
            grades.update({grade: []})

        for student in students:
            studentGrade = student[4]
            grades[studentGrade].append(student)
            
        return grades

    if number:
        students = cur.execute(QUERY_NUM, (number,)).fetchall()
        
    elif fullname:
        fullname = fullname.upper()
        students = cur.execute(QUERY).fetchall()
        students = [student for student in students if (fullname in (student[1] + " " + student[2]))]

    elif grade:
        students = cur.execute(QUERY_CLASS, (grade,)).fetchall()

    return students

def remove_one_student(number):
    QUERY = "DELETE FROM ogrenciler WHERE no = ?"
    cur.execute(QUERY, (number,))
    db.commit()

def remove_all_students():
    QUERY = "DELETE FROM ogrenciler WHERE 1=1"
    cur.execute(QUERY)
    db.commit()

################### CLASSROOMS ##############

def add_new_classroom(*values):
    QUERY = "INSERT OR REPLACE INTO salonlar VALUES(?, ?, ?, ?)"
    cur.execute(QUERY, values)
    db.commit()

def get_all_classrooms(onlyNames = False):
    QUERY = "SELECT derslik_adi FROM salonlar"
    QUERY_2 = "SELECT derslik_adi, ogretmen_yonu, kacli, oturma_duzeni FROM salonlar"
    
    salonAdlari = []
    salonAdlariTuple = cur.execute(QUERY).fetchall()
    for salonAdi in salonAdlariTuple:
        salonAdlari.append(salonAdi[0])

    if onlyNames: #SADECE ADLAR İSE
        return salonAdlari
        
    # SALON BİLGİLERİ
    salonlar = {}
    salonlarTuples = cur.execute(QUERY_2).fetchall()
    salonlarTuples.sort()
    
    for salonAdi, salon in zip(salonAdlari, salonlarTuples):
        salonlar.update({salonAdi: list(salon)})

    return salonlar

def get_classrooms_counts_per_every_grade():
    QUERY_9 = "SELECT * FROM salonlar WHERE derslik_adi LIKE '%9%'"
    QUERY_10 = "SELECT * FROM salonlar WHERE derslik_adi LIKE '%10%'"
    QUERY_11 = "SELECT * FROM salonlar WHERE derslik_adi LIKE '%11%'"
    QUERY_12 = "SELECT * FROM salonlar WHERE derslik_adi LIKE '%12%'"
    QUERY_TOTAL = "SELECT derslik_adi FROM salonlar"
    totalCount = str(len(cur.execute(QUERY_TOTAL).fetchall()))
    count9 = str(len(cur.execute(QUERY_9).fetchall()))
    count10 = str(len(cur.execute(QUERY_10).fetchall()))
    count11 = str(len(cur.execute(QUERY_11).fetchall()))
    count12 = str(len(cur.execute(QUERY_12).fetchall()))
    return [totalCount, count9, count10, count11, count12]

# THESE TWO FUNCTION WORKS TOGETHER
def create_arrangement(kacli: str, ogretmen_yonu: str, oturma_duzeni: str):
    rowCounts = oturma_duzeni.split(",")
    matrix = []
    # KUTUCUKLARI KOY
    for rowCount in rowCounts:
        matrix.append([])
        for _ in range( int(rowCount) ):
            matrix[-1].append({})

    #INDEXLERI YERLESTIR
    deskNo = 1
    if ogretmen_yonu == "Solda":
        for colIndex in range(len(matrix)):
            for rowIndex in range(len(matrix[colIndex])):
                matrix[colIndex][rowIndex].update({deskNo: None})
                deskNo += 1
                if kacli == "2'li":
                    matrix[colIndex][rowIndex].update({deskNo: None})
                    deskNo += 1
                              
    else:
        for colIndex in range(len(matrix) - 1 , -1, -1):
            for rowIndex in range(len(matrix[colIndex])):
                if kacli == "1'li":
                    matrix[colIndex][rowIndex].update({deskNo: None})
                    deskNo += 1
                else:
                    deskNo += 1
                    matrix[colIndex][rowIndex].update({deskNo: None})
                    deskNo -= 1
                    matrix[colIndex][rowIndex].update({deskNo: None})
                    deskNo += 2
                    
    return matrix
    
def get_name_given_classrooms(names: list):
    classrooms = dict()
    for name in names:
        QUERY = f"SELECT * FROM salonlar WHERE derslik_adi = ?"
        result = cur.execute(QUERY, (name,)).fetchall()
        if len(result) >= 1:
            classroom = result[0]

        elif not result:
            return classrooms
        
        derslik_adi, ogretmen_yonu, kacli, oturma_duzeni = [classroom[indx] for indx in range(len(classroom))]
        duzen = create_arrangement(kacli, ogretmen_yonu, oturma_duzeni)
        
        classroom = dict({"derslik_adi": derslik_adi,
                  "ogretmen_yonu": ogretmen_yonu,
                  "kacli": kacli,
                  "oturma_duzeni": duzen,
                  "ogretmen_masasi": None})
        
        classrooms.update({derslik_adi: classroom})

    return classrooms
    
def remove_classroom(classroomName):
    QUERY = "DELETE FROM salonlar WHERE derslik_adi = ?"
    cur.execute(QUERY, (classroomName,))
    db.commit()
    print(get_all_classrooms(onlyNames=True))

################### THE SCHOOL ##############

def update_all_infos(*values):
    QUERY = "DELETE FROM okul_bilgileri WHERE 1=1"
    QUERY_2 = "INSERT INTO okul_bilgileri VALUES(?, ?, ?)"
    cur.execute(QUERY)
    cur.execute(QUERY_2, values)
    db.commit()

def get_all_infos():
    QUERY = "SELECT * FROM okul_bilgileri"
    try:
        bilgiler = cur.execute(QUERY).fetchall()[0]
    except Exception as e:
        bilgiler = ("", "", "")
        
    return bilgiler

def get_table_infos():
    gradeCounts = []
    studentCounts = []
    classroomCounts = []

    grades = get_all_students(withGrades=True)

    total = str(len(grades))
    gradeCounts.append(total)

    gradesList = [gradeName.split("/")[0] for gradeName in grades.keys()]
    gradesSet = set(gradesList)
    for gradeName in gradesSet:
        count = gradesList.count(gradeName)
        gradeCounts.append(str(count))
            
    gradeCounts = ",".join(gradeCounts)

    studentCounts = get_student_counts_per_every_grade()
    studentCounts = ",".join(studentCounts)
    classroomCounts = get_classrooms_counts_per_every_grade()
    classroomCounts = ",".join(classroomCounts)
    
    return [gradeCounts, studentCounts, classroomCounts]

if __name__ == "__main__":
    #cur.execute("INSERT INTO ogrenciler VALUES (2949, 'Yusuf', 'Kiriş', 'Erkek', '10/A')")
    #cur.execute("INSERT INTO ogrenciler VALUES (2950, 'A', 'B', 'C', '10/A')")

    students = cur.execute("SELECT * FROM ogrenciler WHERE sinif = ? ORDER BY sinif, no", ("10/A", )).fetchall()
    print(students)