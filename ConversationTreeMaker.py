import easygui
def make():
    tree= {}

    c = easygui.multenterbox(msg="Top level:", fields=["Text String", "Reward", "Option1", "Option2", "Option3", "Option4"])

    tree["T"] = c[0]
    del c[0]
    tree["R"] = c[0]
    del c[0]
    num = 0
    for i in c:
        if not i == "":
            num +=1
            tree["O" + str(num)] = {"B" : i}
    print(tree)

    for key in tree.keys():
        if not key == "T":
            c = easygui.multenterbox(msg=tree[key], fields=["Text String", "Option1", "Option2", "Option3", "Option4"])
            if c == None:
                break

            if not c[0] == "":
                tree[key]["T"] = c[0]
            del c[0]
            if not c[0] == "":
                tree[key]["R"] = c[0]
            del c[0]
            num = 0
            for i in c:
                if not i == "":
                    num +=1
                    tree[key]["O" + str(num)] = i

    print(tree)

def printTree(tree, depth = 0):
    if tree == None or len(tree) == 0:
        print ("\t" * depth, "-")
    if type(tree) == str:
        print ("\t" * depth, tree)
    else:
        for key, val in tree.items():
            print ("\t" * depth, key)
            printTree(val, depth+1)