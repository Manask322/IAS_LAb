from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.files.storage import FileSystemStorage

from . import cyclic
from .import ECB_file,blind_file,chosen_file

def home(request):
    return render(request,'home.html')

def manual_entry(request):
    if request.method == 'POST':
        print(request.POST['name'] )
        print(request.POST['remark'])
        return render(request,'Home/home.html') 
    else:
        return render(request,'Home/home.html') 

def cyclic_attack(request):
    if request.method == 'POST':
        print(request.POST['e'] )
        print(request.POST['N'])
        e = int(request.POST["e"])
        N = int(request.POST["N"])
        CT = int(request.POST["CT"])
        Attack = cyclic.Cyclic_Attack(e,N)
        res = Attack.get_result(CT)
        print(res)
        print("dfdf")
        return render(request,'cyclic/output.html',{'res':res})
    else:
        return render(request,'cyclic/input.html')

    # ECB.main()
    return render(request,'home.html',{'address': address})

def ECB(request):
    address = "manas"
    if request.method == 'POST':
        DES = ECB_file.execute(request.POST['plainttext'],request.POST['roundkeys'])
        print(DES)
        res = DES
        l = range(0, 16)
        return render(request,'ECB/output.html',{'res':res,'l':l})
    else:
        return render(request,'ECB/input.html')

    # ECB.main()
    return render(request,'home.html',{'address': address})
    # return render(request,'dashboard.html',{'address': address})

def blind(request):
    if request.method == 'POST':
        msg = request.POST['msg']
        # e = int(input("Enter e :"))
        e = int(request.POST['e'])
        p = int(request.POST['p'])
        q = int(request.POST['q'])
        r = int(request.POST['r'])
        # r = int(input("Enter r :"))
        # p = int(input("Enter p :"))
        # q = int(input("Enter q :"))
        # N = int(input("Enter N :"))
        N = p*q
        Attack = blind_file.BlindAttack(msg,p,q,r,e,N)
        # print(Attack.get_text(20041))
        res = Attack.procedure()
        print( "Original Message : "+  Attack.original_msg)
        return render(request,'blind/output.html',{'res':res[1:],'l':Attack.original_msg,'block_size':res[0]})
    else:
        return render(request,'blind/input.html')

    return render(request,'home.html',{'address': address})
    f = 1

def chosen_cipher(request):
    if request.method == 'POST':
        msg = request.POST['msg']
        # e = int(input("Enter e :"))
        e = int(request.POST['e'])
        p = int(request.POST['p'])
        q = int(request.POST['q'])
        r = int(request.POST['r'])
        # r = int(input("Enter r :"))
        # p = int(input("Enter p :"))
        # q = int(input("Enter q :"))
        # N = int(input("Enter N :"))
        N = p*q
        Attack = chosen_file.BlindAttack(msg,p,q,r,e,N)
        # print(Attack.get_text(20041))
        res = Attack.procedure()
        print( "Original Message : "+  Attack.original_msg)
        return render(request,'cipher/output.html',{'res':res[1:],'l':Attack.original_msg,'block_size':res[0]})
    else:
        return render(request,'cipher/input.html')

    return render(request,'home.html',{'address': address})
        # msg = input("Enter Message : ")
    # inter_list.append(msg + " ")
    
    