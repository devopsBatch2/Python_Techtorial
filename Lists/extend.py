
need = ["pencil","eraser","notebook"]
need2 = ("computer","mouse","keybord","camera")

need.extend(need2)
print(need)

# what happens if you extend list with string
str = "Techtorial"
str.upper()
print(str)


list = [1,2,3,4,5]

list.extend(str)
print(list)

#extend method only works with itersble objects

list.extend(1234)  # it will create an error
print(list)
