
def prob1():
    DIRS = [(0,1),(-1,0),(0,-1),(1,0)]
   
    coords = []
    with open("test.txt","r") as file:
        node_num = 0
        max_x = 0
        max_y = 0
        max_node = 0
        
        for line in file:
            data = line.split(",")
            coord = (int(node_num),int(data[0].strip()),int(data[1].strip()))
            if coord[1] > max_x:
                max_x = coord[1]
                max_node = coord[0]
            if coord[2] > max_y:
                max_y = coord[2]
                max_node = coord[0]
            
            coords.append(coord)
            node_num += 1
    
    print(max_x,max_y)
    map = [["" for j in range(max_x+2)] for i in range(max_y+1)]
    for node in coords:
        #map[y][x]
        map[node[2]][node[1]] = "|" + str(node[0])
        
        cx = node[1]
        cy = node[2]
        dist = 2
        count = 1 # dist from current node
        
        done = False
        while not done:
            cx += 1
            cy -= 1
            
            for dir in DIRS:
                ind = 0
                #print(dir)
                while (ind < dist):
                    
                    cy += dir[1]
                    cx += dir[0]
                    #print(cx,cy)
                    #print(max_x)
                    if (cy <= max_y and cx <= max_x+1 and cy >= 0 and cx >= 0):
                        if (map[cy][cx] == ""):
                            map[cy][cx] = str(node[0]) + "-" + str(count)
                        elif ("-" in map[cy][cx] and int(map[cy][cx].split("-")[1]) > count):
                            map[cy][cx] = str(node[0]) + "-" + str(count)
                        elif ("-" in map[cy][cx] and int(map[cy][cx].split("-")[1]) == count):
                            map[cy][cx] = str(node[0]) + "x" + str(count)
                        #elif ("x" in map[cy][cx] and int(map[cy][cx].split("x")[1]) > count):
                        #    map[cy][cx] = str(node[0]) + "-" + str(count)
                    
                    
                    
                    ind += 1
            for line in map:
                print(line)
            input()
            dist += 2
            count += 1
            if count > max_x+1:
                done = True
        
        
    
            #input()
    #for line in map:
    #    print(line)
    
        
     
    
prob1()