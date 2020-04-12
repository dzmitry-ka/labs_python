import random
import string


def main():
    fileName = input("Enter your name of a file: ")
    fileName = fileName.strip(' ')
    file = open((fileName + '.txt'), "w")
    alphabet = list(string.ascii_letters) 
    try:
        MB = float(input("Enter a float size of a file in MB: "))
        B = 1048576 * MB           
        K = (10,100)
        L = (3,10)
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
                    
        print(lines)
                    

    except ValueError:
        print("Please, enter a float size of a file: ")
    file.write(lines)
    file.close()

if __name__ == "__main__":
    main()
