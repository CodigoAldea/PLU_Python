# question 7
file = open("student.txt", "w")
file.write("Name: Palak Sharma")
file.close()

file = open("student.txt", "r")
print(file.read())
file.close()