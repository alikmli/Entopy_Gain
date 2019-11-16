
import math

def Entropy(*arg):
    arg=arg[0]
    total=sum(arg)
    result=0

    if 0 in arg:
        return  0
    for item in arg:
        result += -1 * (item/total) * math.log2(item/total)

    return result

def Gain(S,br):
   Ens=Entropy(S)
   sum_S=sum(S)
   print('Entropy(S)=',Ens)

   total=0
   counter=1
   for item in br:
       sum_br=sum(item)
       w=sum_br / sum_S
       En=Entropy(item)
       print('Entropy(Branch#{0}) = {1}'.format(counter,En))
       total += w*En
       counter+=1

   return Ens - total

if __name__ == "__main__":
    length=int(input('Enter The Number of target function dimens :'))
    S=list()
    items = list()
    for i in range(0,length):
        S.append(int(input()))

    brnchs=int(input('Enter Number of Branch : '))


    for i in range(0,brnchs):
       print('Enter items for branch# ',i+1)
       item=list()
       for k in range(0,length):
           item.append(int(input()))
       items.append(item)
       del item


    print('Gain is : ' ,Gain(S,items))