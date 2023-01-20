f = open("../data/1880-boys.txt")
boys = f.read()

f = open("../data/1880-girls.txt")
girls = f.read()

f2 = open("../data/girls-boys.txt","w")
f2.write(boys + "\n" + girls)