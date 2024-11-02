# Code for class: Book

class Book:
    def __init__(self, title, author_id, isbn, publish_date):
        self.__title = title
        self.__author_id = author_id
        self.__isbn = isbn
        self.__publish_date = publish_date

    def get_title(self):
        return self.__title
    
    def get_author_id(self):
        return self.__author_id
    
    def get_isbn(self):
        return self.__isbn
    
    def get_publish_date(self):
        return self.__publish_date
    