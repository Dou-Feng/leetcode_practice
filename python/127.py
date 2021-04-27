from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ## 把问题转化为求图中计算两个结点的最短距离
        node_num = 0
        nodeId = dict()
        def addNode(word):
            if word in nodeId:
                return 
            nonlocal node_num
            nodeId[word] = node_num
            node_num += 1

        edges = collections.defaultdict(list)
        def addEdge(word):
            addNode(word)
            wordL = list(word)
            for i in range(len(wordL)):
                tmp = wordL[i]
                wordL[i] = '*'
                n_word = "".join(wordL)
                addNode(n_word)
                edges[nodeId[word]].append(nodeId[n_word])
                edges[nodeId[n_word]].append(nodeId[word])
                wordL[i] = tmp


        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in nodeId:
            return 0


        beginId, endId = nodeId[beginWord], nodeId[endWord]
        que = collections.deque([beginId])
        dis = [float('inf')] * node_num
        dis[beginId] = 0
        while que:
            x = que.popleft()
            if x == endId:
                print(dis)
                return dis[endId] // 2 + 1

            for node in edges[x]:
                if dis[node] == float('inf'):
                    dis[node] = dis[x] + 1
                    que.append(node)
        print(dis)
        return 0



sol = Solution()
s = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(s)