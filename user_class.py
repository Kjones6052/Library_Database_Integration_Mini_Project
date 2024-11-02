# Code for class: User

class User: 
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id

    def get_user_name(self):
        return self.__name
    
    def get_user_id(self):
        return self.__library_id