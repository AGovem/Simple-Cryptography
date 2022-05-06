import hashlib
import time
import os
import base64
from cryptography.fernet import Fernet

CurDir = os.getcwd()
DirList = os.listdir(CurDir)

menu = """
\33[92m-----------------\33[91mWelcome To File Encryption App\33[92m-----------------\33[m
            
            \33[94m0)\33[96m Create Key
            
            \33[94m1)\33[96m Text Encryption
            \33[94m2)\33[96m Text Decryption
            
            \33[94m3)\33[96m File Encryption
            \33[94m4)\33[96m File Decryption
            
            \33[94m5)\33[96m Folder Encryption
            \33[94m6)\33[96m Folder Decryption
            
            \33[95m7) Advanced Encryption (Coming Soon)       #2 veya daha fazla kez şifreleme yapacak art arda
            
            \33[94mq)\33[96m Exit
            
\33[31m NOTE\33[m: \33[32mDON'T LOSE YOUR KEY !!!!!\33[m
"""

def CreateKey():
    keyfile = input("Please Type Your Key Files Name (\33[4mB\33[mack) : ")
    keyfile = keyfile+".key"
    if keyfile == "b" or keyfile == "B":
        return menu
    if bool(keyfile):
        pass
    else:
        keyfile = "KeyFile.key"
    Control(keyfile, DirList)
    passwd = input("Please Enter Password :  ").encode("UTF-8")
    key = base64.urlsafe_b64encode(hashlib.sha256(passwd).digest())

    # This Part Save Your Password To A File
    with open(keyfile, "wb") as KFile:
        KFile.write(key)
        KFile.close()

    time.sleep(1)
    print("\n", "Your Key Saved To \33[32m{}\33[m Location as \33[34m{}\33[m".format(CurDir, keyfile))

def LoadKey():
    keyfile = input("Please Type Your Key File's Name/Path (\33[4mB\33[mack) : ")
    if bool(keyfile):
        pass
    else:
        keyfile = "KeyFile.key"
    return open(keyfile, "rb").read()

def TextEnc(Text,KeyFileName):
    f = Fernet(KeyFileName)
    EncText = f.encrypt(Text)
    print("Encrypted Text >>>>>>>"+ "\33[32m", EncText, "\33[m")

def TextDec(EncText,KeyFileName):
    f = Fernet(KeyFileName)
    DecText = f.decrypt(EncText)
    print("Decrypted File >>>>>>>", "\33[32m", DecText, "\33[m")

def Encrypt(FileName,KeyFileName):
    f = Fernet(KeyFileName)
    with open(FileName,"rb") as file:
        FData = file.read()
    EncData = f.encrypt(FData)

    with open(FileName,"wb") as EncFile:
        EncFile.write(EncData)

def Decrypt(FileName,KeyFileName):
    f = Fernet(KeyFileName)
    with open(FileName,"rb") as file:
        FData = file.read()
    DecData = f.decrypt(FData)

    with open(FileName,"wb") as DecFile:
        DecFile.write(DecData)

def Control(FName, SearchZone):
    if FName in DirList:
        input("You Have A File With Same Name")
        return CreateKey()
    else:
        pass

def Return():
    input("There Is No Such File")
    return LoadKey()


while True:
    print(menu)
    c = input("Please Select The Symbol Of The Desired Operation : ")
    try:
        if c == "0":
            CreateKey()
            input()

        elif c == "1":                      # Text Encryption
            key = LoadKey()
            m = input("Please Write Your Text (\33[4mB\33[mack) : ").encode("UTF-8")
            if m == b"b" or m == b"B":
                input("Press Enter To Return To The Menu")
            else:
                TextEnc(m, key)
                input()

        elif c == "2":                      # Text Decrption
            key = LoadKey()
            Em = input("Please Write Encrypted Text (\33[4mB\33[mack) : ").encode("UTF-8")
            if Em == b"b" or Em == b"B":
                input("Press Enter To Return To The Menu")
            else:
                TextDec(Em, key)
                input()

        elif c == "3":                      # File Encryption
            key = LoadKey()
            try:
                file = input("Please Write File Name (\33[4mB\33[mack) : ")
                if file == b"b" or file == b"B":
                    input("Press Enter To Return To The Menu")
                Encrypt(file, key)
                input("\33[92mThis File Is Encrypted Successfully\33[m")
            except:
                input("\33[31mThis File Isn't In The Current Directory!!! Try To Type Your File's Path.\33[m")

        elif c == "4":                      # File Decryption
            key = LoadKey()
            try:
                file = input("Please Write File Name (\33[4mB\33[mack) : ")
                if file == b"b" or file == b"B":
                    input("Press Enter To Return To The Menu")
                Decrypt(file, key)
                input("\33[92mDecryption Is Completed Successfully\33[m")
            except:
                input("\33[31mThis File Isn't In The Current Directory!!! Try To Type Your File's Path.\33[m")

        elif c == "5":                      # Folder Encryption
            try:
                key = LoadKey()
            except:
                Return()
            try:
                folder = input("Please Write Folder Path You Want To Encrypt : ")
                folderdat = os.listdir(folder)
                s = 0
                for filename in folderdat:
                    filepath = folder + "\\" + filename
                    name, ext = os.path.splitext(filepath)
                    if ext != ".key" and ext != ".py":
                        Encrypt(filepath, key)
                    print("\33[92m\r Files Are Encrypting", "\33[92m. \33[m" * s, end="")
                    s += 1
                    time.sleep(1)
                    input("\33[92m Encryption Successfully Finished \33[m")

            except:
                print("\33[91m There Is No Folder Path You Want To Encrypt !!! \33[m")
                time.sleep(3)

        elif c == "6":                      # Folder Decryption
            try:
                key = LoadKey()
            except:
                Return()
            try:
                folder = input("Please Write Folder Path You Want To Decrypt : ")
                folderdat = os.listdir(folder)
                s = 0
                for filenames in folderdat:
                    filepath = folder + "\\" + filenames
                    name, ext = os.path.splitext(filepath)
                    if ext != ".key" and ext != ".py":
                        Decrypt(filepath, key)
                    print("\33[92m Files Are Decrypting", "\33[92m.\33[m" * s, end="")
                    s += 1
                    time.sleep(1)
                    input("\33[92m Decryption Successfully Finished \33[m")
            except:
                print("\33[91mThere Is No Folder Path You Want To Decrypt !!! \33[m")
                time.sleep(3)

        elif c == "q" or c == "Q":
            break

    except:
        input("\33[31m Please Select Symbol On Menu \33[m")
