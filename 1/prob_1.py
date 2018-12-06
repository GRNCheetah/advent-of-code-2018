
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
    freqs = set()
    
    while True:
        with open('input.txt','r') as file:    
            for line in file:
                
                total += int(line.strip())
                #if (line[0] == "+"):
                #    total += int(line[1:])
                #elif (line[0] == "-"):
                #    total -= int(line[1:])
            
                if (int(total) in freqs):
                    return total
                else:
                    freqs.add(int(total))
    

print(prob2())

