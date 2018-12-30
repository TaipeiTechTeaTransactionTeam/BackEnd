import MySQLdb
from pathlib import Path
import shutil
import os
from subprocess import getoutput
def readDBcnf():
    fileName="./my.cnf"
    if(Path(fileName).is_file()):
        f= open(fileName,"r")
        content=f.read(-1)
        content=content.replace(" ","")
        lines=content.split("\n")
        def getVal(atrr):
            return [x.split("=")[1] for x in lines if x.split("=")[0]==atrr] [0]
        user=getVal("user")
        password=getVal("password")
        f.close()
        return user,password
    else:
        print("沒有my.cnf無法使用資料庫")
        if(input("使用locaSetup並繼續(y/n)\n> ")=="y"):
            os.system("python localSetup")
            return readDBcnf()
        else:
            exit()
def rmMigrations():
    path="storeApp/migrations"
    shutil.rmtree(path, ignore_errors=True)
    print("刪除 "+path)
def createMigrations():
    try:
        print(getoutput("python manage.py makemigrations storeApp"))
    except:
        pass
    try:
        print(getoutput("python manage.py migrate"))
    except:
        pass
def sql():
    user,pwd=readDBcnf()
    db  =  MySQLdb . connect ( 
     host = "localhost" ,     #主機名
     user = user ,          #用戶名
     passwd = pwd,   #密碼
       charset='utf8',
    )         #數據庫名稱

    #查詢前，必須先獲取游標
    cur  =  db . cursor ()
    try:
        cur.execute("drop database TTTS")
        print("刪除DB TTTS")
    except:
        pass
    try:
        cur.execute("CREATE DATABASE TTTS CHARACTER SET utf8 COLLATE utf8_general_ci;")
        print("建立utf8 DB TTTS")
    except:
        pass
    db.commit()
    db.close()
def loadSqlDatas():
    if input("是否載入sql預設資料?(y/n)\n")=="y":
        user,pwd=readDBcnf()
        db  =  MySQLdb . connect ( 
        host = "localhost" ,     #主機名
        user = user ,          #用戶名
        passwd = pwd,   #密碼
        charset='utf8',
        )         #數據庫名稱

        #查詢前，必須先獲取游標
        cur  =  db . cursor ()
        cur.execute("use TTTS;")
        sqlStaments=[x+";" for x in open("testData.sql","r",encoding="utf-8").read(-1).split(";")]
        sqlLines=len(sqlStaments)
        for index,stament in enumerate(sqlStaments):
            print("{}/{}".format(str(index+1),str(sqlLines)))
            if stament==";":
                continue
            cur.execute(stament)
            db.commit()
        db.close()
def main():
    funcs=[rmMigrations,sql,createMigrations,loadSqlDatas]
    for key,val in enumerate(funcs):
        print(key+1,end="")
        print("/",end="")
        print(len(funcs))
        print()
        val()
        print("--------")
main()
