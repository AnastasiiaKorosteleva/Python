__author__ = 'anastasiiakorosteleva'
a = input()
n = int(input())
if a == 'утюг':
    if n==1 or (((n-11)%10)==0 and ((n-11)%100)!=0):
        print(n,'утюг')
    elif n==2 or n==3 or n==4 or (((n-2)%10==0) and ((n-12)%100)!=0) or (((n-3)%10==0) and ((n-13)%100)!=0) \
    or (((n-4)%10==0) and ((n-14)%100)!=0):
        print (n,'утюга')
    else:
        print (n,'утюгов')
if a == 'ложка':
    if n==1 or (((n-11)%10)==0 and ((n-11)%100)!=0):
        print(n,'ложка')
    elif n==2 or n==3 or n==4 or (((n-2)%10==0) and ((n-12)%100)!=0) or (((n-3)%10==0) and ((n-13)%100)!=0) \
    or (((n-4)%10==0) and ((n-14)%100)!=0):
        print (n,'ложки')
    else:
        print (n,'ложек')