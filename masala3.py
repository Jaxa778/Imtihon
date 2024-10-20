class Book:
    def __init__(self,name,count_pages,price):
        self.name = name
        self.count_pages = count_pages
        self.price = price

    def pageMidlePrice(self):
        print(f"{self.name} kitobining bitta saxifasining o`rtacha narxi {self.price//self.count_pages} so`m")

    def updateProgrammingBook(self):
        if "Programming" in self.name:
            self.price *= 2
        else:
            print("Yo'q!!! To'g'ri tushuning bu kitob Programming haqida emas.")

    def bookInfo(self):
        print(f"""
              Nomi = {self.name}
              Saxifasi = {self.count_pages} bet
              Narxi = {self.price} so'm""")

kitob1 = Book("O'tkir Hoshimov asarlari", 336, 50000)
kitob2 = Book("Ichingdagi ichingdadir", 240, 30000)
kitob3 = Book("O`yla va boy bo`l", 144, 35000)
kitob4 = Book("Yetti majlis", 300, 35000)
kitob5 = Book("Python Programming", 450, 50000)

kitob1.bookInfo()
kitob3.pageMidlePrice()
kitob5.updateProgrammingBook()
kitob5.bookInfo()