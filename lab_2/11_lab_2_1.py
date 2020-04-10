# SQRT Decomposition
# If you want to open the programm from the file, please, follow this link:
# https://github.com/MrDmitryBy/labs_python/blob/master/lab_2/11_lab_2_1.txt
# and save the programm 11_lab_2_1.py and 11_lab_2_1.txt in in a shared file
# Thank you for your attention! 

import math
import sys
import ast   

def blocks(array,sizeBlocks):
    block = [0]*sizeBlocks
    i = 0
    for i in range(len(array)):
        block[i//sizeBlocks] += array[i]
    return block

def leftRight():
    while True:                                
        left = input('From what part of an array '
                     'should I start (indexing is start from 0)?'
                     'If you want to exit, please,' 
                     'enter "exit" ') 
        if left == "exit":
            print("Good bye!")
            sys.exit()
        else:
            try:
                left = int(left)
                right = input('By what part of an array '
                              'should I finish (indexing is start from 0)?'
                              'If you want to exit, please,' 
                              'enter "exit" ')
                if right == "exit":
                    print("Good bye!")
                    sys.exit()
                else:
                    try:
                        right = int(right)
                        return left,right 
                    except:
                        print()
                        print("You make a mistake! Please, " 
                              "write an integer number(indexing is start from the 0)")
                        print('If you want to exit, please,enter "exit"')
            except:
                print()
                print("You make a mistake! Please, " 
                      "write an integer number (indexing is start from the 0)")
                print('If you want to exit, please,enter "exit"')

def findSum(left,right,array,sizeBlocks,bloki):
    sum = 0
    if left >= 0 and left <= right: 
        i = left
        if left//sizeBlocks == right//sizeBlocks:
            while (i <= right):
                sum += array[i]
                i +=1
        else:
            while (i <= (left//sizeBlocks+1)*math.ceil(math.sqrt(len(array))) - 1):
                sum += array[i]
                i += 1 
            j = (right//sizeBlocks)*sizeBlocks 
            while (j <= right):
                sum += array[j]
                j += 1
            k = (left//sizeBlocks) + 1
            while (k <= (right//sizeBlocks) - 1):
                sum += bloki[k]
                k += 1
    return sum
            
def main():
    if len(sys.argv) > 1:    
        file = open("11_lab_2_1.txt", "r");
        data = file.read(); 
        data = data.split('\n');
        try:
            array = ast.literal_eval(data[0])
            print("Your array is: ", array)
            print("P.S. Indexing is start from the 0")
            left = int(data[1])
            right = int(data[2]) 
            print("We start from the", left, "element and finish by ",right,
                  "element")
        except:
            print("Why did you change my file to the wrong data?")
            print("Please, open my file without changes")
            sys.exit()
    else:    
        array = []
        while True:
            print('If you want to exit, please,enter "exit"')
            arr = input('Enter array'
                        '( if you want to finish adding elements of array'
                         'enter "stop" ): ')
            if arr == "exit" or arr == "EXIT":
                sys.exit()
            elif  arr == "stop" or arr == "STOP":
                break
                
            else:
                try:
                    array.append(int(arr))
                except:
                    print("You make a mistake! Please, " 
                         "write an integer number"
                         "If you want finish adding elements of array"
                         "enter 'stop' ")
                    
            print()             
            print("Your array is: ", array)
    sizeBlocks = math.ceil(math.sqrt(len(array)))                              
    a = leftRight()
    left = a[0]
    right = a[1]       
    bloki = blocks(array,sizeBlocks)
    try:
        sum = findSum(left,right,array,sizeBlocks,bloki)
        print("Sum is equal to ", sum)
                            
    except:
        print()
        print("You make a mistake! Please, " 
              "write start number >= 0 and finish number greater than start")
        print('If you want to exit, please,enter "exit"')
                


if __name__ == "__main__":
    main()

              
