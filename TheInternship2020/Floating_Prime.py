def floating_prime():
    number = float(input("Enter number : "))
    while number != 0.0:
        if  number > 10.0 or number < 1.0:
            break
        elif (number*100000000000) - int(number*100000000000) > 0:
            break
        multiplier = 10
        value = 'NotPrime'
        while value == 'NotPrime' and multiplier <= 1000:
            for i in range(2,int(number*multiplier)):
                if (int(number*multiplier) % i) == 0:
                    multiplier = multiplier*10
                    value = 'NotPrime'
                    break

            else:
                print("TRUE")
                value = 'Prime'
                    
        if multiplier == 10000:
            print("FALSE")
        number = float(input("Enter number : "))   
floating_prime()