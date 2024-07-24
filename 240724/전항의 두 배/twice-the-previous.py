fst,snd=map(int,input().split())

arr=[0]*10
arr[0]=fst
arr[1]=snd

for i in range(2,10):
    arr[i]=arr[i-1]+2*arr[i-2]

for i in range(10):
    print(arr[i],end=' ')