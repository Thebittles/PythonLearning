

class Employee:
  def __init__(self, name, id, dept, title):
    self.__name = name
    self.__id = id
    self.__dept = dept
    self.__title = title

  def set_name(self, name):
    self.__name = name

  def set_id(self, id):
    self.__id = id
  
  def set_dept(self, dept):
   self.__dept = dept

  def get_name(self):
    return self.__name
     
  def get_id(self):
    return self.__id
     
  def get_dept(self):
    return self.__dept
     
  def get_title(self):
    return self.__title
     
     


     