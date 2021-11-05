list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("fileQ3.txt","w")
i=0
while i<len(list):
    f.write(list[i])
    f.write("\n")
    i=i+1

