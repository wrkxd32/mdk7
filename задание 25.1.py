import json

#1
with open('data.json', 'w') as f:
    json.dump({"name": "Alice", "age": 30, "city": "New York"}, f)

with open('e.json') as f:
    e = json.load(f)
    print(e['name'], e['city'])

#2
infoo = {'users': {'username': 'user1', 'email': 'user1@example.com'}}
with open('book.json', 'w') as f:
    json.dump(infoo, f)

#3
with open('user_e.json', 'w') as f:
    us = [{'name': 'Existing User', 'age': 25}]
    us.append({'name': 'New User', 'age': 30})
    json.dump(users, f)

#4
with open('products.json', 'w') as f:
    json.dump([
        {"name": "laptop", "price": 1000},
        {"name": "mouse", "price": 50},
        {"name": "keyboard", "price": 100}
    ], f)

with open('products.json') as f:
    pr = json.load(f)
    for product in pr:
        if product['price'] > 100:
            print(product['name'])

#5
with open('school.json', 'w') as f:
    json.dump({
        "classes": {
            "Class_1": {
                "Students": ["Alice", "Bob"],
                "Teacher": "Mr. Smith"
            },
            "Class_2": {
                "Students": ["Charlie", "David"],
                "Teacher": "Mrs. Johnson"
            }
        }
    }, f)

with open('school.json') as f:
    sch = json.load(f)
    stdnt = max(sch['classes'].items(), key=lambda x: len(x[1]['Students']))
    print(stdnt[0], len(stdnt[1]['Students']))