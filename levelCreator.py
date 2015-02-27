import easygui as eg
from functools import reduce

Spells = ["heal"]

def conversationTree(tree={}):
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
            c = eg.choicebox(msg="Select Branch To Edit:", choices=ops)
            if c == None:
                if cur == tree:
                    ex = eg.buttonbox(msg="Exit?", choices=("Yes", "No"))
                    if ex == "Yes":
                        eg.codebox(msg="Completed Code:", text=tree)
                        return tree
                    else:
                        o = "Back To Top"
                else:
                    o = "Back To Top"
            else:
                o = eg.buttonbox(msg="Edit, end, or continue down branch?", choices=("Back To Top", "Continue", "Edit", "End"))
                branch.append(c.split(":")[0])
                cur = cur[c.split(":")[0]]


        if o == "Edit":
            if not cur == tree:
                curmsg = str(cur)
            if cur == tree:
                curmsg = "Top Level"
            c = eg.multenterbox(msg=curmsg, fields=["Text String", "Reward", "Option1", "Option2", "Option3", "Option4"])
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
                            s = eg.enterbox(msg="Continue Writing:")
                            if not s == None:
                                text.append(s)
                            if s == None:
                                cur["T"] = text
                                break

        if o == "End":
            route = []
            curtree = tree
            while True:
                end = eg.buttonbox(msg="Goto branch, or end conversation?", choices=("End", "GoTo"))
                if end == "GoTo":
                    ops = []
                    for key in curtree:
                        ops.append(key + ": " + str(curtree[key]))
                    c = eg.choicebox(msg="Select Branch To Go To:", choices=ops)
                    route.append(c.split(":")[0])
                    o = eg.buttonbox(msg="Select or Continue?", choices=("Select", "Continue"))
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
        eg.codebox(msg="Current Tree:", title="Tree Maker", text=str(tree))
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

#conversationTree()
#printTree(tree)


def begin():
    global places
    places = {}
    name = eg.enterbox(msg="Type the first place name:")
    places[name] = [[],[]]
    viewRoot()

def viewRoot():
    global curRoom
    print(places)
    print(places.keys())
    rooms = [key for key in places]
    s = eg.choicebox(msg="Select a place:", choices=rooms)
    curRoom = places[s]
    editRoom()

def editRoom():
    while True:
        s = eg.buttonbox(msg="Editing Room", choices=["Edit Items", "Edit Story"])
        if s == "Edit Story":
            if curRoom[1] == []:
                curRoom[1].append("")
            num = 0
            while True:
                maxnum = len(curRoom[1]) - 1
                ch = []
                if num > 0:
                    ch.append("<---")
                ch.append("Edit")
                ch.append("Delete")
                ch.append("Back Up")
                if num < maxnum:
                    ch.append("--->")
                if num == maxnum:
                    ch.append("Add String ->")

                s = eg.buttonbox(msg="String " + str(num + 1) + " of " + str(len(curRoom[1])) + ":\n" + str(curRoom[1][num]), choices = ch)
                if s == "<---":
                    num -= 1
                if s == "--->":
                    num += 1
                if s == "Add String ->":
                    curRoom[1].append("")
                    maxnum = len(curRoom[1][num]) - 1
                    num +=1
                if s == "Edit":
                    e = eg.enterbox(msg="Edit the string:", default=curRoom[1][num])
                    curRoom[1][num] = e
                if s == "Back":
                    break
                if s == "Delete":
                    curRoom[1].pop(num)
                if num > maxnum:
                    num = 0
            curRoom[1].remove("")
        if s == "Edit Items":
            items = curRoom[0]
            items.append(["Add Another..."])
            s = eg.choicebox(msg="Select An Item:", choices=[x[0] for x in items])
            for t in range(0, len(items)):
                if items[t][0] == s:
                    s = items[t]

            if s == ["Add Another..."]:
                ch = ["shirt", "helm", "boot", "book", "map", "weapon", "money", "npc", "item"]
                s = eg.choicebox(msg="Select The Item Type:", choices=ch)
                if s == "shirt" or "helm":
                    e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Defence:"])
                    nm = e[0]
                    df = e[1]
                    if df.isnumeric() == False:
                        eg.msgbox(msg="The defence field must only contain numbers (or decimals). Consider editing this in the future.")
                    ds = eg.enterbox(msg="Enter an item description:", default=str(df)+" Defence")
                    pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
                    pic = pic.replace("\\Pics\\", "")
                    print(pic)
                    curRoom[0].append((nm, ds, [s, df, "c", "i"], pic))
                if s == "boot":
                    e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Defence:", "Speed:"])
                    nm = e[0]
                    df = e[1]
                    sd = e[2]
                    if df.isnumeric() == False or sd.isnumeric() == False:
                        eg.msgbox(msg="The defence and speed fields must only contain numbers (or decimals). Consider editing this in the future.")
                    ds = eg.enterbox(msg="Enter an item description:", default=str(df)+" Defence, " + str(sd) + " Speed")
                    pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
                    pic = pic.replace("\\Pics\\", "")
                    print(pic)
                    curRoom[0].append((nm, ds, [s, df, sd, "c", "i"], pic))
                if s == "weapon":
                    e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Damage:"])
                    nm = e[0]
                    dm = e[1]
                    if dm.isnumeric() == False:
                        eg.msgbox(msg="The damage field must only contain numbers (or decimals). Consider editing this in the future.")
                    ds = eg.enterbox(msg="Enter an item description:", default=str(dm)+" Damage")
                    pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
                    pic = pic.replace("\\Pics\\", "")
                    print(pic)
                    curRoom[0].append((nm, ds, [s, dm, "i"], pic))
                if s == "money":
                    e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Amount:"], values=["A Pouch Of Money"])
                    nm = e[0]
                    am = e[1]
                    if am.isnumeric() == False:
                        eg.msgbox(msg="The amount field must only contain numbers, and no decimals. Consider editing this in the future.")
                    ds = eg.enterbox(msg="Enter an item description:", default="A small pouch of money containing" + str(dm)+" coins")
                    pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
                    pic = pic.replace("\\Pics\\", "")
                    curRoom[0].append((nm, ds, [s, am, "i"], pic))
                if s == "npc":
                    e = eg.multenterbox(msg="Enter data:", fields=["NPC General Name (not real name):", "Description", "Real name:", "Attack:", "Defence:", "Health:", "Max health:", "Rank:", "Speed:", "Luck:", "Magic Strength:"])
                    nm = e[0]
                    ds = e[1]
                    rn = e[2]
                    at = e[3]
                    df = e[4]
                    hl = e[5]
                    mh = e[6]
                    rk = e[7]
                    sd = e[8]
                    lk = e[9]
                    ms = e[10]
                    sp = eg.multchoicebox(msg="Select Spells:", choices=Spells)
                    al = eg.buttonbox(msg="Alignment: G(ood) or E(vil)", choices=["G", "E"])
                    pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
                    pic = pic.replace("\\Pics\\", "")
                    curRoom[0].append((nm, ds, ["npc"], pic, {"name":rn, "att":at, "def":df, "hlt":hl, "mhlt":mh, "rnk":rk, "aln":al, "spd":sd, "lck":lk, "mgc":ms, "spl":sp}))
                    eg.msgbox(msg="To add a conversation tree, edit this NPC later.")


begin()
print(places)