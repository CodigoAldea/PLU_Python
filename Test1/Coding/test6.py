file = open("student.txt", "w")
file.write("faisal dexmo")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()