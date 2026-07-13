# 10. School Annual Report
# A school has recorded the marks of 50 students.
# Write a program that:
# Sorts the marks in ascending order.
# Accepts a mark from the user.
# Checks whether that mark exists in the sorted list.
# Displays the position if found; otherwise, prints "Mark Not Found."


class SchoolReport:
    def __init__(self):
        self.marks = [78, 45, 90, 65, 82, 50, 70, 95, 60, 88]

    def bubble_sort(self):
        n = len(self.marks)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.marks[j] > self.marks[j + 1]:
                    self.marks[j], self.marks[j + 1] = self.marks[j + 1], self.marks[j]

    def binary_search(self, key):
        low = 0
        high = len(self.marks) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.marks[mid] == key:
                print("Mark Found at position:", mid)
                return

            elif self.marks[mid] < key:
                low = mid + 1

            else:
                high = mid - 1

        print("Mark Not Found")

    def display(self):
        print("Marks in Ascending Order:")
        print(self.marks)


obj = SchoolReport()

obj.bubble_sort()
obj.display()

mark = int(input("Enter the mark to search: "))
obj.binary_search(mark)
