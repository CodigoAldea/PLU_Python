


f = open("Student.txt", "w")
f.write("Yash Deore")
f.close

f = open("Student.txt", "r")
data = f.read()
print(data)
f.close()