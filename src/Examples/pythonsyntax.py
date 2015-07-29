# Richie Python Syntax Example

# ----- ASSIGNMENT -----
print("-----ASSIGNMENT-----")
a = 3
b = "hello"
c = "hi" + str(3) + "there" # use str() to match datatypes
d = 7
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(a + d)

# ----- IF STATEMENTS -----
print("\r\n\r\n-----IF STATEMENTS-----")
a = 5
b = 10
c = 5
if a == c:
    print("A equals C")
if a < b:
    print("A is less than B")
if b > a:
    print("B is more than A")
if b >= a:
    print("B is more or equal to A")

if a <= b:
    print("A is less or equal to B")
else:
    print("A is not less or equal to B")

# ----- LOOPS -----
print("\r\n\r\n-----LOOPS-----")
for i in range(10):
    print(i)

print("\r\nexample #2")
for i in range(4,10):
    print(i)

print("\r\nexample #3")
for i in ["hello", "how", "are", "you"]:
    print(i)

print("\r\nexample #4")
i = 1
while i < 10:
    i += 1
    print(i)

print("\r\nexample #5")
i = 1
while True:
    i += 1
    print(i)
    if i > 10:
        break

# ----- FUNCTIONS -----
print("\r\n\r\n-----FUNCTIONS-----")
def hello():
    def world():
        print("world")
    print("hello")
    world()
hello()

print("\r\nexample #2")
print("exception is rased here as world is not accessable in this scope")
print("I catch the exception with try, except so the whole program does not explode!")
try:
    world()
except Exception as e:
    print(e)

# ----- LISTS (very powerful arrays) -----
print("\r\n\r\n-----LISTS-----")
l1 = [1, 2, 3, "hello", "test"]
l2 = [[1, 1], [2,3], [5,7]]
print(l1[0])
print("\r\nexample #2")
print(l1[-1])
print("\r\nexample #3")
print(l1[4])
print("\r\nexample #4")
for i in l1:
    print(i)
print("\r\nexample #5")
print(l2)

# ----- Dictionary (map x to y) -----
print("\r\n\r\n-----DICTIONARYS-----")
mydict = {}
mydict["hello"] = "world"
mydict["world"] = "hi"
mydict["hello"] = "there"
print(mydict)

print("\r\nexample #2")
mydict = {"hello":"world", "hi":"there"}
print(mydict)
