import  sys
def check_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def get_next_date(dd, mm, yy):
    
    if check_leap_year(yy):
        if mm == 2:
            if dd == 29:
                dd = 1
                mm += 1
            else :
                dd += 1
            if mm == 12:
                mm = 1
                yy += 1
                
                
            print("{0}/{1}/{2}".format(dd,mm,yy))

        else:
            if dd == 31 or dd == 30:
                dd =  1
                mm += 1
            else:
                dd += 1
            if mm == 12:
                mm = 1
                yy += 1
                

            print("{0}/{1}/{2}".format(dd,mm,yy))
    else:
        if mm == 2:
            if dd == 28:
                dd = 1
                mm += 1
            else:
                dd += 1
            if mm == 12:
                mm = 1
                yy += 1
            print("{0}/{1}/{2}".format(dd,mm,yy))

        else:
            if dd == 31 or dd == 30:
                dd =  1
                mm += 1
            else:
                dd += 1
            if mm == 12:
                mm = 1
                yy += 1                

            print("{0}/{1}/{2}".format(dd,mm,yy))
def validate_input(dd,mm,yy):
    if check_leap_year(yy):
        if dd > 29:
            print("Invalid day")
            sys.exit(0)
    else:
        if dd > 28:
            print("Invalid Date")
            sys.exit(0)
    if mm > 12:
        print("Invalid date")
        sys.exit(0)
    if mm % 2 == 0 and mm > 30:
        print("Invalid Date")
        sys.exit(0)
    if mm % 2 != 0 and mm > 31:
        print("Invalid Date")
        sys.exit(0)
    
        
        
dd = int(input("Enter date"))
mm = int(input("Enter month"))
yy = int(input("Enter year"))
validate_input(dd,mm,yy)
get_next_date(dd,mm,yy)

