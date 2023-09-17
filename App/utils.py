a = 'Hello'

def greeting(name):
    print("Hello, " + name)

person1 = [
    {
    "name": "John",
    "age": 36,
    "country": "Norway"
    },
    {
    "name": "Jose",
    "age": 37,
    "country": "Norway"
    }
]

def obtener_edad(name):
    for i in person1:
        if i['name'] == name:
            return i['age']
    return None
