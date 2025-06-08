def calculating_minimum_weight(N, M, steps):
    temp_steps = [[0 for _ in range(M)] for _ in range(N)]
    
    temp_steps[0][0] = steps[0][0]
    for i in range(1, N):
        temp_steps[i][0] = steps[i][0] + temp_steps[i-1][0]
    for j in range(1, M):
        temp_steps[0][j] = steps[0][j] + temp_steps[0][j-1]
    
    for i in range(1, N):
        for j in range(1, M):
            temp_steps[i][j] = min(temp_steps[i][j-1], temp_steps[i-1][j]) + steps[i][j]
    
    return temp_steps[N-1][M-1]

def main():
    N = 0
    M = 0
    steps = []
    
    with open("input.txt", "r") as input_file:
        N, M = map(int, input_file.readline().split())
        steps = []
        for _ in range(N):
            row = list(map(int, input_file.readline().split()))
            steps.append(row)
    
    print(calculating_minimum_weight(N, M, steps))

if __name__ == "__main__":
    main()