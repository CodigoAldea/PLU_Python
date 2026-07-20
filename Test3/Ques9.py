# 9. Library Book Search
# A library has 10,000 books, and the Book IDs are already arranged in
# ascending order.
# Write a program to find a given Book ID efficiently.
# Also mention which searching algorithm you used and why it is suitable.


books = [101,105,110,120,130,145,160,180,200]
book = int(input("Enter Book ID: "))

low = 0

high = len(books)-1

found = False

while low <= high:

    mid = (low+high)//2

    if books[mid] == book:

        print("Book Found at Index:", mid)

        found = True

        break

    elif book < books[mid]:

        high = mid-1

    else:

        low = mid+1

if not found:

    print("Book Not Found")

print("Algorithm Used : Binary Search")
print("Reason : List is already sorted.")