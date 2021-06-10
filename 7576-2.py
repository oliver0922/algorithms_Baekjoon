import sys
from collections import deque

input = sys.stdin.readline

def BFS():
    day = 0
    
    #큐에 탐색해야 하는 노드 없을 때까지 실행
    while queue:
    
        day += 1 #일수 증가
        
        #큐에 있는 노드 수만큼 탐색
        for _ in range(len(queue)):
        
            x, y = queue.popleft() #큐에 있는(탐색해야 하는) 노드의 좌표
            
            for i in range(4):
                pointX = x + dx[i] #상하좌우
                pointY = y + dy[i] #상하좌우

                #인덱스 벗어나지 않는 경우
                if -1 < pointX < N and -1 < pointY < M:
                
                    #아직 방문하지 않은 경우 (익지 않은 토마토)
                    if paint[pointX][pointY] == 0:
                        paint[pointX][pointY] = 1 #익음 (방문처리)
                        queue.append([pointX, pointY]) #큐에 삽입

    #익지 않은 토마토 남아있는 경우 -1 반환
    for i in range(len(paint)):
        for j in range(len(paint[i])):
            if paint[i][j] == 0:
                return -1

    #모두 익은 경우 일수 출력
    return day - 1

M, N = map(int, input().split())

paint = [list(map(int, input().split())) for _ in range(N)]

queue = deque([])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(len(paint)):
    for j in range(len(paint[i])):
        if paint[i][j] == 1:
            queue.append([i, j])

print(BFS())