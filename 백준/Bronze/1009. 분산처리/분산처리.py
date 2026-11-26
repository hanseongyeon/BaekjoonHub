T = int(input())
for testcase in range(1, T+1):
    a, b = map(int, input().split())
    if b%4 == 0:
        data_cnt = a**4
    else:
        data_cnt = a**(b%4)

    if data_cnt % 10 == 0:
        ans = 10
    else:
        ans = data_cnt%10
    print(ans)