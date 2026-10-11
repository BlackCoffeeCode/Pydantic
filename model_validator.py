
from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # Model-level validation
    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if (
            self.age > 60
            and "emergency" not in self.contact_details
        ):
            raise ValueError(
                "Patients older than 60 must have an emergency contact"
            )

        return self


def update_patient_data(patient: Patient):
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Updated patient data")


# Patient information
patient_info = {
    "name": "Nitish",
    "email": "nitish@hdfc.com",
    "age": 65,
    "weight": 70.5,
    "married": True,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "phone": "9876543210",
        "emergency": "9876501234"
    }
}


# Create and validate the Patient object
patient1 = Patient(**patient_info)

# Update patient data
update_patient_data(patient1)
