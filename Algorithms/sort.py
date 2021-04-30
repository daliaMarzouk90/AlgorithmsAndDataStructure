def larger(a, b):
    if(a > b):
        return True
    
    return False

def smaller(a, b):
    if(a < b):
        return True

    return False

def insertion_sort(array, comp_function = None):
    if(comp_function == None):
        comp_function = lambda a, b: a < b

    for i in range(1, len(array)):
        hole_pos = i

        swap = False
        temp = None

        for j in range(hole_pos, 0, -1):
            swap = comp_function(array[j], array[j - 1])

            if swap == False:
                break

            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp

    return array


def quick_sort(array, comp_function = None):
    if(comp_function == None):
        comp_function = lambda a, b: a > b
    
    size = len(array)

    if size <= 1:
        return array

    pivot = array[size - 1]

    i = 0    
    
    for j in range(size - 1):
        if(comp_function(pivot, array[j]) == False): #element is larger than pivote
            continue

        if(i == j):
            continue

        if(comp_function(array[j], array[i])):
            continue

        #element is smaller than pivote
        temp = array[i] 
        array[i] = array[j]
        array[j] = temp

        i = i+1

    if(comp_function(array[i], pivot) == True):
        temp = array[size - 1]
        array[size - 1] = array[i]
        array[i] = temp
    else:
        i = size - 2
    
    if(i >= 2):
        array[:i] = quick_sort(array[:i])
    if(i < size -1):
        array[i+1:] = quick_sort(array[i+1:])
            
    return array

array = quick_sort([8,9,6,4,10,30,0])
print(array)
