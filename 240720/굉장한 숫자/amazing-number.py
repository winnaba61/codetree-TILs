n=int(input())
if (n%2!=0 and n%3==0) or (n%2==0 and n%5==0):
    n=1
else:
    n=0
print(n)