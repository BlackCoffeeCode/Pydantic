
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Computed field: calculate BMI automatically
    @computed_field
    @property
    def bmi(self) -> float:
        bmi_value = round(self.weight / (self.height ** 2), 2)
        return bmi_value


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("BMI:", patient.bmi)
    print("Updated")


# Patient information
patient_info = {
    "name": "nitish",
    "email": "abc@icici.com",
    "age": "65",
    "weight": 75.2,
    "height": 1.72,
    "married": True,
    "allergies": ["pollen", "dust"],
    "contact_details": {
        "phone": "2353462",
        "emergency": "235236"
    }
}


# Create and validate the Patient object
patient1 = Patient(**patient_info)

# Display patient information and computed BMI
update_patient_data(patient1)

# Print all model data, including the computed field
print("\nComplete patient data:")
print(patient1.model_dump())
