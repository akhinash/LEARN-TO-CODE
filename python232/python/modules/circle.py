pi=3.14
def find_area(r):
    return pi*r*r
def find_peri(r):
    return 2*pi*r

if __name__=='__main__':
    print("this is a circle module")
    print("area",find_area(4))