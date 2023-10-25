import sys
from config import DB_DETAILS

def main():
    #program takes atleast one argument
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)
    for args in sys.argv:
        print(args)
    print("hello")

if __name__=="__main__":
    main()  