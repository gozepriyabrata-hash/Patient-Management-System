from pydantic import BaseModel
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int
    allergies: list[str]
    address: Address
    contact_details: dict[str, str]

address_dict = {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345"
}

address1 = Address(**address_dict)

patient_dict = {
    "name": "John Doe",
    "age": 30,
    "allergies": ["peanuts", "shellfish"],
    "address": address_dict,
    "contact_details": {"phone": "123-456-7890", "email": "abc@gamil.com"}
}

patient1 = Patient(**patient_dict)

print(patient1.name)
print(patient1.age)
print(patient1.allergies)
print(patient1.address.street)
