def dfs_iterative(graph, start):
    visited = set()  # 방문한 노드를 저장할 집합
    stack = [start]  # 시작 노드를 스택에 추가

    while stack:
        vertex = stack.pop()  # 스택에서 노드 하나를 꺼냄
        if vertex not in visited:
            visited.add(vertex)  # 방문 처리
            print(vertex)  # 방문한 노드 출력
            # 인접 노드를 스택에 추가 (역순으로 추가하여 원래 순서를 유지)
            stack.extend(reversed(graph[vertex]))

# 그래프 정의 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_iterative(graph, 'A')