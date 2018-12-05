with open("input.txt","r") as file:
    data = file.read().strip()

#data = "dabAcCaCBAcCcaDA"
done = False
ind_to_remove = []
#while not done:
#    i = 0
#    print("OUT")
i = 0
last_jump = 0
while i < len(data)-1:

    if ord(data[i]) == ord(data[i+1])+32 or ord(data[i])+32 == ord(data[i+1]):
        ind_to_remove += [i,i+1]
        temp = ""
        
        
        for j in range(0,len(data)):
            if not (j in ind_to_remove):
                temp += data[j]
        
        data = temp
        ind_to_remove = []
        
        i = last_jump
        last_jump = i
    else:
        i += 1
        
i = 0
last_jump = 0

    #print(i)
        
    #if ind_to_remove == []:
    #    done = True
    #else:
    #    temp = ""
    #    for j in range(0,len(data)):
    #        if not (j in ind_to_remove):
    #            temp += data[j]
    #  
    #    data = temp
    #    ind_to_remove = []

print(data)
print(len(data))
