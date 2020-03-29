import math
def main():
    while True:
        array = []
        array = input('Enter the elements of array'
                      'If you want to exit, please, enter "exit" ')
        if array == "exit":
            print("Good bye!")
            break
        else:
            while True:
                if array == "stop" or "STOP":
                    return False
                else:
                    try:
                        array = array.append(float(array))
                        sizeArray = len(array)
                        sizeBlocks = math.ceil(math.sqrt(sizeArray))
                def blocks():
                    block = [0]*sizeBlocks
                    i = 0
                    for i in sizeArray - 1:
                        block[i//sizeBlocks] = array[i]
                        i += 1
                        return block
                    def findSum():
                        while True:
                            sum = 0
                            left = input('From what part of an array'
                                         'should I start?'
                                         'If you want to exit, please,' 
                                         'enter "exit" ') 
                            if left == "exit":
                                print("Good bye!")
                                break
                            else:
                                try:
                                    left = int(left)
                                    right = input('By what part of an array'
                                            'should I finish?'
                                            'If you want to exit, please,' 
                                            'enter "exit" ')
                                    if right == "exit":
                                        print("Good bye!")
                                        break
                                    else:
                                        try:
                                            right = int(right)
                                            try:
                                                if left >= 0 and left <= right: 
                                                    i = left
                                                    while (i <= right):
                                                        sum += array[i]
                                                        i +=1
                                                    return sum
                                                print("Sum is equal to ", sum)
                                    
                                            except: print("You make a mistake! Please, " 
                                                          "write start number >= 0 and finish number greater than start")
                                                    print('If you want to exit, please,enter "exit"')
                                        except: 
                                            print("You make a mistake! Please, " 
                                                  "write an integer number")
                                            print('If you want to exit, please,enter "exit"')
                                except:
                                    print("You make a mistake! Please, " 
                                          "write an integer number")
                                    print('If you want to exit, please,enter "exit"')
                                        
                    except: 
                        print("You make a mistake! Please, write a float number(-s)")

if __name__ == "__main__":
    main()
