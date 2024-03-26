import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse, FileResponse
import datetime
from .models import *

def isAuth(request):
    id_user = request.session.get('id_user',None)
    if not id_user:
        return {}
    else:
        user = User.objects.get(id= id_user)
        return {"user" : id_user, "branchs_id" : user.branchs.split(','), "name" : user.name}

def printer_driver(request):    
    data = isAuth(request)
    data['printers'] = PrinterModel.objects.all()
    return render(request, "printer_driver.html", context= data)

def printers(request):
    data = isAuth(request) 
    if data:
        branchs = Branch.objects.filter(id__in = data["branchs_id"])
        data["branchs"] = branchs
    return render(request, "printers.html", context= data)

def printers_on_branch(request, id):
    data = isAuth(request) 
    if data:
        if str(id) in data["branchs_id"]:
            printers = Printer.objects.filter(branch = id)
            data["printers"] = printers
        else:
            data["error"] = "За вами не закреплен данный филиал."
    else:        
        data["error"] = "Требуется авторизация"
    return render(request, "printers.html", context= data)

def index(request):
    data = isAuth(request) 
    if data:
        branchs = Branch.objects.filter(id__in = data["branchs_id"])
        data["branchs"] = branchs
    return render(request, "index.html", context= data)

def monitoring(request):
    data = isAuth(request)
    if request.method == "POST":
        if data:
            equipments = Equipment.objects.filter(branch__in = data["branchs_id"], status = False, monitoring = True)
            x = datetime.datetime.now()        
            c = datetime.datetime(x.year,x.month, x.day, x.hour,x.minute,x.second)
            for eq in equipments:
                eq.time_off = c.replace(tzinfo=eq.time_off.tzinfo) - eq.time_off
            data["equipments"] = equipments
            return render(request, "equipment.html", context= data)
        else:
            return HttpResponse('Не авторизован.')
    else:
        return render(request, "monitoring.html", context=data)
    
def about(request):
    return render(request, "about.html")
 
def contact(request):
    return render(request, "contact.html")

def info_page(request):
    try:       
        data = isAuth(request) 
        get_type = request.GET.get("type",None)
        if get_type:            
            info_topic = Info.objects.filter(type = get_type).order_by("topic").distinct()            
            data['name_head'] = get_type
            data['info_topic'] = info_topic   
        else:  
            info_type = Info.objects.values_list("type", flat=True).order_by("type").distinct()
            data['name_head'] = 'Info'
            data['info_type'] = info_type
        return render(request,"info.html",context = data)
    except Info.DoesNotExist:
        return HttpResponseNotFound("<h2>Info not found</h2>")

def info(request, id):
    try:
        data = isAuth(request) 
        info = Info.objects.get(id = id)
        data['name_head'] = info.type + " - " + info.topic
        data['info'] = info
        if info.file != '':
            if(os.path.splitext(info.file)[1]) == ".jpg" :
                data['img'] = info.file
            else :
                data['file'] = info.file          
            return render(request,"info.html",context = data)
        return render(request,"info.html",context = data)
    except Info.DoesNotExist:
        return HttpResponseNotFound("<h2>Info not found</h2>")

def file(request):    
    name = request.GET.get("name")
    try:
        if(file):
            return FileResponse(open("C:/ZabbixMTBot/" + name, 'rb'))
        else:        
            return HttpResponseNotFound("<h2>File not found</h2>")
    except:        
        return HttpResponseNotFound("<h2>File not found</h2>")

def setting(request):
    data = isAuth(request)
    return render(request,"setting.html", context = data)    

def auth(request):
    if request.method == "POST":
        login_post = request.POST.get("login", None)
        if(login_post):
            try:            
                user = User.objects.get(login = login_post)
                if user:
                    print(user)
                    request.session['id_user'] = user.id
                    return HttpResponse('ok')
                else:
                    return HttpResponse('Не верный логин')
            except:                
                return HttpResponse('Не верный логин')
    return HttpResponse('Нельзя так делать!!!')

def logout(request):
    request.session['id_user'] = None
    return HttpResponseRedirect('/')