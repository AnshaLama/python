print("Prime numbers: ")
for i in range(1, 21): 
    count = 0 
    for j in range(1 , 21): 
        if ( i % j == 0):
            count = count + 1
    if count == 2:
         print(i)

    