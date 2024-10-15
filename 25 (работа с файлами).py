#1
with open('learning_python.txt', 'w') as file:
    file.write("In Python you can build desktop applications")
    file.write("In Python you can perform data visualization")
    file.write("In Python you can create machine learning models")

with open('learning_python.txt', 'r') as file:
    print(file.read())

with open('learning_python.txt', 'r') as file:
    for line in file:
        print(line.strip())

with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
print([line.strip() for line in lines])

#2
with open('learning_python.txt', 'r') as file:
    for line in file:
        print(line.replace('Python', 'Java').strip())