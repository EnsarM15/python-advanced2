person ={
    "name": "John Doe",
    "age": 30,
    "adress":{
         
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345"
    
    },
    "contacts": [
        {
            "type": "email",
            "value": "john.doe@example.com"
        },
        {
            "type": "phone",
            "value": "555-1234"
        },
        
    ]
}

print(person["name"]) 
print(person["age"]) 
print(person["adress"]["city"]) 
print(person["contacts"][1]["value"]) 