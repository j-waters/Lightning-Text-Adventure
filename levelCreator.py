import easygui as eg
from functools import reduce

Spells = ["heal"]

def ConversationTree(tree={}):
    branch = []
    if tree == {}:
        tree = {"Conversation":{}, "Idle":{}}
    while True:
        if branch == []:
            cur = tree
        else:
            cur = reduce(lambda a, b: a[b], branch, tree)
        ch = []
        root = ""
        print("CUR:")
        print (cur)
        for key in cur:
            print(cur)
            print(key)
            ch.append(key + ": " + str(cur[key]))
        if branch == []:
            root = "Top Level"
            ch.clear()
            ch.append("Conversation Tree")
            ch.append("Random Idle Comments")
        else:
            ch.append("Add An Item...")
            for i in branch:
                root = root + "> " + i
            if ch > 1:
                ch.append("Delete An Item")
        a = ""
        s = eg.choicebox(msg=root, choices=ch)
        if s == "Add An Item...": #Adding an item - statement, action or option
            ckeys = [key for key in cur.items()]
            ch = ["Action", "Option", "Conditional"]
            if not branch == ['Conversation'] or branch == ['Idle'] or "B" in ckeys :
                ch.append("Button Text")
            if not "T" in ckeys:
                ch.append("Statement")

            a = eg.buttonbox(msg="Select type:", choices=ch)
            exists = False
        elif s == "Delete An Item":
            ch.remove("Add An Item...")
            ch.remove("Delete An Item")
            s = eg.choicebox(msg="Select An Item To Delete:", choices=ch)
            if not s == None:
                reduce(lambda a, b: a[b], branch, tree).pop(s.split(":")[0])
        else:
            if s == None:
                try:
                    reduce(lambda a, b: a[b], branch, tree).update(cur)
                    branch.pop(len(branch) - 1)
                    cur = {}
                except:
                    yn = eg.ynbox(msg="Do you want to finish editing?")
                    if yn == "Yes":
                        eg.codebox(msg="Finished Conversation Tree:", text=tree)
                    else:
                        branch = []
            elif s == "Conversation Tree":
                branch.append("Conversation")
                cur = cur["Conversation"]
            elif s == "Random Idle Comments":
                branch.append("Idle")
                cur = cur["Idle"]
            elif list(s.split(":")[0])[0] == "O":
                branch.append(s.split(":")[0])
                cur = cur[s.split(":")[0]]
            elif s.split(":")[0] == "T":
                a = "Statement"
                exists = True
                item = cur["T"]
            elif list(s.split(":")[0])[0] == "A":
                a = "Action"
                exists = True
                item = cur[s.split(":")[0]]
                number = list(s.split(":")[0])[1]
            print("split:")
            print(list(s.split(":")[0])[0])

        if a == "Statement":
            if exists:
                sta = item
            else:
                sta = [""]
            num = 0
            while True: #Statement loop
                maxnum = len(sta) - 1
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

                s = eg.buttonbox(msg="String " + str(num + 1) + " of " + str(len(sta)) + ":\n" + str(sta[num]), choices = ch)
                if s == "<---":
                    num -= 1
                if s == "--->":
                    num += 1
                if s == "Add String ->":
                    sta.append("")
                    maxnum = len(sta[num]) - 1
                    num +=1
                if s == "Edit":
                    e = eg.enterbox(msg="Edit the string:", default=sta[num])
                    sta[num] = e
                if s == "Back Up":
                    break
                if s == "Delete":
                    sta.pop(num)
                if num > maxnum:
                    num = 0
            cur["T"] = sta
        elif a == "Option":
            knum = 1
            while True:
                if "O" + str(knum) in cur:
                    knum +=1
                else:
                    break
            cur["O" + str(knum)] = {}
            eg.msgbox(msg="Added an extra branch")
            if s == "Button Text":
                cur["B"] = eg.enterbox(msg="Enter the text that will show on this branch's button:")
        elif a == "Action":
            print("Action")
            print(exists)
            if not exists:
                item = ""
                knum = 1
                while True:
                    if "A" + str(knum) in cur:
                        knum +=1
                    else:
                        break
            if exists:
                knum = number
            ch.clear()
            ch = ["Give Item", "Give Quest", "End Quest", "Battle"]

            s = eg.choicebox(msg="Choose An Action:", choices=ch)

            if s == "Give Item":
                print("give item")
                if exists and item[0] == "G":
                    t = item[1][2][0]

                ch = ["shirt", "helm", "boot", "book", "map", "weapon", "money", "npc", "item"]
                t = eg.choicebox(msg="Select The Item Type:", choices=ch)
                if exists:
                    addingItem = addItem(t, exists, item[1])
                if not exists:
                    addingItem = addItem(t, exists, "")
                cur["A" + str(knum)] = ("G", addingItem)

        print("TREE:")
        print(tree)

#TODO: Add rewards
#TODO: Add conditionals



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
    if name == None:
        name = ""
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
        if s == None:
            return
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
            items.append(("a shirt", "A nice shirt", ["shirt", 5, "i"]))
            s = eg.choicebox(msg="Select An Item:", choices=[x[0] for x in items])
            for t in range(0, len(items)):
                if items[t][0] == s:
                    s = items[t]

            if s == ["Add Another..."]:
                ch = ["shirt", "helm", "boot", "book", "map", "weapon", "money", "npc", "item"]
                t = eg.choicebox(msg="Select The Item Type:", choices=ch)
                exists = False
            else:
                t = s[2][0]
                exists = True

            print(t)
            print("printed")
            curRoom[0].append(addItem(t, exists, s))
            if exists:
                curRoom[0].remove(s)

def addItem(t, exists, s=""):
    print(s)
    if t == "shirt" or t == "helm":
        print("shirt / helm")
        if exists:
            e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Defence:"], values=[s[0], s[2][1]])
        else:
            e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Defence:"])
        nm = e[0]
        df = e[1]
        if df.isnumeric() == False:
            eg.msgbox(msg="The defence field must only contain numbers (or decimals). Consider editing this in the future.")
        if exists:
            ds = eg.enterbox(msg="Enter an item description:", default=s[1])
        else:
            ds = eg.enterbox(msg="Enter an item description:", default=str(df)+" Defence")
        pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
        if not pic == None:
            pic = pic.replace("\\Pics\\", "")
        print(pic)
        print(nm, ds, [t, df, "c", "i"], pic)
        return(nm, ds, [t, df, "c", "i"], pic)

    if t == "boot":
        e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Defence:", "Speed:"])
        nm = e[0]
        df = e[1]
        sd = e[2]
        if df.isnumeric() == False or sd.isnumeric() == False:
            eg.msgbox(msg="The defence and speed fields must only contain numbers (or decimals). Consider editing this in the future.")
        if exists:
            ds = eg.enterbox(msg="Enter an item description:", default=s[1])
        else:
            ds = eg.enterbox(msg="Enter an item description:", default=str(df)+" Defence, " + str(sd) + " Speed")
        pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
        if not pic == None:
            pic = pic.replace("\\Pics\\", "")
        print(pic)
        return(nm, ds, [t, df, sd, "c", "i"], pic)

    if t == "weapon":
        e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Damage:"])
        nm = e[0]
        dm = e[1]
        if dm.isnumeric() == False:
            eg.msgbox(msg="The damage field must only contain numbers (or decimals). Consider editing this in the future.")
        if exists:
            ds = eg.enterbox(msg="Enter an item description:", default=s[1])
        else:
            ds = eg.enterbox(msg="Enter an item description:", default=str(dm)+" Damage")
        pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
        if not pic == None:
            pic = pic.replace("\\Pics\\", "")
        print(pic)
        return(nm, ds, [t, dm, "i"], pic)

    if t == "money":
        e = eg.multenterbox(msg="Enter data:", fields=["Item Name:", "Amount:"], values=["A Pouch Of Money"])
        nm = e[0]
        am = e[1]
        if am.isnumeric() == False:
            eg.msgbox(msg="The amount field must only contain numbers, and no decimals. Consider editing this in the future.")
        if exists:
            ds = eg.enterbox(msg="Enter an item description:", default=s[1])
        else:
            ds = eg.enterbox(msg="Enter an item description:", default="A small pouch of money containing " + str(am)+" coins")
        pic = eg.fileopenbox(msg="Choose A Picture. Must be in a folder named \"Pics\" within the games root directory:", default="/Pics/*")
        if not pic == None:
            pic = pic.replace("\\Pics\\", "")
        return(nm, ds, [t, am, "i"], pic)

    if t == "npc":
        c = eg.buttonbox(msg="Edit NPC's stats or conversation tree?", choices=["Stats", "Conversation"])
        print("yes npc")
        if exists:
            c = eg.buttonbox(msg="Edit NPC's stats or conversation tree?", choices=["Stats", "Conversation"])
            if c == "Stats":
                e = eg.multenterbox(msg="Enter data:", fields=["NPC General Name (not real name):", "Description", "Real name:", "Attack:", "Defence:", "Health:", "Max health:", "Rank:", "Speed:", "Luck:", "Magic Strength:"], values=[s[4]["name"], s[1], s[4]["att"], s[4]["def"], s[4]["hlt"], s[4]["mhlt"], s[4]["rnk"], s[4]["aln"], s[4]["spd"], s[4]["lck"], s[4]["mgc"], s[4]["spl"]])
            if c == "Conversation":
                if len(s) == 6:
                    ConversationTree(s[5])
                else:
                    ConversationTree({})
        else:
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
        if not pic == None:
            pic = pic.replace("\\Pics\\", "")
        return(nm, ds, ["npc"], pic, {"name":rn, "att":at, "def":df, "hlt":hl, "mhlt":mh, "rnk":rk, "aln":al, "spd":sd, "lck":lk, "mgc":ms, "spl":sp})
        print((nm, ds, ["npc"], pic, {"name":rn, "att":at, "def":df, "hlt":hl, "mhlt":mh, "rnk":rk, "aln":al, "spd":sd, "lck":lk, "mgc":ms, "spl":sp}))
        eg.msgbox(msg="To add a conversation tree, edit this NPC later.")

    if t == "map":
        #TODO: Maps
        pass
    if t == "book":
        #TODO: Books
        pass



#begin()
ConversationTree()
print(places)