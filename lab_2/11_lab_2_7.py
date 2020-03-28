# Leonardo numbers with with runtime O(log n) 
import sys

def main():
    while True:
        try: 
            if len(sys.argv[0]) > 1:
                n = sys.argv[1]
        except:        
            n = input("Enter the number: ")
        if n == "exit":
            break
        else: 
            try:
                n = int(n)
                if n >= 0:
                    def multiply(Q, M) :
                        x = Q[0][0] * M[0][0] + Q[0][1] * M[1][0] 
                        y = Q[0][0] * M[0][1] + Q[0][1] * M[1][1] 
                        z = Q[1][0] * M[0][0] + Q[1][1] * M[1][0] 
                        w = Q[1][0] * M[0][1] + Q[1][1] * M[1][1] 
                        Q[0][0] = x 
                        Q[0][1] = y 
                        Q[1][0] = z 
                        Q[1][1] = w 
                           
                    def power(Q, n) : 
                        M = [[ 1, 1 ], [ 1, 0 ] ] 
                        
                            # n - 1 times multiply the matrix 
                            # to {{1, 0}, {0, 1}} 
                        for i in range(2, n + 1) : 
                                multiply(Q, M) 
                                  
                          
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
                              
                             
                    print("Leonardo number is ", leon(n)) 
                
                else: 
                    print("You make a mistake, please, write \n \
                          a positive number: ")
                
            except:
                print("You make a mistake, please, write \n \
                      an integer positive number: ")
if __name__ == "__main__":
    main()
    
