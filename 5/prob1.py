with open("input.txt","r") as file:
    data = file.read().strip()
    
#data = "dabAcCaCBAcCcaDA"
done = False
ind_to_remove = []
i = 0
while not done:
    while i < len(data)-1:
        if ord(data[i]) == ord(data[i+1])+32 or ord(data[i])+32 == ord(data[i+1]):
            ind_to_remove += [i,i+1]
            i += 2
        else:
            i += 1
    
    if ind_to_remove == []:
        done = True
    else:
        temp = ""
        for j in range(0,len(data)):
            if not (j in ind_to_remove):
                temp += data[j]
    
        data = temp
        ind_to_remove = []
        i = 0

print(len(data))
