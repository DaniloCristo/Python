
def isSorted(arr):
    '''
    arr: uma lista
    retorno: retorna True caso a lista esteja ordenada e False caso não esteja
    '''
    #iterando sobre o array
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

#teste com inteiros
print(isSorted([1,2,3,4,6]))
#teste com char
print(isSorted(["a","b","d","c"]))    