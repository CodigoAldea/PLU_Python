file_name = "student.txt"
my_name = "Razak"  
with open(file_name, "w") as file:
    file.write(my_name)
with open(file_name, "r") as file:
    result = file.read()
    print(result)