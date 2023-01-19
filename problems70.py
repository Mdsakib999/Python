#Create a library management(Harry vai)

class Library:
    def  __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lend_dic = {}
    
    def display_book(self):
        print(f"we have following book in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def land_book(self, book, user):
        if book not in self.lend_dic.keys():
            self.lend_dic.update({book:user})
            print("Books has been updated")
        else:
            print(f"Book is not avilable {self.lend_dic[book]}")

    def add_book(self, book):
        self.booklist.append(book)
        print("Book has been added to the list")

        
    def return_book(self, book):
        self.booklist.remove(book)



if __name__ == '__main__':
    All_books = Library(['Python', 'physics', 'C++ book', 'Biology', 'JavaScript'])