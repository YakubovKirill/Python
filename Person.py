class Person:
  __name = "Nmae 1"
  __age = 0

  def set(self, name, age):
    self.__age = age
    self.__name = name

  def getName (self):
    return self.__name

  def getAge (self):
    return self.__age
  