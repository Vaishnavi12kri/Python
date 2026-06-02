tup = (2,1,3,1)
print(type(tup))
print(tup[0])
print(tup[1])
# tup[0] = 5  #this is not allowed in tuples because tuples are immutable
tup = ()
print(tup)
print(type(tup))

tup = (1)
print(tup)
print(type(tup))

tup = (1.0)
print(tup)
print(type(tup))

tup = ("hello")
print(tup)
print(type(tup))

tup = ("hello",)
print(tup)
print(type(tup))

tup = (1,2,3,4)
print(tup[1:3])