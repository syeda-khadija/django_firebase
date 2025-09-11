from django.shortcuts import  render, redirect
from mypro.firebase_config import db
from django.contrib import messages
from wheel.cli.convert import convert


def Contacts(request):
    if request.method=="POST":
        a = request.POST.get("name")
        b = request.POST.get("email")
        c = request.POST.get("message")

        db.collection("contact").add({
            "Name": a,
            "Email" :b,
            "Msg": c
        })
        messages.success(request,"query has been submitted")
        return redirect("con")

    return render(request,"myapp/Contacts.html")
def showData(request):
    mydata =db.collection("contact").stream()
    contact=[]
    for a in mydata:
        convert_dict = a.to_dict()
        contact.append(convert_dict)
    return render(request,"myapp/showdata.html",{"con":contact})