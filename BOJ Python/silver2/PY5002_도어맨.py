N = int(input())
arr = list(map(str, input().rstrip()))
m_cnt, w_cnt = 0, 0
ans = 0
for i in range(len(arr)):
    if abs(m_cnt - w_cnt) < N:
        if arr[i] == 'M': m_cnt += 1
        else: w_cnt += 1
        ans += 1
    else:
        if arr[i] == 'M':
            if abs(m_cnt + 1 - w_cnt) < N:
                m_cnt += 1
                ans += 1
            else:
                if i + 1 < len(arr) and arr[i + 1] == 'W':
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    w_cnt += 1
                    ans += 1
                else: break
        else:
            if abs(w_cnt + 1 - m_cnt) < N:
                w_cnt += 1
                ans += 1
            else:
                if i + 1 < len(arr) and arr[i + 1] == 'M':
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    m_cnt += 1
                    ans += 1
                else: break
print(ans)