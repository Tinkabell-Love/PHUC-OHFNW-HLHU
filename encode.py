

def encode(input_str:str, number:int):

    output_str_tmp = []
    output_str = ""

    #input_str_tmp = input_str.lower()

    for char in input_str:
        output_str_tmp.append((ord(char) - 65 + number) % 26 + 65)

    for i in output_str_tmp:        
        output_str += (chr(i))

        #print(chr(i))

    return output_str



#print(ord("A"))
#print(chr(65))
#
#print(ord("Z"))

#print(encode("ABC",3))
#
#
#print(ord("Z")+3)


#print(ord("Ä"))