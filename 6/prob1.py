

def prob1(switch):
 
    ## Collect all the nodes
    ## node(num,x,y)
    coords = []
    with open("input.txt","r") as file:
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
    
    ## 2D array representing the map
    ## map[y][x] 0,0 upper left
    map = [["" for j in range(max_x+2)] for i in range(max_y+1)]
    ## Place the nodes in the map
    for node in coords:
        map[node[2]][node[1]] = "+" + str(node[0])
    
    ## Populate distances to square from each node
    if (switch == "part1"):
        for r in range(max_y+1):
            for c in range(max_x+2):
                dist = []
                if (not "+" in map[r][c]):
                    for node in coords:
                        dist.append(abs(node[1] - c)+abs(node[2] - r))
                        
                    if dist.count(min(dist)) > 1:
                        map[r][c] = "."
                    else:
                        map[r][c] = str(dist.index(min(dist)))
                        
                        
        areas = [0 for x in range(len(coords))]
        
        for r in range(max_y+1):
            for c in range(max_x+2):
                if ((r <= 0 or c <= 0 or r >= max_y or c >= max_x+1) and map[r][c] != "."):
                    areas[int(map[r][c])] = -1
                elif (map[r][c] != "." and areas[int(map[r][c])] != -1):
                    areas[int(map[r][c])] += 1
        return max(areas)
    else:
        total = 0
        for r in range(max_y+1):
            for c in range(max_x+2):
                dist = 0

                for node in coords:
                    dist += (abs(node[1] - c)+abs(node[2] - r))
                    
                if dist < 10000:
                    if not "+" in map[r][c]:
                        map[r][c] = "#"
                    total += 1
                else:
                    map[r][c] = "."
                    
        #for line in map:
        #    print(line)      
        return(total)
                    

     
    
print(prob1("part2"))