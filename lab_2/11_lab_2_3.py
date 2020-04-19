# If you want to open program using files, then write the full path to them
# You must specify two files:
# 1)From what file do you get the text?
# 2)Which file are you sending the result to?
# P.S. Only supported with .txt format


import sys
from re import search

def load(i, B):
    quantity =  int(i/B*100) 
    procent = '✡'*int(quantity/5)+'[]'*int((100-quantity)/5) 
    sys.stdout.write('\rProgress: {1} ◀ {0}% ▶ '.format(quantity, procent))
    sys.stdout.flush()


def MergeSort(array):
    if len(array) == 0:
        array = []
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i, j, k = 0, 0, 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1
            


def main():
    array = []
    try:
        if len(sys.argv) > 1:
            if len(sys.argv) == 3:
                fileName1 = sys.argv[1]
                if search(r'\b.txt\b', fileName1):
                    fileName2 = sys.argv[2]
                    if search(r'\b.txt\b', fileName2):
                        fileName2 = fileName2    
                   
        else:
            fileName1 = input("Enter name of the input file: ")
            fileName1 = fileName1.strip(' ')
            fileName2 = input("Enter name of the output file: ")
            fileName2 = fileName2.strip(' ')
    except:
        print("You have entered not enough arguments"
              "or you did not enter .txt at the end of the file name")
        print("Please, enter names of the input and output files "
              "in this sequence")
   

    file1 = open(fileName1, "r")
        
    lines = file1.read().split('\n')
    
    for string in lines:
        array.append(string)
    for i in range(len(array)):
        array[i]=array[i].split()
        MergeSort(array[i])
    
    MergeSort(array)
    
    result = ''
    i = 1
    for parameters in array:
        result +=  ' '.join(parameters) + '\n'
        load(i, len(array))
        i += 1
        
    print()
    print(result)
    file2 = open(fileName2, "w")
    file2.write(result)
    file2.close()
    
    
if __name__ == "__main__":
    main()
