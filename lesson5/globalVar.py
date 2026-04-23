def funksioni():

    global name
    name = "andi"
    print(name)

funksioni()

def test():
    name = "lisa"
    print(name)

test()

shkolla="digitalschool"

def test2():
    global shkolla
    shkolla="harvard"

test2()
print(shkolla)


