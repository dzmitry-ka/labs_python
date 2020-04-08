import math
import sys

def blocks(array,sizeBlocks):
    block = [0]*sizeBlocks
    i = 0
    for i in range(len(array)):
        block[i//sizeBlocks] += array[i]
    return block
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
    array = []
    flag = True
    while flag:
        arr = input('Enter array '
                    '( if you want finish adding elements of array'
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
    while flag:                                
        left = input('From what part of an array '
                     'should I start?'
                     'If you want to exit, please,' 
                     'enter "exit" ') 
        if left == "exit":
            flag = False
            print("Good bye!")
            sys.exit()
        else:
            try:
                left = int(left)
                right = input('By what part of an array '
                              'should I finish?'
                              'If you want to exit, please,' 
                              'enter "exit" ')
                if right == "exit":
                    print("Good bye!")
                    sys.exit()
                else:
                    try:
                        right = int(right)
                        bloki = blocks(array,sizeBlocks)
                        try:
                            sum = findSum(left,right,array,sizeBlocks,bloki)
                            print("Sum is equal to ", sum)
                        
                        except:
                            print()
                            print("You make a mistake! Please, " 
                                  "write start number >= 0 and finish number greater than start")
                            print('If you want to exit, please,enter "exit"')
                    except:
                        print()
                        print("You make a mistake! Please, " 
                              "write an integer number")
                        print('If you want to exit, please,enter "exit"')
            except:
                print()
                print("You make a mistake! Please, " 
                      "write an integer number")
                print('If you want to exit, please,enter "exit"')
                
"""if len(sys.argv) >= 0:
    array = []
    my_file = open("11_lab_2_1.txt", "r")
    if my_file.mode == 'r':
       arr = my_file.readlines()
       arr = arr.split()
       for line in my_file.readlines():
    # loop over the elemets, split by whitespace
            for i in line.split():
        # convert to integer and append to the list
                array.append(int(i))"""
       

if __name__ == "__main__":
    main()
