
def prob1():
    total = 0
    with open('input.txt','r') as file:
        for line in file:
            if (line[0] == "+"):
                total += int(line[1:])
            elif (line[0] == "-"):
                total -= int(line[1:])
                
    print(total)
    
    
def prob2():
    total = 0
    freqs = []
    count = 0
    while True:
        with open('input.txt','r') as file:    
            for line in file:
                
                if (line[0] == "+"):
                    total += int(line[1:])
                elif (line[0] == "-"):
                    total -= int(line[1:])
            
                if (int(total) in freqs):
                    return total
                else:
                    freqs.append(int(total))
                    #print(total)
        count += 1

print(prob2())

