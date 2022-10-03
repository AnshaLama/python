#Making a list from one to one million
num =  list(range(1 , 1000001))
print(min(num))
print(max(num))

#Summing everything 
sum = 0 
for i in num:
    sum = sum + i
print(f"SUM: {sum}")  #To see how quickly Python can add a million numbers. 







