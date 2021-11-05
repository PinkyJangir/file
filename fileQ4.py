f=open("alllist.txt","r")
for i in f:
    if "delhi" in i:
        f=open("Delhi.txt","a")
        f.write(i)
    if "shimla" in i:
        f=open("Shimla txt","a")
        f.write(i)
    if "Others" in i:
        f=open("others.txt","a")
        f.write(i)
    if "shimla" not in i and "delhi" not in i and "others" not in i:
        f=open("others.txt","a")
        f.write(i)
