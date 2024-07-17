# Q1
newlist = [i for i in range(5) if i >2]
print (newlist)
ints =set({1,1,2,3,3,34})
print(len(ints))

# Q2
d = {
    'a': 1
}
d['b'] = 2
print(d)

# Q3 
class Dog:
    def __init__(self):
        pass
    def bark(self):
        return "bark bark bark bark"
d = Dog()
print(d.bark())

# Q4
this_var = 30
def func():
    global this_var
    this_var = 20
    print(this_var)
print(this_var)
func()
print(this_var)

# Q5
w = 'python'
w_iterator = iter(w)
print(next(w_iterator))

# Q6
class Builiding:
    def __init__(self, number):
        self.number = number
b = Builiding(245)
print (b.number)

x = lambda: "I know"
print(x)


# Q7
for i in "hello":
    if i == "l":
        continue
    print(i)

# Q8
x = lambda: "I know how to call this function"
print(x())

# Q9

def greet(name,age):
    print (name)
    print(age)
print(greet("PP", 30))

# Q10
with open ('D:\Pradeep\Learning\CodingBat-Python\cat_data.txt') as file:
  text = file.read()
n = 0
for word in text.split():
  if word.lower() in ['cat','cats']:
    n += 1
print('Lewis has used the word "cat" {} times'.format(n))

