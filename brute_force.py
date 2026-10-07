import encode
import decode


def find_key(input_str:str)->str:
    for i in range(0,26):
        print(i,": ", decode.decode(test,i))
   

test = "kdoos"

test2 = "Hallo"

for i in range(0,26):
    print(i,": ", decode.decode(test,i))

for i in range(0,26):
    print(i,": ", encode.encode(test2,i))


find_key("")