L = [1, 1]
n = 5
i = 2
R = L.copy()
print('i:', i, 'L:', L, 'k:', '-', 'R:', R, 'n:', n)
while i < n:
    k = L[i-1] + L[i-2]
    L.append(k)
    if k % 2 == 1:
        R.append(k)
    print('i:', i, 'L:', L, 'k:', k, 'R:', R, 'n:', n)
    i = i + 1   
#print(len(R))
