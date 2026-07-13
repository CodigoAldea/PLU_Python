class Library:
    def __init__(self):
        self.book_ids = [100, 140, 200, 250, 300, 350, 400, 450, 500, 550]

    def search_book(self, key):
        low = 0
        high = len(self.book_ids) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.book_ids[mid] == key:
                print("Book found at index:", mid)
                return
            elif self.book_ids[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        print("Book not found")


lib = Library()
key = int(input("Enter Book ID: "))
lib.search_book(key)