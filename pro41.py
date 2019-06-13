v1,k1=input().split()

v1=int(v1)

k1=int(k1)

s1=''

u=2

if(v1+k1<=3):

    for i in range(0,v1+k1):

        if(i%2!=0):

            s1=s1+'0'

        else:

            s1=s1+'1'

else:    

    for i in range(0,v1+k1):

        if(i==u):

            s1=s1+'0'

            if(u==k1):

                u=u+2

            else:

                u=u+3

        else:

            s1=s1+'1'

x=len(s1)-1

if(int(s1[x])==0):

    print('-1')

elif v1==1 and k1==2: print("011")

else:

    print(s1)
