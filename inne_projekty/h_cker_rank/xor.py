A = [0]
for i in range(1, 10**5):
    A.append(A[i-1] ^ i)

res = [0]
for i in range(1, len(A)):
    res.append(res[i-1] ^ A[i])


l, r = 34567, 98450
print(res[l-1] ^ res[r])
    