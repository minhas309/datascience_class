x=10
typeof(x)
print("Hello                        1", "World")
x = "This is Data Science Class"
print(type(x))
def func(x,y):
    return x+y

print(func(18, 5))
x = lambda x: x*5
print(x('ha'))
x = lambda x: x*5
seq = ["ha","he","hi"]
print(x(seq))
x = lambda x, y: x+y
print(x('ha','he'))
#tuple

tup = 4,5,6,7
print(tup)
#tuple

tup = 4,5,6,7
print(type(tup))
#tuple

tup = 4,5,6,7
a,b,c,d = tup
print(a,b,c,d)
#tuple

tup = (4,5,6,7), (2,3)
a,b = tup
c,d,e,f=a
print(f)
#tuple

tup = (4,5,6,7), (4,5)
#print(tup)
seq = []
#unpack tuple
for i,value in enumerate(tup):
    #print(value)
    seq.append(value)
    
print(len(seq))
#tuple

tup = (4,5,6,7)
tup2 = (4,5)
tup3 = tuple(zip(tup,tup2))

    
print(tup3)
#tuple

tup = (4,5,6,7), (4,5)
#print(tup)
seq = []
#unpack tuple
for i,value in enumerate(tup):
    print(i)
    
#list
courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.append("SRE")
print(courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)
courses.pop()
print(courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)
courses.pop(1)
print(courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)
courses.remove("SRE")
print(courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)
for course in courses:
    if(len(course) > 15):
        print(course)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)

print([course for course in courses if len(course)>15])
#list

courses = ["Data Science", "Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)
for course in courses:
    if(len(course) > 15):
        print(course)
        for value in course:
            print(value)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)

print([value for value in course for course in courses if len(course)>15])
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)

#list[start:stop:step]
print(courses[::-2])
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)

#list[start:stop:step]
print(list(reversed(courses)))
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)

print("Data Science" in courses)
#list

courses = ["Data Science", " Advanced Programming", "intro to SE"]
print(courses)
courses.insert(1,"SRE")
print(courses)

print(" " in courses)
#DICTIONARY

d={12:'Abdullah', 420:'Ahzam', 421:'Haseeb chillz'}
d2={420:'Ahzam', 421:'Haseeb chillz'}
d2.update(d)
print(d2)

#DICTIONARY

courses = ["Data Science", " Advanced Programming", "intro to SE"]
courseCode = {'CS4048', 'CS4043','SE1001', 'SE2002'}
course2 = dict(zip(courseCode,courses))

print(course2)
