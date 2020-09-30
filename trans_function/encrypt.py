import string


def encp(inp):
   lc = list(string.ascii_lowercase)
   uc = list(string.ascii_uppercase)
   ss = list(string.punctuation)
   dict = {}
   enmsg = [""]
   for x in xrange(0,26):
        dict[lc[x]] = ss[x]   # Encryption  body   
   inpt = list(inp)
   key = dict.keys()
   for fe in inpt:
        for c in key:
            if (fe == c):
                enmsg = enmsg + list(dict.get(c))
   print ''.join(enmsg)
                    

def inpt():
    print "################## ENCRYPTION function ##################"
    getinput = raw_input("Enter the Message here: ")
    encp(getinput)



if __name__ == '__main__':
        inpt()    
