data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print("Angka yang di cari: ", end="")
target = int(input())

n = len(data)
for i in range(n):
    for j in range(0, n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("BubbleSort: ", data)
low = 0
high = len(data) - 1
awns = -1
while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
        awns = mid
        break
    elif data[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
print(awns)