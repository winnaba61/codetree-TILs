sum=0
cnt=0
while True:
    age=int(input())
    if 20<=age<30:
        cnt+=1
        sum+=age
    else:
        break

print(f"{(sum/cnt):.2f}")