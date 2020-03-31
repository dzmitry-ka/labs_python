#Power of 2
import sys

def main():
    while True:
        try: 
            if len(sys.argv[0]) > 1:
                x = sys.argv[1]
        except:
            x = input("""\tEnter the number: 
                        
                            !ATTENTION! 
                            If you want exit from the programm, enter "exit" 
                              """)
        if x == "exit":
            break
        else: 
            try:
                x = int(x)
                def power(x):
                    if x & (x - 1) == 0 and x != 0:
                        return 1
                if power(x) == 1:
                    print()
                    print("Yes, number ", x, " is a power of 2")                    
                else: 
                    print()
                    print("Unfortunately, number ", x, " isn't a power of 2")
                k = input('Do you want try again? Please, write "Yes" or "No" ')
                if k == "yes" or k == "Yes" or k == "YES":
                    continue
                else:
                    if k == "no" or k == "NO" or k == "No":
                        break
                    else:
                        print('Because you are dummy, the programm will run again')
                        
            except:
                print()
                print("You make a mistake, please, write \n \
                      an integer positive number: ")
     
if __name__ == "__main__":
 main()
 
