'''An airline wants to manage routes between cities.
  Requirements:
	create a graph where each city is connected to its direct flight destination.
	Display all available routes.
	Store all city names in a list.
	sort the city names alphabetically using Insertion sort.
	Ask the user to search for a city using Binary search.
	if found, display all cities directly connected to it.	
	Otherwise, display "city not found".'''
 
 
class AirlineGraph:
    def __init__(self):
        self.graph = {}

    def add_route(self, origin, destination):
        if origin not in self.graph:
            self.graph[origin] = []
        self.graph[origin].append(destination)
        
        if destination not in self.graph:
            self.graph[destination] = []

    def display_routes(self):
        print("\n--- Available Flight Routes ---")
        for city, destinations in self.graph.items():
            if destinations:
                for dest in destinations:
                    print(f"{city} -> {dest}")
            else:
                print(f"{city} (No outgoing flights)")

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def find_connected_cities(self, city):
        if city in self.graph and self.graph[city]:
            print(f"\nCities directly connected from {city}: {', '.join(self.graph[city])}")
        else:
            print(f"\nNo direct flights departing from {city}.")

# --- Main Program Execution ---
airline = AirlineGraph()

# Add direct flight destinations
airline.add_route("Delhi", "Mumbai")
airline.add_route("Amritsar", "Patna",)
airline.add_route("Patna", "Lucknow")
airline.add_route("Bangalore", "Hyderabad",)
airline.add_route("Goa", "Bhuneshwar")

# 1. Display all available routes
airline.display_routes()

# 2. Store all city names in a list
cities = list(airline.graph.keys())

# 3. Sort the city names alphabetically using Insertion sort
sorted_cities = airline.insertion_sort(cities)
print("\nSorted City Names:", sorted_cities)

# 4. Ask the user to search for a city using Binary search
search_city = input("\nEnter a city to search for direct flights: ").strip()

# 5. Search & Display results
city_index = airline.binary_search(sorted_cities, search_city)
if city_index != -1:
    airline.find_connected_cities(search_city)
else:
    print("City not found")
