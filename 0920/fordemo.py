
for i in range(65,91):
    cnt = 0

    for j in chr(i):
        # line = chr(i)[:4]     
        if cnt == 5 & chr(i).isupper():
            print(chr(i).lower(),end="")
        else:
            print(chr(i),end="")
        if cnt == 5:
            cnt = 0
    cnt += 1
    print("cnt : ",cnt)

    # print(line,end="")