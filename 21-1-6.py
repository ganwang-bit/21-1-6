a=input()
b=a.split()
maxn=b[0]
minn=b[0]
for i in b:
    if i>maxn:
        maxn=i
    if i<minn:
        minn=i
print(maxn)
print(minn)
