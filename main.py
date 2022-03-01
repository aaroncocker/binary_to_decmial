total = 0
value = 128

binary = str(input("Input a binary number: "))
split = list(binary)

if len(binary) == 8:
    try:
        for i in range(0, len(split)):
            split[i] = int(split[i])
    
        for i in range(0,7):
            if split[i] == 1:
                total = total + value
                i = i + 1
                value = value / 2

        print(binary + " is equal to", total)
    
    except:
        print("Binary number must equal 8 characters!")
