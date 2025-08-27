import sys
sys.setrecursionlimit(2000)
def nacteni_souboru(file_path):
    array = []
    with open(file_path, 'r') as file:
        for i in file:
            array.append(list(map(int, i.strip().split())))
        return array
if len(sys.argv) < 3:
    sys.exit(1)
path_l = sys.argv[1]
path_r = sys.argv[2]



left_list = nacteni_souboru(path_l)
right_list = nacteni_souboru(path_r)

#left_list = [3,4,2,1,3,3]
#right_list = [4,3,5,3,9,3]


left = []
right = []
for i in left_list:
    for j in i:
        left.append(j)
for i in right_list:
    for j in i:
        right.append(j)
#print(left)
#print(right)
    


def min_val(left_list, right_list, distances):
    min_val1 = min(left_list)
    min_val2 = min(right_list)
    distance = abs(min_val1 - min_val2)
    
    distances.append(distance)
    #return distances
    
    left_list.pop(left_list.index(min_val1))
    right_list.pop(right_list.index(min_val2))
    #return distances, left_list, right_list

    if len(left_list) and len(right_list) != 0:
        min_val(left_list, right_list, distances)
        #distances.append(distance)
    return distances



distances = []
delky = min_val(left, right, distances)
sum = 0
for delka in delky:
    sum += delka


print(sum)

