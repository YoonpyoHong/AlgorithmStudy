inputAr= input().split(" ")

x = int(inputAr[0])
y = int(inputAr[1])
w = int(inputAr[2])
h = int(inputAr[3])

print(min(min(x,w-x), min(y,h-y)))