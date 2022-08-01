class Solution:
    def dfs(self, curNode: int, adjList: Dict[int, List[int]], visited: Set[int]) -> None:
        if curNode in visited:
            return

        visited.add(curNode)
        
        for neighbor in adjList[curNode]:
            self.dfs(neighbor, adjList, visited)
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adjList = dict()
        
        for i in range(n):
            adjList[i] = []
        
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        visited = set()
        self.dfs(0, adjList, visited)
        
        return len(visited) == n