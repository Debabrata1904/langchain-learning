from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Debu"  # Default value for the name field
    age: Optional[int] = None  # Optional field for age, default is None
    email: EmailStr  # Field for email, must be a valid email address
    cgpa: float = Field(ge=0.0, le=10.0, default=0.0, description="this is student's CGPA")  # Field for CGPA, must be between 0.0 and 10.0


#student = {"name": "Debabrata"}
#new_student = Student(**student)



new_student = Student(
    name="Debabrata Bhowmik",
    age='25',                  # age is provided as a string, but Pydantic will convert it to an integer using type coercion
    email="debabrata@example.com",
    cgpa=8.5
)  

print(new_student.name)
print(new_student.age)
print(new_student.email)
print(new_student.cgpa)