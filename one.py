# i=1
# biao=0
# while i>0:
#     if i==5:
#         biao=1
#     m=0
#     while m<i:
#         print("*",end=' ')
#         m=m+1
#     print()
#     if biao==1:
#         i=i-1
#     else:
#         i=i+1

# a=[1,2,32,4,5,23,14,67,43]
# print(a)
# print(max(a))
# print(min(a))

# a='guanhao'
# print(a)
# a=a+'lcy'
# print(a)


# a='hello world'
# count={}
# for i in range(len(a)):
#     if a[i] not in count:
#         count[a[i]]=1
#     else:
#         count[a[i]]+=1
# for key,value in count.items():
#     if key==' ':
#         print('空格:'+str(value),end=' ')
#     else:
#         print(key+':'+str(value),end=' ')
# for key ,value in count.items():
#     print(key+':',end='')
#     print(value,end=' ')
# print()


i=1
while i<10:
    j=1;
    while j<=i:
        print(str(j)+'*'+str(i)+'=',end='')
        print(j*i,end='  ')
        j+=1
    print()
    i+=1


