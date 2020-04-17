import random
import string
import sys
import re
import ast
import math

def load(i, B):
    quantity =  math.floor(i/B*100)
    procent = '✡'*math.floor(quantity/3)+'[]'*math.ceil((100-quantity)/3)
    sys.stdout.write('\rProgress: {1} ◀ {0}% ▶ '.format(quantity, procent))
    sys.stdout.flush()

def generator(K,L,B,alphabet):
    lines = ''
    while lines.__sizeof__() <= B:
        nWords = random.randrange(K[0],K[1]) #кол-во слов в строке
        for tWord in range(nWords): # начинается взаимодействие со словом 
            lwords = random.randrange(L[0],L[1]) #длина конкретного слова
            for word in range(lwords):
                word = ''.join(random.choice(alphabet) for changer in range(lwords)) # заполнение слова случайными буквами 
                lines = lines + word
                if lines.__sizeof__() <= B:
                    lines = lines + ' '
                else:
                    break
        load(lines.__sizeof__() + 1, B)
    return lines


def main():
    K = (10,100)
    L = (3,10)
    alphabet = list(string.ascii_letters)
    if len(sys.argv) > 1:
        if len(sys.argv) == 3:
            try:
                fileName = sys.argv[1]
                if re.search(r'\b.txt\b', fileName):
                    file = open(fileName, "w")
                    try:
                        MB = float(sys.argv[2])
                        B = 1048576 * MB
                        print(fileName)
                        if len(sys.argv) == 4:
                            try:
                                K = ast.literal_eval(sys.argv[3])  
                                if K[0] <= K[1] and type(K[0]) == int and type(K[1]) == int:
                                    if len(sys.argv) == 5:
                                        try:
                                            L = ast.literal_eval(sys.argv[4])
                                            if L[0] <= L[1] and type(L[0]) == int and type(L[1]) == int:
                                                L = L
                                            else:
                                                print("You make a mistake, because L isn't",
                                                      "int type or L[0] is not <= L[1]")
                                                sys.exit()    
                                        except:
                                            print("Please, enter an int K with brackets: ")
                                            print("For example: (1,3)")
                                            sys.exit()
                    
                                    else:        
                                        pass
                                else:
                                    print("You make a mistake, because K isn't",
                                          "int type or K[0] is not <= K[1]")
                                    sys.exit()
                            
                            except:
                                print("Please, enter an int K with brackets: ")
                                print("For example: (1,3)")
                                sys.exit()
                    
                        else:        
                            pass
                        
                    except ValueError:
                        print("Please, enter a float size of a file: ")
                        sys.exit()   

            except:
                print("You are not enter .txt file or you enter a space in the",
                      "line command.")
                print("Please, write file without space and with .txt format ")
                sys.exit()
       

            
    else:  
        fileName = input("Enter your name of a file: ")
        fileName = fileName.strip(' ')
        file = open((fileName + '.txt'), "w") 
        try:
            MB = float(input("Enter a float size of a file in MB: "))
            B = 1048576 * MB           

        except ValueError:
            print("Please, enter a float size of a file: ")
            sys.exit()

        
    lines = generator(K,L,B,alphabet)
    #print(lines)     
    file.write(lines)
    file.close()

if __name__ == "__main__":
    main()
