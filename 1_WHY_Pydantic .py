def insert_patient_data(name: str, age: int):
    # """
    #  Inserts patient data into the database.

    #  Args:
    #      name (str): The name of the patient.
    #      age (int): The age of the patient.
        # print(name)
        # print(age)
        # print('inserted into database')
    
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('age cannot be negative') 
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError('incorrect data type')


def update_patient_data(name: str, age: int):
    
    
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('updated in database')
    else:
        raise TypeError('incorrect data type')    


update_patient_data('John Doe', 30)

insert_patient_data('John Doe', 30)