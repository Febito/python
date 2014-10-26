def summing(start,end):
    sum = 0
    for i in range(start,end+1):
        print("hey i is", i)
        sum = sum + i
    return sum

print(summing(1,3))
