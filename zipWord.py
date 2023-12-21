import zipfile
import time 

folderpath=input("path to the file:")
zipf=zipfile.ZipFile(folderpath)

global result
result=0

global tried
tried=0
c=0

if not zipf:
    print("The zip file is not password protected")
else:
    starttime=time.time()
    wordlistfile=open("wordlist.txt","r",errors="ignore")
    body=wordlistfile.read().lower()
    words=body.split("\n")
    for i in range(len(words)):
        word=words[i]
        password=word.encode("utf8").strip()
        c=c+1
        try:
            with zipfile.ZipFile(folderpath,"r") as x:
                x.extractall(pwd=password)
                print("success! the password is "+word)
                endTime=time.time()
                result=1
            break
        except:
            pass
    if result==0:
        print("Sorry password not found")
    else:
        duration=endTime-starttime
        print("Congratulations! The password found in "+str(duration)+" seconds")