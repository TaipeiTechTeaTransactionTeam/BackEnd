#發現Ｄｊａｎｇｏ開發環境本來就支援Ｐｙｔｈｏｎ，又寫了ｓｈ跟ｂａｔ的我，乾脆．．．．．．．．來個跨平台ＰＹ腳本

#使用方法 
    #python autoGit.py -參數(選填) commit名稱(選填)
    #或
    #python autoGit.py commit名稱(選填) -參數(選填)
    
    #可選Args說明
        #可用參數輸入，不輸入程式執行會循問commitName
        #減號參數不填=add+commit+push全做
        
    #參數 減開頭 (一般順序 add->commit->push)
        # -a : add
        # -c : commit
        # -p : push
        # 可以減號後方多個英文字母
        # e.g. -acp,-ap,-cp...
        # 第二碼為~或者-表示前面的動作也要做
        # --p, -~p : -acp , add+commit+push
        # --c, -~c : -ac , add+commit

#注意
    #會產生記錄檔branch.log紀錄是否切換branch，保障不亂推送到別人的分支

from subprocess import getoutput
from sys import argv 
BranchCheckLogPath="./branch.log"
def add():
    getoutput("git add .")
    getoutput("git reset HEAD manage.py")
def commit():
    def getCommitName():
        args=[x for x in argv if x[0]!="-"]
        commitName=""
        if(len(args)==1):#NO input argv Only path
            commitName=input("Please input a commit name\n> ")
        elif(len(args)==2):#Only commit name with "" or one word
            commitName=args[1]
        else:
            for i in range(1,len(args)-1):
                commitName += args[i] + " "
            commitName += args[len(args)-1]
        commitName="\""+commitName+"\""
        return commitName
    commitName=getCommitName()
    try:
        print(getoutput("git commit -m "+commitName))
    except:
        pass
def isChangeBranch(branch):
    lastBranch=branch
    try:
        bf=open(BranchCheckLogPath,"rt")
        lastBranch=bf.readline()
    except:
        pass
    else:
        bf.close()
    try:
        f=open(BranchCheckLogPath,'wt')
        f.write(branch)
    finally:
        f.close()
    return not lastBranch==branch
def push():
    branchName = [x for x in getoutput("git branch").split("\n") if x[0]=="*"][0][2:]
    if(isChangeBranch(branchName)):
        if(input("<Warning!!!> You change the different branch, are you sure that you want to push the changes to \""+branchName+"\" (y/n)\n> ") in ["n","N"]):
            return
    try:
        print(getoutput("git push origin "+branchName))
    except:
        pass
def step(op):
    ops={"a":add,"c":commit,"p":push}
    ops[op]()
def argsJudge():
    priority="acp"
    args=[x[1:] for x in argv if x[0]=="-"]
    finalSet = set()
    for item in args:
        if(item[0]=="~" or item[0]=="-"):
            item=priority[:priority.index(item[1])]+item[1:]
        finalSet |= set(item)
    finalSet &= set(priority)
    if(finalSet==set("")):
        finalSet=set("acp")
    steps = [x for x in priority if x in finalSet]
    #print("steps : ",end='')
   # print(steps)
    for op in steps:
        step(op)
argsJudge()