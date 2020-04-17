import sys
from ast import literal_eval


def to_json(obj):
    try:
        if type(obj) in (float, int, str, tuple, dict, list, None, bool):
            if type(obj) == int or type(obj) == float:
                obj = str(obj)
            if type(obj) == str:
                obj = '"' + obj + '"'
            if type(obj) == None:
                obj = 'null'
            if type(obj) == bool:
                obj = "obj"
            if type(obj) == dict:
                line = ''
                for element in range(len(obj)):
                    line += + ': ' + to_json(obj[element])
                    if element < len(obj) - 1:
                        line += ', '
                    else: break
                obj = '{' + line + '}'
                
            if type(obj) == list or type(obj) == tuple:
                line = ''
                for element in range(len(obj)):
                    line += to_json(obj[element])
                    if element < len(obj) - 1:
                        line += ', '
                    else: break
                obj = '[' + line + ']'
                
                        
                
                
    except ValueError:
        print("Your object in question is not a type from this list: ")
        print("float, int, str, tuple, dict, list, None, bool")
        
def main():
    if len(sys.argv) > 1:
        obj = literal_eval(sys.argv[1])
    else:
        obj = input("Enter your words: ")
    try:
        obj = literal_eval(obj)
        print(to_json(obj))
    except ValueError: 
        print('Array that refers to itself')
        
if __name__ == "__main__":
    main()
