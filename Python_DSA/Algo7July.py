#1st code:
#list [2,100,9,105,10,20,15,36,55,42] ,find 20 is present or not in the list using linear search.

# list1 = [2,100,9,105,10,20,15,36,55,42]
# found = False
# for i in list1:
#     if i == 20:
#         found = True
#         break
# if found:
#     print("20 is present in the list.")
# else:
#     print("20 is not present in the list.")
    

#2nd code:
#Apply binary search to find 20 is present or not in the list. Apply function also.

# def search(var, element):
#     #step 1: sorted structue ?
#     sorted_var = var.sort()
    
#     #step 2: find the mid value:
#     mid_index = len(sorted_var) // 2
    
#     #step 3: check the condition:
#     if sorted_var[mid_index] < element:
#         #this is to check for the right structure
#         search(sorted_var[:mid_index+1], element)
        
#     elif sorted_var[mid_index] > element:
#         #elif 
#         search(sorted_var[mid_index+1:], element)
    
#     else:        
#         print(f"{element} found in the index {mid_index}.")

#3rd code:
#add the numbers and print like 1+1+1 = 3, 5+0+1 = 6, etc. and the output in sorted list.
# var = [111, 501, 100, 515, 424, 899, 991, 605, 103, 1104]
# output = []
# for i in var:
#     count = 0
#     for j in str(i):
#         count += int(j)
#         if count > 10:
#             for a in str(count):
#                 count += int(a) 
#     output.append(count)

# output.sort()
# print(output)

num =input("Enter the number to find the sum of digits: ")
num = list(map(int, num.split(",")))
print(num)



#Create same logic using for loop.
# var = [2,100,9,105,10,20,15,36,55,42]
# element = 20
# mid_index = len(var) // 2
# for i in range(len(var)):
#     if var[mid_index] < element:
#         continue
#     if var[mid_index] > element:
#         mid_index += 1
#     else:
#         print(f"{element} found in the index {mid_index}.")
#         break
    

