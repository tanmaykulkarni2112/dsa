class Graph:
    def __init__(self, cities):
        self.num_cities = len(cities)
        self.city_to_index = {city: i for i, city in enumerate(cities)}
        self.graph = [[0] * self.num_cities for _ in range(self.num_cities)]
    
    def add_edge(self, source, destination, cost):
        source_index = self.city_to_index[source]
        destination_index = self.city_to_index[destination]
        self.graph[source_index][destination_index] = cost
    
    def is_connected(self):
        visited = [False] * self.num_cities
        self.dfs(0, visited)
        return all(visited)
    
    def dfs(self, node, visited):
        visited[node] = True
        for i in range(self.num_cities):
            if self.graph[node][i] != 0 and not visited[i]:
                self.dfs(i, visited)

# Main program
cities = input("Enter the names of cities separated by commas: ").split(',')
graph = Graph(cities)
while True:
    print("\nFlight Paths Management System")
    print("1. Add Flight Path")
    print("2. Check if Graph is Connected")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        source = input("Enter Source City: ")
        destination = input("Enter Destination City: ")
        cost = float(input("Enter Cost/Time/Fuel Used: "))
        graph.add_edge(source, destination, cost)
        print("Flight Path added successfully.")
    elif choice == '2':
        if graph.is_connected():
            print("The graph is connected.")
        else:
            print("The graph is not connected.")
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
