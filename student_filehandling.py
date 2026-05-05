#1.student_marks.csv contains the marks an other details fro some students.WAP
#1 OPEN A FILE IN READ MODE
#2create a dictinory from the given data
#3 add a new field to dictinory total_marks and store the total marks of the students
#4 add a new field to dictinory average and store the average marks of the students
#5 create a new file and write this information to the new file(http://www.kaggle.com/arunkumar413/studentmarks)

# file=open("student_marks.csv","r") 

import csv

student_dict = {}
#Q21 AND Q2
with open("student_marks.csv","r") as file:
  
     
    reader = csv.DictReader(file)

    for row in reader:
         
        student_dict[row["name"]] = {
            "roll_no": row["roll_no"],
            "math": int(row["math"]),
            "science":int(row["science"]),
            "english": int(row["english"])
            
        }
        #Q3
for student in student_dict:
     math=student_dict[student]["math"]
     science=student_dict[student]["science"]
     english=student_dict[student]["english"]
     total=math+science+english
     student_dict[student]["total_marks"]=total
#Q4
for student in student_dict:
    math=student_dict[student]["math"]
    science=student_dict[student]["science"]
    english=student_dict[student]["english"]

    avg=(math+science+english)/3
    student_dict[student]["average_marks"]=avg


print(student_dict)

with open("updated_student_marks.csv", "w", newline="") as file:
    fieldnames = [
        "name",
        "roll_no",
        "math",
        "science",
        "english",
        "total_marks",
        "average_marks"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for student, details in student_dict.items():
        row = {"name": student}
        row.update(details)
        writer.writerow(row)