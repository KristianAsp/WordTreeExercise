from src.WordTree import WordTree

t = WordTree()
t.add("car"); t.add("can"); t.add("cat"); t.add("cat"); t.add("cat")
print("1: ",t.count("ca"),t.count("can"),t.count("car"),t.count("cat"),t.minst())
print(t, t.size)
# t.remove("")
print(t, t.size)
t.add("")
print(t, t.size)
t.add("ca")
print("2: ",t.count("ca"),t.count("can"),t.count("car"),t.count("cat"),t.minst())
print(t, t.size)
# t.remove("car")
# print("3: ",t.count("ca"),t.count("can"),t.count("car"),t.count("cat"),t.minst()) print(t, t.size)
# t.remove("cat"); t.remove("cat"); t.remove("cat")
# print("4: ",t.count("ca"),t.count("can"),t.count("car"),t.count("cat"),t.minst()) print(t, t.size)
# t.remove("ca"); t.add("car")
# print("5: ",t.count("ca"),t.count("can"),t.count("car"),t.count("cat"),t.minst()) print(t, t.size)