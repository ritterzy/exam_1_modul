def min_steps(num):
    step = 0
    while True:
        if num ==0:
            return step
        elif num % 2 ==0:
            num /2
            step +=1
        else: 
            num -1
            step+=1
print(min_steps(310))




