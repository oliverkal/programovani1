#listy = [[10,6,4,2,1], [7,6,4,2,1], [7,6,4,2,1], [10,6,4,2,1]]
#from collections import Counter

import sys
def nacteni_souboru(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(list(map(int, line.strip().split()))) 
        return array

path = sys.argv[1]
levels = nacteni_souboru(path)

#print(levels)

def inc_dec(level):                                 #Function to check if the list is either increasing or decreasing
    increasing = True
    decreasing = True
    for i in range(len(level) -1):
        if level[i] <= level[i+1]:
            decreasing = False
        if level[i] >= level[i+1]:
            increasing = False                  #return False if both increasing or decreasing are False
    return increasing or decreasing             #else return True if either increasing or decreasing is True
    #if level == sorted(level):                                 this apparoach is wroking as well/ sorted()
     #   return True
    #elif level == sorted(level, reverse = True):
    #    return True
    #else:
    #    return False
        
#print(listy)
#print(list[-1]) jak najit posledni prvek v listu
# list[-1] vrati posledni prvek v listu, a list[::-1] vrati "obraceny list"

def check_safety(listy):                        #check safety of the list
    count = 0
    unsafe_arrays = []                                   
    for list in listy:
        #print(list)
        #list.sort()
        last_element = list[-1]
        safety = True
        if not inc_dec(list):
            unsafe_arrays.append(list)                #if the list is not increasing or decreasing, it is unsafe, conitnue and go to the next list    
            continue
            
        for index in range(len(list) - 1):          #take the indexes of the list based on the length of the list
            current = list[index]                      
            next_val = list[index + 1]              #that way we can check next value: lasi[index+1]
            diff = abs(next_val - current)          #calculate the differece that is next value minus current value  
            if (diff < 1 or diff > 3):              #if the difference is less than 1 or exceeds 3, it is unsafe                  #print("UNSAFE")
                unsafe_arrays.append(list)
                safety = False                      #set safety to False
                break                               #break the loop, we don't need to check the rest of the list
#if (((abs(list[index +1] -i)) <= 3 and (abs(list[index + 1] -i)) >= 1)) and (list[index + 1] > i):
            else:
                safety = True                     #else safetu is True
        if safety:                                      
            count += 1                             #if safety is True, increment count, outside of the loop checking the current indexes of the current list
           #print("SAFE")
    #print(unsafe_arrays) 
    return count, unsafe_arrays               #return the unsafe arrays and the count of safe arrays    
    


#tuple_list = [tuple(sublist) for sublist in (check_safety(levels)[1])]  # Convert each sublist to a tuple
#counts = Counter(tuple_list)
#duplicates = [list(t) for t, count in counts.items() if count > 1]
#print(duplicates)


safe2 = 0
#count = (check_safety(levels)[0])  
unsafe_arrays = levels#(check_safety(levels)[1])

def inc(level):
    for i in range(len(level)-1):
        if level[i] >= level[i+1]:
            return False
    return True

def dec(level):
    for i in range(len(level)-1):
        if level[i] <= level[i+1]:
            return False            
    return True

def check_dif(level):
    for i in range(len(level)-1):
        current = level[i]
        next_val = level[i+1]
        dif = abs(next_val - current)
        if (dif < 1) or (dif > 3):
            return False
    return True

def remove_inc(level):
    for i in range(len(level)):
        removed = level[:i] + level[i+1:]           #orezat list pomoci list[:i]+list[i+1:], kde cislo na pozici i oreze a necha zbytek listu
        if inc(removed) and check_dif(removed):     #check if the removed list is increasing and has no difference anomaly
            return True, removed
    return False

def remove_dec(level):
    for i in range(len(level)):
        removed = level[:i] + level[i+1:]
        if dec(removed) and check_dif(removed):     #check if the removed list is decreasing and has no difference anomaly
            return True, removed
    return False

false_inc_dec = []
inc_dec_arrays = []             #arrays that are either increasing or decreasing, but have difference anomaly              
for array in unsafe_arrays:
    if not (inc(array) or dec(array)):
        false_inc_dec.append(array)
    else:
        inc_dec_arrays.append(array)
#for i in range(len(false_inc_dec)):
    #print(i)
#print(inc_dec_arrays)
#print(false_inc_dec)
roztridit_false_inc_dec = []
for i in false_inc_dec:
    if remove_inc(i):
        #print(remove_inc(i))
        roztridit_false_inc_dec.append(remove_inc(i)[1])
    elif remove_dec(i):
        #print(remove_dec(i))
        roztridit_false_inc_dec.append(remove_dec(i)[1])

    else:
        #print(i)
        continue

#print(" ")
#print(roztridit_false_inc_dec)


counter = 0

#print(roztridit_false_inc_dec)

for i in roztridit_false_inc_dec:
    if  check_dif(i):                                       #tahle podminka uz je pouzita remove_inc/remove_dec funkcich, pro jistotu ji nechavam
        counter +=1
        #print(i)
#print(counter)
#print(inc_dec_arrays)

def remove_dif(level):
    for i in range(len(level)):
        removed = level[:i] + level[i+1:]
        if check_dif(removed):
            return True, removed
    return False
for i in inc_dec_arrays:
    #print(remove_dif(i))
    if remove_dif(i):
        safe2+= 1
#print(len(inc_dec_arrays))
#print(safe2)
solution = safe2 + counter
print(solution)
                   
                   
