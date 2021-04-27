# 利用优先级队列可以加速迪杰斯特拉算法
import queue
INF = 10**9 + 7

# 图是邻接矩阵表示，org 表示源点的序号
def dijkstra_PriorityQueue(graph, org):
    n = len(graph)
    lsd = queue.PriorityQueue()
    lsd.put((0, org))

    ret = [INF] * n
    ret[org] = 0

    vis = [False] * n
    path = [-1] * n
    path[org] = org
    while not lsd.empty():
        l, v = lsd.get()
        if vis[v]: 
            continue

        vis[v] = True
        # print("Get least:", v, "Dis:", l)
        for i in range(n):
            dis = l + graph[v][i]
            # print(i, vis[i], dis, graph[org][i])
            if not vis[i] and dis < ret[i]:
                # print(i, dis)
                ret[i] = dis
                path[i] = v
                lsd.put((dis, i))

    return ret, path
                

    


if __name__ == '__main__':
    n = 5
    graph = [[0, 3, 2, INF, INF, INF], [3, 0, 1, INF, INF, INF], [2, 1, 0, 1, INF, INF], [INF, INF, 1, 0, 10, 3], [INF, INF, INF, 10, 0, 4], [INF, 4, INF, 3, 4, 0]]
    d, path = dijkstra_PriorityQueue(graph, n)
    print(d)
    for i, p in enumerate(path):
        s = str(i) + "<-"
        while p != n:
            s += str(p) + "<-"
            p = path[p]
        s += str(p)
        print(s)

