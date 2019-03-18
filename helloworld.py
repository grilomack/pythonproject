
An=input("无序整数数组A[n]:")
An=An.split(" ")
An=[int(An[i]) for i in range(len(An))]
An.sort()
n=len(An)-1
An1=An[n]
if An1<0:
    An2=An[n-1]
    An3=An[n-2]
    print(An1*An2*An3)
elif An1==0:
    print(0)
elif An1>0 and An[n-2]>0:
    print(An1*An[n-1]*An[n-2])
elif An1>0 and An[n-2]<=0:
    print(An[0]*An[1]*An1)





