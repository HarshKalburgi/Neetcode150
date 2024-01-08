# Encode and Decode strings
# Design an algorithm to encode a list of strings to string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# please implement encode and decode
#code
class solution:
    def encode(self, strs):
        res=""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, str):
        res, i =[],0

        while i< len(str):
            j=1
            while str[j] !="#":
                j+=1
                length = int(str[i:j])
                res.append(str[j+1:j+1+length])
                i = j + 1 + length
            return res    
