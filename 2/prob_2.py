def prob1():
    two = 0
    three = 0
    with open("input.txt","r") as file:
    
        for line in file:
            
            counts = {}
            stop2 = False
            stop3 = False
            
            for letter in line:
                
                if not(letter in counts.keys()):
                    counts[letter] = 1
                else:
                    counts[letter] += 1
                    
            for k,v in counts.items():
                
                if v == 2 and not stop2:
                    two += 1
                    stop2 = True
                if v == 3 and not stop3:
                    three += 1
                    stop3 = True
                
        
    return (two*three)
    
def prob2():
    
    ids = []
    with open("input.txt","r") as file:
        for line in file:
            ids.append(line)
            
    for i in range(len(ids)):
        for j in range(1,len(ids)):
            dif = 0
            for k in range(len(ids[i])):
                if ids[i][k] != ids[j][k]:
                    dif += 1
                if dif > 1:
                    break
                    
            if dif == 1:
                for m in range(len(ids[i])):
                    if ids[i][m] != ids[j][m]:
                        return ids[i],ids[j]
                        return ids[i][0:m] + ids[i][m+1:]
                

            
            
print(prob2())