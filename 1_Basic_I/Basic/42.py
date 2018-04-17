import struct
def check_bit():
    return(struct.calcsize("P") * 8)

if __name__ =="__main__":
    print(check_bit())