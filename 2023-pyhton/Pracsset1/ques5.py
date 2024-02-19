students = {
    "s1":{"Name": "Rahul Mahajan", "CGPA": 8.5},
    "s2":{"Name": "Rohit Sharma", "CGPA": 2.5},
    "s3":{"Name": "Rajat Sharma", "CGPA": 3.0},
    "s4":{"Name": "Rahul Sharma", "CGPA": 2.8},
    "s5":{"Name": "Sahil Sharma", "CGPA": 9.1},
    "s6":{"Name": "Sayan Verma", "CGPA": 5.5}
}

def printOnlyinitials(students):
    for student_id, student_info in students.items():
        name = student_info["Name"]
        name = name.split(" ")
        print(name[0][0] + ". " + name[1])

def findHighestCGPA(students):
    highest=0
    highestStudent=students
    for student_id, student_info in students.items():
        cgpa=student_info["CGPA"]
        std=student_id
        if cgpa>highest:
            highest=cgpa
            highestStudentid=std
    return highestStudentid       
            
def cgpaLt(students,limit):
    sids=[]
    for student_id, student_info in students.items():
        cgpa=student_info["CGPA"]
        std=student_id
        if cgpa<limit:
            sids.append(student_id)
            
    return sids        
            
        


def main():
    printOnlyinitials(students)
    print("Student with highest CGPA is: ",students[findHighestCGPA(students)])
    limit=3
    ltlst=cgpaLt(students,limit)
    print(f"Student with CGPA less than {limit}")
    for id in ltlst:
        print(students[id]["Name"])

if __name__ == "__main__":
    main()
