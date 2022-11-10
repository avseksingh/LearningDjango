class Book:
    def __init__(self,bookname,subject,price):
        self.bookname=bookname
        self.subject=subject
        self.price=price

    def __str__(self) -> str:
        return "Book Name={0},Subject={1},Price={2}".format(self.bookname,self.subject,self.price)
