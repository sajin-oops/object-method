'''
                                OBJECT METHODS
Objects can also contain methods. Methods in objects are functions that belong to the object.
'''

class new:
  def __init__(self,name,role):
    self.name = name
    self.role = role
  def myfunc(self):
    print("Hello my name is " + self.name)
    print("My Designation is " + self.role)

obj = new("Sajin","Data scientist")
obj.myfunc()

# O/P 
'''
Hello my name is Sajin
My Designation is Data scientist
'''