# Leonardo numbers with with runtime O(log n) 
import sys

def main():
    flag = True
    while flag:
        try: 
            if len(sys.argv[0]) > 1:
                n = sys.argv[1]
                flag = False
        except:        
            n = input("""Enter the number:
                
                
                      !ATTENTION! 
                      If you want exit from the programm, enter "exit" 
                      """)
        if n == "exit" or n == "EXIT":
            break
        else: 
            try:
                n = int(n)
                if n >= 0:
                    def multiplication(Q, M) :
                        a = Q[0][0] * M[0][0] + Q[0][1] * M[1][0] 
                        b = Q[0][0] * M[0][1] + Q[0][1] * M[1][1] 
                        c = Q[1][0] * M[0][0] + Q[1][1] * M[1][0] 
                        d = Q[1][0] * M[0][1] + Q[1][1] * M[1][1] 
                        Q[0][0] = a 
                        Q[0][1] = b 
                        Q[1][0] = c 
                        Q[1][1] = d 
                           
                    def power(Q, n) : 
                        M = [[ 1, 1 ], [ 1, 0 ] ]                      
                        for i in range(2, n + 1) : 
                                multiplication(Q, M) 
                                  
                          
                    def fib(n) : 
                        Q = [ [ 1, 1 ], [ 1, 0 ] ] 
                        if (n == 0) : 
                            return 0
                        power(Q, n - 1) 
                        return Q[0][0] 
                           
                    def leon(n) : 
                        if (n == 0 or n == 1) : 
                            return 1
                        return (2 * fib(n + 1) - 1) 
                              
                    print()         
                    print("Leonardo number is ", leon(n)) 
                
                else: 
                    print()
                    print("You make a mistake, please, write \n \
                          a positive number: ")
                
            except:
                print()
                print("You make a mistake, please, write \n \
                      an integer positive number: ")
if __name__ == "__main__":
    main()
    
