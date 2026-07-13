'''9. Library Book Search
A library has 10,000 books, and the Book IDs are already arranged in
ascending order.
Write a program to find a given Book ID efficiently.
Also mention which searching algorithm you used and why it is suitable.
'''

book_ids = list(map(int, input("Enter sorted Book IDs: ").split()))
key = int(input("Enter Book ID to search: "))

low = 0
high = len(book_ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if book_ids[mid] == key:
        print("Book ID found at position:", mid)
        found = True
        break
    elif book_ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Book ID not found")