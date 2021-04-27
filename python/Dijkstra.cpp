//
//  Dijkstra.cpp
//  201409
//
//  Created by Walker on 2019/9/12.
//  Copyright © 2019 WM. All rights reserved.
//

#include "bits/stdc++.h"

using namespace std;

#define INF 0x7fffffff

const int maxn = 1000;
int edges[maxn][maxn]; // 无向图
int N; // 记录顶点数
int M; // 记录边的数量

int path[maxn]; // 记录结点路径上的前一个结点
int dist[maxn]; // 记录源点到各个其他点的距离
int s[maxn]; // 记录是否达到最短

// 不允许出现负权重的边
void dijkstra(int n) { // n 是源点的序号
    // 初始化
    memset(s, 0, sizeof(s));
    for (int i = 0; i < N; i++) {
        dist[i] = edges[n][i];
        if (edges[n][i] < INF)
            path[i] = n;
        else
            path[i] = -1;
    }
    dist[n] = 0;
    s[n] = 1;
    // 进行遍历
    for (int i = 0; i < N; i++) {
        // 找到距离source point n最近的一个顶点
        int u = n, dis = INF;
        for (int j = 0; j < N; j++) {
            if (s[j] == 0 && dist[j] < dis) {
                dis = dist[j];
                u = j;
            }
        }
        s[u] = 1;
        // 判断经过u是否会有更短路径出现
        for (int k = 0; k < N; k++) {
            if (!s[k]) {
                if (edges[u][k] != INF && dist[k] > dist[u]+edges[u][k]) {
                    dist[k] = dist[u]+edges[u][k];
                    path[k] = u;
                }
            }
        }
    }
}


void shortestPath(int src) {
    for (int i = 0; i < N; i++) {
        if (i == src) {
            dist[i] = 0;
            path[i] = -1;
        } else
            dist[i] = INF;
    }
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    pq.push(make_pair(0, src));
    while (!pq.empty()) {
        pair<int, int> p = pq.top();
        pq.pop();
        int weight = p.first, u = p.second;
        if (s[u]) continue;
        s[u] = 1;
        for (int i = 0; i < N; i++) {
            if (!s[i])
                if (edges[u][i] != INF && weight+edges[u][i] < dist[i]) {
                    dist[i] = dist[u]+edges[u][i];
                    pq.push(make_pair(dist[i], i));
                    path[i] = u;
                }
        }
    }
}
int main() {
    cin >> N >> M;
    int a, b, e;
    for (int i = 0; i < maxn; i++) {
        for (int j = 0; j < maxn; j++) {
            edges[i][j] = INF;
        }
    }
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> e;
        edges[a][b] = e;
        edges[b][a] = e;
    }
    int source;
    cin >> source;
//    dijkstra(source);
    shortestPath(source);
    cout << "Source point " << source << " to other points' minimum distance" << endl;
    for (int i = 0; i< N; i++) {
        cout << "Point " << i << ", d = " << dist[i] << ", pre: "<< path[i] << endl;
    }
    return 0;
}
