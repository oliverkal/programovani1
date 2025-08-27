import sys
def nacteni_souboru(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(map(int, line.strip().split())))              #can be optimized, so output is not 2D array
        return array

if len(sys.argv) < 3:
    sys.exit(1)
path_l = sys.argv[1]
path_r = sys.argv[2]


left_list = []
right_list = []
left = nacteni_souboru(path_l)
right = nacteni_souboru(path_r)
for i in left:                              #only because of 2D array output in nacteni_souboru function    
    for j in i:
        left_list.append(j)
for i in right:
    for j in i:
        right_list.append(j)

#left_list = [3,4,2,1,3,3]
#right_list = [4,3,5,3,9,3]

count = 0
def appereance(left_list, right_list):                  #funtcion for appereance
    global count                                        #take global variable count
    scores = []
    for value in left_list:
        for target in right_list:
            if  value == target:                        #check if value in left_list is equal to target in right_list
                count += 1                              #increment the appereance of the matching value
        sim_score =  count * value                      #similarity score is the product of count and value
        scores.append(sim_score)
        count = 0                                       #reset count for the next value
    return scores

suma=0  
for score in appereance(left_list, right_list):       #call the function and iterate through the scores
    #print(score)
    suma += score
print(suma) 







            
        


