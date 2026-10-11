# Why?
'''1. Type Validation: Pydantic provides robust type validation, ensuring that the data conforms to the expected types. This helps catch errors early in the development process.
2. Data Validation: Pydantic allows you to define validation rules for your data models, such as required fields, default values, and custom validation logic. This ensures that the data being processed is valid and meets the specified criteria.
3. Serialization and Deserialization: Pydantic makes it easy to serialize and deserialize data, allowing you to convert between Python objects and JSON or other formats seamlessly. This is particularly useful when working with APIs that exchange data in JSON format.
4. Automatic Documentation: Pydantic models can be used to automatically generate API documentation, making it easier for developers to understand the expected data structures and endpoints'''




from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import List, Dict, Annotated, Optional


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give the patient's name in less than 50 characters",
            examples=["Nitish", "Amit"]
        )
    ]

    email: EmailStr

    linkedin_url: AnyUrl

    age: int = Field(ge=0, lt=120)

    weight: Annotated[
        float,
        Field(gt=0, strict=True)
    ]

    married: Annotated[
        Optional[bool],
        Field(description="Is the patient married or not?")
    ] = None

    allergies: Annotated[
        Optional[list[str]],
        Field(max_length=5)
    ] = None

    contact_details: dict[str, str]


def insert_patient_data(patient: Patient):
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Inserted patient data successfully.")


def update_patient_data(patient: Patient):
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Updated patient data successfully.")


patient_info = {
    "name": "Piyush",
    "email": "piyush@example.com",
    "linkedin_url": "https://www.linkedin.com/in/piyush-dhakad/",
    "age": 22,
    "weight": 70.5,
    "married": False,
    "allergies": ["Dust"],
    "contact_details": {
        "phone": "9876543210",
        "emergency_contact": "9876501234"
    }
}


# Validate the dictionary and create a Patient object
patient1 = Patient(**patient_info)

# Insert and update patient data
insert_patient_data(patient1)
print("-" * 35)
update_patient_data(patient1)
