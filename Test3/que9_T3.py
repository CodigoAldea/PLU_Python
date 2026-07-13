class Library:
    def __init__(self):
        self.book_ids = [101, 105, 110, 115, 120, 125, 130, 135, 140, 145]

    def search_book(self, key):
        low = 0
        high = len(self.book_ids) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.book_ids[mid] == key:
                print("Book Found at index:", mid)
                return

            elif self.book_ids[mid] < key:
                low = mid + 1

            else:
                high = mid - 1

        print("Book Not Found")


obj = Library()

book_id = int(input("Enter Book ID to search: "))
obj.search_book(book_id)