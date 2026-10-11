
from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # 1. Email domain validation
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]

        domain_name = str(value).rsplit("@", 1)[-1].lower()

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")

        return value

    # 2. Transform the patient's name to uppercase
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    # 3. Validate the patient's age after Pydantic parses it
    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if isinstance(value, bool):
            raise ValueError("Age must be an integer between 1 and 99")

        if isinstance(value, str):
            value = value.strip()

            if not value.isdigit():
                raise ValueError(
                    "Age must be an integer between 1 and 99"
                )

            value = int(value)

        if not isinstance(value, int) or not 0 < value < 100:
            raise ValueError(
                "Age should be between 0 and 100"
            )

        return value


def update_patient_data(patient: Patient):
    print(patient.name)
    print("updated")


# Patient information
patient_info = {
    "name": "Piyush",
    "email": "piyush@hdfc.com",
    "age": 30,
    "weight": 70.5,
    "married": False,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "phone": "9876543210",
        "emergency_contact": "9876501234"
    }
}

# Create and validate the Patient object
patient1 = Patient(**patient_info)

# Update patient data
update_patient_data(patient1)
