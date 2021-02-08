input()
numbers = list(map(int, input().split()))
mean = sum(numbers)/len(numbers)
numbers.sort()
if len(numbers)%2==0:
 median = sum(numbers[int((len(numbers)/2)-1):int(len(numbers)/2+1)])/2
else:
 median = numbers[len(numbers)/2]
L1=[]
i = 0
while i < len(numbers) : 
    L1.append(numbers.count(numbers[i])) 
    i += 1
d1 = dict(zip(numbers, L1)) 
mode={k for (k,v) in d1.items() if v == max(L1) } 
print(mean)
print(median)
print(min(mode))
