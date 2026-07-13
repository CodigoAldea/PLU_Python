# 9. Library Book Search
# A library has 10,000 books, and the Book IDs are already arranged in
# ascending order.
# Write a program to find a given Book ID efficiently.
# Also mention which searching algorithm you used and why it is suitable.

n = int(input("Enter number of Book IDs: "))
book = []
for i in range(n):
    book.append(int(input("Enter Book ID: ")))
find = int(input("Enter Book ID to Search: "))
low = 0
high = n - 1
while low <= high:

    mid = (low + high) // 2

    if book[mid] == find:
        print("Book Found at Index:", mid)
        break

    elif find < book[mid]:
        high = mid - 1

    else:
        low = mid + 1

else:
    print("Book Not Found")

print("Algorithm Used: Binary Search")
print("Reason: List is already sorted.")