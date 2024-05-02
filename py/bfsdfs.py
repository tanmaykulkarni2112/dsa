class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {node: [] for node in nodes}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start):
        visited = set()
        stack = [start]
        visited.add(start)
        while stack:
            node = stack.pop()
            print(node, end=' ')
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

def print_graph(graph):
    print("Graph:")
    for node, neighbors in graph.adj_list.items():
        print(f"{node}: {neighbors}")

def main():
    # Creating the graph
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    graph = Graph(nodes)
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')

    print_graph(graph)

    while True:
        print("\nMenu:")
        print("1. Perform DFS")
        print("2. Perform BFS")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_node = input("Enter the starting node for DFS traversal: ")
            if start_node in graph.nodes:
                print("DFS:")
                graph.dfs(start_node)
            else:
                print("Invalid node. Please enter a valid node.")
        elif choice == '2':
            start_node = input("Enter the starting node for BFS traversal: ")
            if start_node in graph.nodes:
                print("BFS:")
                graph.bfs(start_node)
            else:
                print("Invalid node. Please enter a valid node.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
