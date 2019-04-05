class BlindAttack:
    def __init__(self,msg,p,q,r,e,N):
        self.msg = msg
        self.p = p 
        self.q = q 
        self.r = r
        self.e = e
        self.N = N
        self.qN = (p-1)*(q-1)
        self.blind = ''
        self.blind_text = ''
        self.msg_sender_sign = ''
        self.msg_sender_sign_text = ''
        self.sender_sign = ''
        self.sender_sign_text = ''
        self.original_msg = ''
    
    def get_val(self,ipt):
        ipt = ipt.encode('utf-8')
        ipt = ipt.hex()
        return int(ipt,16)

    def get_d(self):
        i = 1
        e = self.e%self.qN
        # print(self.e,self.qN)
        d = (e*i)%self.qN
        while( d != 1):
            d = (e*i)%self.qN
            i += 1
            if(i > self.qN):
                print("here")
                return -1        
        return (i - 1) 
    
    def get_r(self):
        i = 1
        r = self.r%self.N
        d = (r*i)%self.N
        while( d != 1):
            i += 1
            d = (r*i)%self.N     
            if( i > self.N ):
                return -1    
        return i 
    
    def get_text(self,ipt):
        print(ipt)
        hex_res = hex(ipt)[2:]
        res = bytes.fromhex(hex_res).decode('utf-8')
        return res
        

    def implement(self,ipt,inter_list):
        d = self.get_d()
        if d == -1 :
            print("no valid value for d ")
            inter_list.append("no valid value for d ")
            return 
        print("value for d :" + str(d))
        inter_list.append("value for d :" + str(d))
        
        ri = self.get_r()
        if ri == -1 :
            print("no valid value for r inverse") 
            inter_list.append("no valid value for r inverse")     
            return 
        print("value of ri :" + str(ri))
        inter_list.append("value of ri :" + str(ri))

        ipt = (ipt*pow(self.r,self.e))%self.N
        self.blind += str(ipt)
        # print(self.blind)
        print("Blind Attack Message : " + str(ipt))
        inter_list.append("Blind Attack Message : " + str(ipt))
        ipt = (pow(ipt,d))%self.N
        self.msg_sender_sign += str(ipt)
        print("Message with senders signature : " + str(ipt)) 
        inter_list.append("Message with senders signature : " + str(ipt))  
        ipt = (ipt*ri)%self.N
        self.sender_sign += str(ipt)
        print("Senders signature : " + str(ipt))      
        inter_list.append("Senders signature : " + str(ipt))
        ipt = (pow(ipt,self.e))%self.N
        print("Original Message : " + str(ipt))    
        inter_list.append("Original Message : " + str(ipt))
        self.original_msg += self.get_text(ipt)
        # print(ipt)
        return inter_list
    
    def get_block_size(self):
        i = 1 
        while( pow(2,8*i) <= self.N ):
            i += 1
        return (i - 1)

    def procedure(self):
        j = ''
        final_list = []
        val = 0
        flag = 1
        s_i = 0 
        block_size = self.get_block_size()
        print("block_size : " + str(block_size))
        final_list.append("block_size:" + str(block_size))
        e_i = s_i + block_size
        while( e_i < len(self.msg)):
            inter_list = []
            print("input_text_for block :" + self.msg[s_i:e_i])
            inter_list.append("input_text_for block :" + self.msg[s_i:e_i])
            val = self.get_val(self.msg[s_i:e_i])
            inter_list =  self.implement(val,inter_list)
            s_i = e_i 
            e_i = s_i + block_size
            final_list.append(inter_list) 
            print()

        if s_i == (len(self.msg)- 1):
            inter_list = []
            print("input_text_for block :" + self.msg[s_i])
            inter_list.append("input_text_for block :" + self.msg[s_i])
            val = self.get_val(self.msg[s_i])
            inter_list = self.implement(val,inter_list)
            final_list.append(inter_list)
        elif(s_i < len(self.msg)):
            inter_list = []
            print("input_text_for block :" + self.msg[s_i:len(self.msg)])
            
            inter_list.append("input_text_for block :" + self.msg[s_i:len(self.msg)])
            val = self.get_val(self.msg[s_i:len(self.msg)])
            inter_list =  self.implement(val,inter_list)
            final_list.append(inter_list)
        print(self.blind, self.msg_sender_sign, self.sender_sign)
        return final_list
  
  
  

def main():
    # msg = input("Enter Message : ")
    msg = "NITK575025"
    # e = int(input("Enter e :"))
    e = 5
    p = 1013
    q = 1019
    r = 22
    # r = int(input("Enter r :"))
    # p = int(input("Enter p :"))
    # q = int(input("Enter q :"))
    # N = int(input("Enter N :"))
    N = p*q
    Attack = BlindAttack(msg,p,q,r,e,N)
    # print(Attack.get_text(20041))
    res = Attack.procedure()
    print( "Original Message : "+  Attack.original_msg) 
    # Attack.get_d()
    # Attack.implement(14)
