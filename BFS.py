from collections import deque

def bfs(graph, start):
    # 큐 초기화
    queue = deque([start])
    visited = set([start])  # 방문한 노드 집합

    while queue:
        # 큐에서 노드 꺼내기
        vertex = queue.popleft()
        print(vertex, end=' ')  # 현재 노드 출력

        # 인접 노드 탐색
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)  # 방문 표시
                queue.append(neighbor)  # 큐에 추가

# 그래프 예시 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS 실행
bfs(graph, 'A')