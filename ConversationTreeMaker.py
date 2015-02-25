import easygui
from functools import reduce
global tree
def make(tree={}):
    cur = tree
    branch = []
    while True:
        if cur == tree:
            print("CUR == TREE")
        if cur == {}:
            o = "Edit"

        if not cur == {}:
            print("cur not {}")
            ops = []
            for key in cur:
                print("For " + str(key))
                ops.append(key + ": " + str(cur[key]))
            print("OPS: " + str(ops))
            c = easygui.choicebox(msg="Select Branch To Edit:", choices=ops)
            if c == None:
                if cur == tree:
                    ex = easygui.buttonbox(msg="Exit?", choices=("Yes", "No"))
                    if ex == "Yes":
                        easygui.codebox(msg="Completed Code:", text=tree)
                        return
                    else:
                        o = "Back To Top"
                else:
                    o = "Back To Top"
            else:
                o = easygui.buttonbox(msg="Edit, end, or continue down branch?", choices=("Back To Top", "Continue", "Edit", "End"))
                branch.append(c.split(":")[0])
                cur = cur[c.split(":")[0]]


        if o == "Edit":
            if not cur == tree:
                curmsg = str(cur)
            if cur == tree:
                curmsg = "Top Level"
            c = easygui.multenterbox(msg=curmsg, fields=["Text String", "Reward", "Option1", "Option2", "Option3", "Option4"])
            if not c == None:
                cur["T"] = c[0]
                del c[0]
                if not c[0] == "":
                    cur["R"] = c[0]
                del c[0]
                num = 0
                print("C: " + str(c))
                if not c == ['', '', '', '']:
                    for i in c:
                        if not i == "":
                            num +=1
                            cur["O" + str(num)] = {"B" : i}
                else:
                    if not cur["T"] == "":
                        text = []
                        text.append(cur["T"])
                        cur["O1"] = {"B" : "..."}
                        while True:
                            s = easygui.enterbox(msg="Continue Writing:")
                            if not s == None:
                                text.append(s)
                            if s == None:
                                cur["T"] = text
                                break

        if o == "End":
            route = []
            curtree = tree
            while True:
                end = easygui.buttonbox(msg="Goto branch, or end conversation?", choices=("End", "GoTo"))
                if end == "GoTo":
                    ops = []
                    for key in curtree:
                        ops.append(key + ": " + str(curtree[key]))
                    c = easygui.choicebox(msg="Select Branch To Go To:", choices=ops)
                    route.append(c.split(":")[0])
                    o = easygui.buttonbox(msg="Select or Continue?", choices=("Select", "Continue"))
                    if o == "Select":
                        cur["E"] = route
                        break
                    if o == "Continue":
                        curtree = curtree[c]
                if end == "End":
                    cur["E"] = "END"
        if o == "Continue":
            pass

        if o == "Back To Top":
            cur = tree
            branch = []


        print("TREE: " + str(tree))
        print("CUR: " + str(cur))
        print("BRANCH: " + str(branch))
        print("reduced tree: " + str(reduce(lambda a, b: a[b], branch, tree)))
        reduce(lambda a, b: a[b], branch, tree).update(cur)
        easygui.codebox(msg="Current Tree:", title="Tree Maker", text=str(tree))
        printTree(tree)
        print(tree)



# TODO: Redo all of this stuff to make it work with cur (almost done)
def printTree(tree, depth = 0):
    if tree == None or len(tree) == 0:
        print ("\t" * depth + "-")
    elif type(tree) == str:
        print ("\t" * depth + tree)
    elif type(tree) == list:
        print ("\t" * depth + str(tree))
    else:
        for key, val in tree.items():
            print ("\t" * depth + key)
            printTree(val, depth+1)

make()
printTree(tree)

