file = open("student.txt", "w")
file.write("Rahul")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()