sizeFloppyDisk = float(1.44 * 1024 * 1024)
sizeBook = float(100 * 50 * 25 * 4)

bookCounter = int(sizeFloppyDisk // sizeBook)


print("Количество книг, помещающихся на дискету:", bookCounter)
