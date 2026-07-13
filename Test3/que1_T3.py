student_roll =[22, 33, 44, 55, 66]
roll_num =int(input("Enter the roll number: "))
if roll_num in student_roll:
    position=student_roll.index(roll_num)
    print(f"student found: {position}")
else:
    print("stduent not found")