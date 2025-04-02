from collections import defaultdict, deque

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        graph = defaultdict(list)

        for i in range(len(edges)):
            [u, v] = edges[i]

            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        q = deque([start_node])
        probabilities = [0] * n
        probabilities[start_node] = 1

        while q:
            currentNode = q.popleft()
            currProb = probabilities[currentNode]

            for nextNode, nextProb in graph[currentNode]:
                newProb = currProb * nextProb
                if newProb > probabilities[nextNode]:
                    probabilities[nextNode] = newProb
                    q.append(nextNode)
        
        return probabilities[end_node]