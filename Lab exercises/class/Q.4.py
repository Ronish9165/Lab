a=65
for i in range(4):
    for j in range(4-i):
        print(chr(a),end=" ")
        a+=1
    print()