# Python function to print permutations of a given list
def permutation(lst):
    if len(lst) == 0:
        return []
    
    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list. remLst is
        # remaining list
        remLst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)

    return l


# Driver program to test above function
data = [1,4,3,6,44,7]
print('size= {}'.format(len(permutation(data))))
for p in permutation(data):
    print (p)
