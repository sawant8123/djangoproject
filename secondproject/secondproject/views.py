from django.shortcuts import HttpResponse
data=f"<hr><a href='/'>Home</a>   <a href='/signup'>Signup</a>   <a href='/signin'>Signin</a>"

def index(req):
    return HttpResponse(f"<center><h1>Welcome to my page{data}</h1></center>")

def signup(req):
    global username
    username=input("Enter your name=")
    return HttpResponse(f"<center><h1>Signup Page{data}</h1></center>")

def signin(req):
    checkusername=input("Enter username to sign in :")
    if checkusername==username:
        next=f"<hr><h1><a href='/'>LOgout</a></h1>"
        return HttpResponse(f"<center><h1>Welcome{checkusername}!! {next} </h1></center>")
    else:
        msg=f"<center><h1></h1>Incorrect Username !! Try Again</center>"
        next=f"<hr><h1><a href='/'>Click here to go back</a>"
        return HttpResponse(f"{msg}{next}")