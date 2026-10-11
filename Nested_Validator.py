
from pydantic import BaseModel


# Nested model for address details
class Address(BaseModel):
    city: str
    state: str
    pin: str


# Main Patient model
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address


# Address data
address_dict = {
    "city": "gurgaon",
    "state": "haryana",
    "pin": "122001"
}

# Create an Address object
address1 = Address(**address_dict)


# Patient data containing the nested Address object
patient_dict = {
    "name": "nitish",
    "gender": "male",
    "age": 35,
    "address": address1
}

# Create a Patient object
patient1 = Patient(**patient_dict)


# Display patient details
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)
