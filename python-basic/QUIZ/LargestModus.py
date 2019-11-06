def main():
    modus = None
    num = []
    length = int(input("Length : "))
    for i in range(0, length):
        n = int(input())
        num.append(n)

    print(num)
    appearence = 1

    for i in num:
        n = 0
        for j in num:
            if i == j and i != modus:
                n += 1
        if n >= appearence and n != 1:
            appearence = n
            modus = i if modus is None else i if i > modus else modus
    print("Largest Modus %s" % modus if modus != None else "Tidak Ada Modus")


if __name__ == "__main__":
    main()
