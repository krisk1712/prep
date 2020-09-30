import string

def decr():
   lc = list(string.ascii_lowercase)
   uc = list(string.ascii_uppercase)
   ss = list(string.punctuation)
   dict = {}
   decmsg = [""]
   for x in xrange(0,26):
        dict[lc[x]] = ss[x]       
   inp = raw_input("MEssage here : ")
   inpt = list(inp)
   val = dict.values()
   for fe in inpt:
        for key, val in dict.iteritems():
            if (fe == val):
                decmsg = decmsg + list(key)
   print ''.join(decmsg)             


decr()
