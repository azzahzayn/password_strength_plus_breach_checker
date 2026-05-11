import re #to do pattern checking
import hashlib
import requests
def checkstrength(pw):
    score=0
    feedback=[] 
    if len(pw)>=12:
        score+=2
    elif len(pw)>=8:
        score+=1
    else:
        feedback.append('password too short make it 12 characters')
    if re.search(r'[A-Z]',pw):
        score+=1
    else:
        feedback.append('password should contain atleast one uppercase character')
    if re.search(r'[a-z]',pw):
        score+=1
    else:
        feedback.append('password should contain atleast one lowercase character')
    if re.search(r'[0-9]',pw):
        score+=1
    else:
        feedback.append('password should contain atleast one digit')
    if(re.search(r'[!@#$%^&*()_+={}|:;"<>?/]',pw)):
        score+=1
    else:
        feedback.append('password should contain atleast one special character')
    if(score>=6):
        print('strength: strong pw')
    elif(score>=3):
        print('strength: medium pw')
    else:
        print('strength: weak pw')
        print('feedback:')
    c=1
    for i in feedback:
        print(c,'.',i)
        c+=1
    return     
def checkbreach(pw):
    hashed=hashlib.sha1(pw.encode()).hexdigest().upper()
    prefix=hashed[:5]
    url=f"https://api.pwnedpasswords.com/range/{prefix}"
    response=requests.get(url)
    if(response.status_code==200):
        values=response.text.splitlines()
        for i in values:
            suffix,count=i.split(':')
            if(suffix==hashed[5:]):
                print('no of times breach has happened ->',count)
                return 
    print('no breach has happened')
    return
password=input('input pw: ')
checkstrength(password)
checkbreach(password)
