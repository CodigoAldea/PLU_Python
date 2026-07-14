roll_list = [105, 102, 110, 108, 101, 107]
target = int(input("enter roll number search: "))
found = False
for i in range(len(roll_list)):
    if roll_list[i] == target:
        print(f"student found at position {i+1}")
        found = True
        break
    if not found:
        print("student not found roll no")
        