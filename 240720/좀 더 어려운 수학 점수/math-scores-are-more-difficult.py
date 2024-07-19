math_a,eng_a=map(int,input().split())
math_b,eng_b=map(int,input().split())

if math_a>math_b:
    ans='A'
elif math_a<math_b:
    ans='B'
else:
    if eng_a>eng_b:
        ans='A'
    elif eng_a<eng_b:
        ans='B'

print(ans)