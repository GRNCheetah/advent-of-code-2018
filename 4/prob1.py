def prob1():
    lines = []
    with open("input.txt","r") as file:
        for line in file:
            data = {}
            data["year"] = int(line[1:5])
            data["month"] = int(line[6:8])
            data["day"] = int(line[9:11])
            data["hour"] = int(line[12:14])
            data["min"] = int(line[15:17])
            data["data"] = line[19:].strip()
            lines.append(data)
            
    lines = sortTime(lines,0)
    
    
    ASLEEP = "falls asleep"
    AWAKE  = "wakes up"
    GUARD  =  "Guard #"
    
    
    guards = []
    sleep_times = []
    schedules = []
    
    
    for line in lines:
        msg = line["data"]
        curr_min = line["min"]
        
        if msg.startswith(GUARD):
            ind = msg.index(" ", 7)
            curr_guard = int(msg[7:ind])

            if not(curr_guard in guards):
                guards.append(curr_guard)
                sleep_times.append(0)
                schedules.append([0 for x in range(60)])

        if msg == ASLEEP:
            start_min = curr_min
            
        if msg == AWAKE:
            guard_ind = guards.index(curr_guard)

            for i in range(start_min,curr_min,1):
                schedules[guard_ind][i] += 1
        
            sleep_times[guard_ind] += curr_min - start_min


    most_sleep = 0
    target = 0
    sched = []
    for i in range(len(guards)):
        if sleep_times[i] > most_sleep:
            most_sleep = sleep_times[i]
            target = guards[i]
            sched = schedules[i]
    
    
    
    print("Part 1: Guard #: " + str(target) + " | Minute: " + str(sched.index(max(sched))) + " | Ans: " + str(sched.index(max(sched)) * target))
        
    
    curr_max_guard_ind = 0
    max_same = 0
    
    for i in range(len(guards)):
        if max(schedules[i]) > max_same:
            max_same = max(schedules[i])
            curr_max_guard_ind = i
    sched = schedules[curr_max_guard_ind]
    print("Part 2: Guard #: " + str(guards[curr_max_guard_ind]) + " | Minute: " + str(sched.index(max(sched))) + " | Ans: " + str(sched.index(max(sched)) * guards[curr_max_guard_ind]))
    
    
    
    
    
def sortTime(arr,key_num):
    KEYS = ["year","month","day","hour","min"]
    temp = []
    
    if key_num == 0:
        mergeSort(arr,"year")
        temp = sortTime(arr,key_num+1)
        
    elif (key_num < len(KEYS)):
        sec = []
        key = KEYS[key_num-1]
        sort_key = KEYS[key_num]
        
        curr_time = arr[0][key]
        
        for line in arr:
            if line[key] == curr_time:
                sec.append(line)
            else:
                 
                #if sort_key == "hour":
                #    sec = hourSort(sec) 
                #else:
                mergeSort(sec,sort_key)
                    
                temp += sortTime(sec,(key_num + 1))
                           
                curr_time = line[key]
                sec = [line]
        
        #if sort_key == "hour":
        #    sec = hourSort(sec)
        #else:
        mergeSort(sec,sort_key)

        temp += sortTime(sec,(key_num + 1))

    else:
        return arr

    return temp
    
       
            
def hourSort(arr):
    end = []
    sec = []
    for line in arr:
        if line["hour"] == 0:
            end.append(line)
        else:
            sec.append(line)
    
    mergeSort(sec,"hour")
    
    return sec + end
            
            
def mergeSort(arr,key):
    if len(arr) > 1:
        mid = int(len(arr)/2)
    
        L = arr[:mid]
        R = arr[mid:]
    
        mergeSort(L,key)
        mergeSort(R,key)
        
        count = 0
        l_ind = 0
        r_ind = 0
        
        while l_ind < len(L) and r_ind < len(R):
            if L[l_ind][key] < R[r_ind][key]:
                arr[count] = L[l_ind]
                l_ind += 1
            else:
                arr[count] = R[r_ind]
                r_ind += 1
            count += 1
        
        while l_ind < len(L):
            arr[count] = L[l_ind]
            l_ind += 1
            count += 1
        while r_ind < len(R):
            arr[count] = R[r_ind]
            r_ind += 1
            count += 1
            

        

#list = [4,2,3,9,10,1]
#mergeSort(list)

#print(list)
    
    




prob1()