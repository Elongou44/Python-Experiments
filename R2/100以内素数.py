for num in range(100):
    is_prime = True
    if(num<2):
        is_prime = False
    for i in range(2,num-1):
        if(num%i==0):
            is_prime=False
    if is_prime:
        print(num,end=" ")

