# Create student.txt, write your name, then read and display.

file = open("student.txt", 'w')
file.write("Tanvi")
file.close()

file = open("student.txt", 'r')
print(file.read())
file.close()
