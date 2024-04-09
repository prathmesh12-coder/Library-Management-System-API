from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional



#Create a FastAPI instance 
app = FastAPI()


#Connect to mongo Atlas

client=MongoClient("mongodb+srv://Prathmesh:prathmesh12345@cluster0.2zcanyt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0");
db=client["libray_management"]


# Define a Pydantic model for Student
class Student(BaseModel):
    name: str
    age: int
    address: dict


#Defining pydantic model with optional specifically for patch request
class UpdatedStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[dict] = None


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Library Management System API!"}


# Endpoint to create a new student
@app.post("/api/students", status_code=201)
async def create_student(student: Student):
    # Insert the student data into the database
    result = db.students.insert_one(student.model_dump())
    # Return the ID of the newly created student
    return {"id": str(result.inserted_id)}


@app.get("/api/students", status_code=200)
async def list_students(country: str = None, age: int = None):
    # Define filters based on query parameters
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}
    # Project only name and age fields from the database query
    projection = {"name": 1, "age": 1, "_id": 0}
    # Retrieve students from the database based on filters and projection
    students = list(db.students.find(filters, projection))
    # Return the list of students with only name and age
    return {"data": students}

# Endpoint to fetch a specific student by ID
@app.get("/api/students/{id}", status_code=200)
async def get_student(id: str):
    # Convert id to ObjectId
    obj_id = ObjectId(id)
    # Retrieve the student from the database by ID
    student = db.students.find_one({"_id": obj_id}, {"_id": 0})
    # Return the student details
    return student


@app.patch("/api/students/{id}", status_code=204)
async def update_student(id: str, student: UpdatedStudent):
    # Convert id to ObjectId
    obj_id = ObjectId(id)
    # Create a dictionary containing only the set fields from the student model
    update_data = student.model_dump(exclude_unset=True)
    # Update the student data in the database
    db.students.update_one({"_id": obj_id}, {"$set": update_data});
    # Return No Content status
    return update_data


# Endpoint to delete a specific student by ID
@app.delete("/api/students/{id}", status_code=200)
async def delete_student(id: str):
    #convert id to ObjectId
    obj_id=ObjectId(id)
    # Delete the student from the database
    db.students.delete_one({"_id": obj_id})
    # Return a sample response
    return {"message": "Student deleted successfully"}