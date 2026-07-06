file = open("student.txt", "w")
file.write("Shyam")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()