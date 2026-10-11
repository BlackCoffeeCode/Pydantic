
from pydantic import BaseModel


# Nested model for address details
class Address(BaseModel):
    city: str
    state: str
    pin: str


# Patient model
class Patient(BaseModel):
    name: str
    gender: str = "male"
    age: int
    address: Address


# Address information
address_dict = {
    "city": "gurgaon",
    "state": "haryana",
    "pin": "122001"
}

address1 = Address(**address_dict)


# Patient information
patient_dict = {
    "name": "nitish",
    "age": 35,
    "address": address1
}

# Create Patient object
patient1 = Patient(**patient_dict)


# Serialize the model into a Python dictionary
temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))


# Serialize all fields, including default values
print("\nComplete serialization:")
print(patient1.model_dump())
