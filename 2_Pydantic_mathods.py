from pydantic import BaseModel, EmailStr,AnyUrl,Field , field_validator , model_validator , computed_field
from typing import List, Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated [str , Field(..., min_length=1, max_length=100, description="Name of the patient")]
    email: EmailStr = Field(..., description="Email address of the patient")
    linkedIn: AnyUrl = Field(..., description="LinkedIn profile URL of the patient")
    age: int = Field(..., ge=0, description="Age of the patient")
    weight: float = Field(..., gt=0,strict=True, description="Weight must be greater than zero")
    height: float = Field(..., gt=0, description="Height must be greater than zero")
    married: Annotated[bool, Field(default=False,description='Is the patient married or not')]
    allergies: Optional[List[str]] = None
    contact_details: dict[str, str] 


    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
        domain = value.split('@')[-1]
        if domain not in valid_domains:
            raise ValueError(f'Email domain must be one of {valid_domains}')
        return value
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, value):
        if not all(part.isalpha() for part in value.split()):
            raise ValueError('Name must contain only alphabetic characters and spaces')
        return value
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if value < 0:
            raise ValueError('Age must be a positive integer')
        return value
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls):
        if model.age>60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Emergency contact is required for patients over 60 years old')
        return model
    
    @computed_field
    @property
    def calculate_bmi (self) -> float:
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return round(bmi, 2)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.calculate_bmi)
    print('updated in database')

patient_info = Patient(
    name='John Doe',
    email='john.doe@gmail.com',
    linkedIn='https://www.linkedin.com/in/johndoe',
    age=30,
    weight=70.5,
    height=175.0,
    married=True,
    allergies=['peanuts'],
    contact_details={'phone': '123-456-7890', 'emergency_contact': '1234567890'}
)

patient1 = patient_info

insert_patient_data(patient1)
update_patient_data(patient1)