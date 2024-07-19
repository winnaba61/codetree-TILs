h,w=map(int,input().split())
b=10000*w/(h*h)
print(f"{b:.1f}")
if b>=25:
    print("Obesity")