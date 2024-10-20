with open("masala2.txt") as f:
    matn = f.read()
    raqamlar =[]
    for i in matn.split(" "):
        if i.isdigit():
            raqamlar.append(str(i))

    if raqamlar == sorted(raqamlar, key = int):
        print("True")
    else:
        print("False")