
    
#data = "dabAcCaCBAcCcaDA"
def activate(data):
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
    
    return (len(data))

    
def improve(data):

    removal = []
    curr_min_len = 0
    bad_unit = 65
    
    nums = []
    
    for unit in range(65,91,1):
        print(chr(unit))
        mod_data = ""
        # get mod data
        for i in range(len(data)):
            if ord(data[i]) != unit and ord(data[i]) != unit + 32:
                mod_data += data[i]
        
        len_mod = activate(mod_data)
        print(len_mod)
        nums.append(len_mod)
        
        
     
        
    return min(nums)
    
    

if __name__ == "__main__":
    with open("input.txt","r") as file:
        data = file.read().strip()
    
    #print(activate(data))
    
    print(improve(data))
    
    