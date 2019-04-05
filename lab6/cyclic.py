class Cyclic_Attack:
    def __init__(self, e, N):
        self.e = e
        self.N = N
    
    def Attack(self,ele):
        res = pow(ele,self.e)%self.N
        it_count = 1
        g = ele
        while res != ele :
            g = res
            print("C" + str(it_count) + " : " + str(res))
            res = pow(res,self.e)%self.N
            it_count += 1
        # if it_count >1000:
            # return "infi"
        print("C" + str(it_count) + " : " + str(res))        
        return g

    def get_result(self,ipt):
        # result = []
        # while(len(ipt) <= 8 ):
        #     ipt += ' '
        # for ele in ipt:
        #     res = self.Attack(ord(ele))
        #     result.append(res)
        # self.get_plain(result)
        res = self.Attack(ipt)
        return res
        print( "Plaint Text is : " +  str(res) )

    
    def get_plain(self,ipt):
        # return ipt
        print("The Plain Text is : ",end="")
        for e in ipt :
            if e != "infi":
                print(chr(e) +" " ,end="")
            else:
                print("infi " , end = "")
        print("")

# def main():
#     # e = int(input("e : "))
#     # N = int(input("N : "))
#     # N = int(input("CT : "))
#     e = 5
#     N = 667
#     CT = 41
#     Attack = Cyclic_Attack(e,N)
#     Attack.get_result(CT)

# if __name__ == "__main__":
#     main()