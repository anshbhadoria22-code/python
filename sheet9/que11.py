def fun1():
  name ="Suyash"
  def fun2():
    nonlocal name
    name ="Chaudhary"
  fun2()
  print(name)
fun1()

#output:# Chaudhary
 