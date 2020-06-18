class Person:
  __name = "Nmae 1"
  __age = 0

  def __init__(self, sex):
    self.sex = sex

  @property
  def sex(self):
    return self.__sex

  @sex.setter
  def sex(self, sex):
    self.__sex = sex

  def getSex(self):
    return self.__sex

  def set(self, name, age):
    self.__age = age
    self.__name = name

  def getName (self):
    return self.__name

  def getAge (self):
    return self.__age
  