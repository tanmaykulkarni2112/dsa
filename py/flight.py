class Graph:
    def __init__(self,cities):
        self.numcities=len(cities)
        #dictionary
        self.city_toindex={cities: i for i, cities in enumerate(cities)}
        #graph
        self.graph=[[0]*self.numcities for _ in range(self.numcities)]

    def addedge(self,source,destination,cost):
        #dictionary ops
        source_index=self.city_toindex[source]
        destination_index=self.city_toindex[destination]
        #graph ops
        self.graph[source_index][destination_index]=cost

    def dfs(self,node,visited):
        #list
        visited[node]=True
        for i in range(self.numcities):
            #with graph and list
            if self.graph[node][i] !=0 and not visited[i]:
                self.dfs(i,visited)
    
    def isConnected(self):
        visited =[False]*self.numcities
        self.dfs(0,visited)
        return all(visited)



#main

cities=input("Enter the cities seperated using , ").split(',')
graph=Graph(cities)
while True:
    print("Functions on flight using adjacency matrix")
    print("1.Add the edge between cities")
    print("2. Check if graph is connected")
    print("3. Exit the program")
    choice= input("Enter the choice")
    if choice == '1':
        source=input("Enter the source")
        destination=input("Enter the destination city")
        cost=float(input("Enter the cost"))
        graph.addedge(source,destination,cost)
        print("Flight added successfully")
    elif choice =='2':
        if graph.isConnected():
            print("Graph is connected")
        else:
            print("Graph is not connected")
    elif choice==3:
        print("exitiing the program")
        break
    else:
        print("Invalid choice. Try again")