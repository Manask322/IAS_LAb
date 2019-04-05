
def get_ciper_text(ipt_list):
    l = []
    for i in range(len(ipt_list)//8):
        temp = ipt_list[i*8:(i + 1)*8]
        num = 0
        for j in range(7,-1,-1):
            num += temp[7-j]*pow(2,j)
        l.append(num)
    res = ''
    for j in l :
        res += chr(j)
    return res

class DES:
    def __init__(self,ipt_list,ipt_key_list):
        self.input_text = ipt_list
        self.input_keys = ipt_key_list
        self.expansion = [32, 1, 2, 3, 4, 5,
                        4, 5, 6, 7, 8, 9,
                        8, 9, 10, 11, 12, 13,
                        12, 13, 14, 15, 16, 17,
                        16, 17, 18, 19, 20, 21,
                        20, 21, 22, 23, 24, 25,
                        24, 25, 26, 27, 28, 29,
                        28, 29, 30, 31, 32, 1]


        self.permutation = [16, 7, 20, 21, 29, 12, 28, 17,
                            1, 15, 23, 26, 5, 18, 31, 10,
                            2, 8, 24, 14, 32, 27, 3, 9,
                            19, 13, 30, 6, 22, 11, 4, 25]
        self.S_Boxes = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
                        ],

                        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
                        ],

                        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
                        ],

                        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
                        ],

                        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
                        ],

                        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
                        ],

                        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
                        ],

                        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
                        ]]

    def get_expanded_bits(self,ipt_list):
        expanded_list = []
        for i in self.expansion:
            expanded_list.append(ipt_list[i - 1])
        return expanded_list

    def get_XOR(self,ipt_list_1,ipt_list_2):
        XOR_list = []
        for i in range(len(ipt_list_1)):
            XOR_list.append(ipt_list_1[i]^ipt_list_2[i])
        return XOR_list

    def get_decimal(self,ipt_list):
        decimal = 0
        for i in range(len(ipt_list)):
            decimal += pow(2,len(ipt_list) - 1 - i)*ipt_list[i]
        return decimal
    
    def get_binary(self,ipt):
        res = []
        # print(ipt)
        while(ipt > 0):
            res.append(ipt%2)
            ipt = ipt//2
        res = list(reversed(res))
        while len(res) < 4 :
            res.insert(0,0)
        return res

    def get_S_boxes(self,ipt_list):
        temp = ipt_list
        result_list = []
        for i in range(8):
            ipt_list = temp[i*6:(i+1)*6]
            # print(ipt_list)
            row = ipt_list[0]*2 + ipt_list[-1]
            col = self.get_decimal(ipt_list[1:5])
            dec = self.S_Boxes[i][row][col]
            temp_list = self.get_binary(dec)
            result_list += temp_list
        return result_list

    def get_Simple_Permuatation(self,ipt_list):
        permutation_list = []
        for i in self.permutation:
            permutation_list.append(ipt_list[i - 1])
        return permutation_list

    def Procedure(self):
        left_ipt_list = self.input_text[0:32]
        right_ipt_list = self.input_text[32:64]
        res = []
        for i in range(16):
            print(" Round {} ".format(i+1), end =" ")
            temp_list = right_ipt_list
            right_ipt_list = self.get_expanded_bits(right_ipt_list)
            right_ipt_list = self.get_XOR(right_ipt_list,self.input_keys[i])
            right_ipt_list = self.get_S_boxes(right_ipt_list)
            right_ipt_list = self.get_Simple_Permuatation(right_ipt_list)
            right_ipt_list = self.get_XOR(right_ipt_list,left_ipt_list)
            left_ipt_list = temp_list
            # print(right_ipt_list)
            if i != 15 :
                print(''.join(str(v) for v in (left_ipt_list + right_ipt_list) ))
                res.append(left_ipt_list+right_ipt_list)
        print(''.join( str(v) for v in (right_ipt_list + left_ipt_list) ))
        res.append(right_ipt_list + left_ipt_list)
        return right_ipt_list + left_ipt_list,res

class Permute1:
    def __init__(self):
        self.permutation_choice_1_array = [0]*64
        self.permutation_choice_2_array = [0]*64
        # print(self.permutation_choice_1_array)

    
    def initialise_arrays(self):
        self.permutation_choice_1_array = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
        self.permutation_choice_2_array =[14,17,11,24,1,5,3,28,
        15,6,21,10,23,19,12,4,
        26,8,16,7,27,20,13,2,
        41,52,31,37,47,55,30,40,
        51,45,33,48,44,49,39,56,
        34,53,46,42,50,36,29,32]

    def PC_1(self,ipt_string):
        intermediate_list = []
        for i in self.permutation_choice_1_array:
            intermediate_list.append(ipt_string[i - 1])
        return intermediate_list
    
    def PC_2(self,ipt_string):
        final_list = []
        for i in self.permutation_choice_2_array:
            final_list.append(ipt_string[i-1])
        return final_list
    
    def left_shfit(self,ipt_string,id):
        id_l = [1,2,9,16]
        if id in id_l :
            shift = 1
        else:
            shift = 2
        while shift > 0 :
            temp = ipt_string[0]
            for i in range(len(ipt_string) - 1):
                ipt_string[i] = ipt_string[i+1]
            ipt_string[len(ipt_string) - 1] = temp
            shift = shift - 1
        return ipt_string
    


class Permute:
    def __init__(self):
        self.initial_permutation_array = [0]*64
        self.final_permutation_array = [0]*64
        # print(self.initial_permutation_array)

    
    def initialise_arrays(self):
        self.initial_permutation_array = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
        self.final_permutation_array = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
    
    def intermediate_permutation(self,ipt_string):
        intermediate_list = []
        for i in self.initial_permutation_array:
            intermediate_list.append(ipt_string[i - 1])
        return intermediate_list
    
    def final_permtation(self,ipt_string):
        final_list = []
        for i in self.final_permutation_array:
            final_list.append(ipt_string[i-1])
        return final_list
    
def padding(input_string):
    if len(input_string)%8 == 0 :
        return input_string
    padd_len = 8 - len(input_string)%8
    l = ' '*padd_len
    return input_string + l

def string_to_ASCII(input_string):
    res_l = []
    for i in input_string:
        res_l.append(ord(i))
    return res_l 

def get_binary(ipt):
    res = []
    print(ipt)
    return res
    while(ipt > 0):
        res.append(ipt%2)
        ipt = ipt/2
    while len(res) < 8 :
        res.insert(0,0)
    return res

def ASCII_to_binary(ascii_string_list):
    res_list = []
    temp1 = ''
    for i in ascii_string_list:
        # res_list.append(get_binary(i))
        temp =''
        while(i > 0):
            temp = temp + str(i%2)
            i = i//2
        temp = temp[::-1]
        while len(temp) < 8 :
            temp = '0' + temp
        # break
        temp1 = temp1 + temp
    res_list = list(temp1)
    res_list = list(map(int, res_list))
    return res_list


def execute(inpt_string,input_key):
    ipt_key = []
    P = Permute1()
    P.initialise_arrays()
    input_string = input_key
    # print(input_string)   
    # print(input_string)
    
    # input_string = padding(input_string)
    # print(len(input_string))
    choice = 1
    if len(input_string) < 8 :
        print("Error Minimum size of input string should be 8")
        return 

    if choice == 1 :
        input_string = input_string[0:8]
    elif choice == 2 :
        input_string = input_string[len(input_string) - 8:len(input_string)]

    
    ascii_string_list = []
    ascii_string_list = string_to_ASCII(input_string)
    # print(ascii_string_list)
    
    initial_list = []
    total_list =[]
    # for i in range(len(ascii_string_list)//8):
    binary_list = []
    binary_list = ASCII_to_binary(ascii_string_list)
    ##print("initial : ",end =" ")
    # print(binary_list)
    # print(''.join(str(v) for v in binary_list))
    initial_list.append(binary_list)
    intermediate_list = P.PC_1(binary_list)
    ##print("56- bit key : ", end=" ")
    # f.write("56- bit key : ")
    ##print(''.join(str(v) for v in intermediate_list))
    # f.write(''.join(swtr(v) for v in intermediate_list))
    ##print()
    # f.write("\n")
    for i in range(1,17):
        left_list = P.left_shfit(intermediate_list[0:28],i)
        # print(intermediate_list[0:28])
        # print(left_list)
        right_list = P.left_shfit(intermediate_list[28:56],i)
        intermediate_list = left_list + right_list
        # print("Round {} : ".format(i), end ="")
        # f.write("Round ")        
        # f.write(str(i) + " : ")
        final_list = P.PC_2(intermediate_list)
        ipt_key.append(final_list)
        ##for i in range(6) :
            ##print(''.join(str(v) for v in final_list[i*8:(i+1)*8]), end=" ")
        ##print("")
        # print("------------------------------------------------")
    # print(len(ipt_key[0]))

    P = Permute()
    P.initialise_arrays()
    input_string = inpt_string
    # print(input_string)
    if len(input_string) > 40 :
        print("input size should be less than 40 bytes")
        return 
    input_string = padding(input_string)
    # print(len(input_string))

    ascii_string_list = []
    ascii_string_list = string_to_ASCII(input_string)
    # print(ascii_string_list)

    return_list = []
    for i in range(len(ascii_string_list)//8):
        initial_list = []
        total_list =[]
        inter_list = []
        ipt_list = []
        inter_value = []
        # binary_list = []
        print("STRING : " + input_string[i*8:(i+1)*8])
        ipt_list.append(input_string[i*8:(i+1)*8])
        binary_list = ASCII_to_binary(ascii_string_list[i*8:(i+1)*8])
        print("initial : " ,end="")
        # file_output.write
        print( ''.join(str(v) for v in binary_list))
        initial_list += (binary_list)
        intermediate_list = P.intermediate_permutation(binary_list)
        D = DES(intermediate_list,ipt_key)
        intermediate_list,res =  D.Procedure()
        inter_list += res
        # print("intermediate")
        # print(intermediate_list)
        print("Final : ",end="")
        final_list = P.final_permtation(intermediate_list)
        total_list += final_list
        print(''.join( str(v) for v in final_list),end="")
        # print(get_ciper_text(final_list))
        return_list.append([ipt_list,initial_list,inter_list,total_list])
        print()
    # print(initial_list)
    # print(total_list)
    # print(inter_list)
    return return_list
    print(return_list[1][3],len(return_list[1][3]))


