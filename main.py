from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Student (BaseModel):
    id : int
    name : str
    grade : int


Students = [
    Student(id= 1, name= "zakaria", grade=6),
    Student(id= 2, name= "soulayman", grade=3)
]

@app.get("/profs")
def read_profs():
    return Prof

@app.get("/students")
def read_students():
    return Students

@app.post("/students")
def create_student(new_student : Student ):
    Students.append(new_student)
    return(new_student)

@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(Students):
        if student.id == student_id:
            Students[index] = update_student
            return update_student
    return {"message": "not found"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(Students):
        if student.id == student_id:
            del Students[index]
            return {"message": "student deleted"}
        else:
            return {"message": "student not found"}
