import easygui
from lightCore import printTree
def make():
    global tree
    tree= {}

    c = easygui.multenterbox(msg="Top level:", fields=["Text String", "Reward", "Option1", "Option2", "Option3", "Option4"])

    tree["T"] = c[0]
    del c[0]
    if not c[0] == "":
        tree["R"] = c[0]
    del c[0]
    num = 0
    for i in c:
        if not i == "":
            num +=1
            tree["O" + str(num)] = {"B" : i}
    print(tree)

    while True:
        ops = []
        for key in tree:
            ops.append(key + ": " + str(tree[key]))
        c = easygui.choicebox(msg="Select Branch To Edit:", choices=ops)
        o = easygui.buttonbox(msg="Edit, end, or continue down branch?", choices=("Continue", "Edit", "End"))
        if o == "Edit":
            branch = c.split(":")[0]
            print(branch)
            c = easygui.multenterbox(msg=tree[branch], fields=["Text String", "Reward", "Option1", "Option2", "Option3", "Option4"])
            tree[branch]["T"] = c[0]
            del c[0]
            if not c[0] == "":
                tree[branch]["R"] = c[0]
            del c[0]
            num = 0
            if not c == []:
                for i in c:
                    if not i == "":
                        num +=1
                        tree[branch]["O" + str(num)] = {"B" : i}
            else:
                if not tree[branch]["T"] == "":
                    string = []
                    string.append(tree[branch]["T"])
                    tree[branch]["O1"] = "..."
                    while True:
                        s = easygui.enterbox(msg="Continue Writing:")
                        if not s == None:
                            string.append(s)
                        if s == None:
                            tree[branch]["T"] = string
                            break


            print(tree)
        if o == "End":
            branch = c.split(":")[0]
            route = []
            curtree = tree
            while True:
                ops = []
                for key in curtree:
                    ops.append(key + ": " + str(curtree[key]))
                c = easygui.choicebox(msg="Select Branch To Go To:", choices=ops)
                route.append(c.split(":")[0])
                o = easygui.buttonbox(msg="Select or Continue?", choices=("Select", "Continue"))
                if o == "Select":
                    tree[branch]["E"] = route
                    break
                if o == "Continue":
                    curtree = curtree[c]





make()
printTree(tree)
print(tree)