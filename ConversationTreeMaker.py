import easygui

tree= {}

c = easygui.multenterbox(msg="Top level:", fields=["Text String", "Option1", "Option2", "Option3", "Option4"])

tree["T"] = c[0]
del c[0]
num = 0
for i in c:
    if not i == "":
        num +=1
        tree["O" + str(num)] = i
print(tree)

for key in tree.keys():
    if not key == "T":
        c = easygui.multenterbox(msg=tree[key], fields=["Text String", "Option1", "Option2", "Option3", "Option4"])
        if c == None:
            break

        tree[key]["T"] = c[0]
        del c[0]
        num = 0
        for i in c:
            if not i == "":
                num +=1
                tree[key]["O" + str(num)] = i

print(tree)