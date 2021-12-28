#백준 단계별 문제 8958번
N = int(input())
score = 0
total_score = 0
for i in range(N):
    result = list(input())
    for quiz in result:
        if quiz == "O":
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)
    total_score = 0
    score = 0
