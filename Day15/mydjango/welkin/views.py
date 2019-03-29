from django.shortcuts import render, HttpResponse, redirect
from welkin import models
import hashlib

# Create your views here.


def index(request):
    return render(request,'index.html')


def dele(request):
    iid = request.GET.get('idi')
    models.User.objects.filter(uid=iid).delete()
    return redirect('/manage/')


def login(request):
    mesg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('pwd')
        pass_wd = hashlib.md5(passwd.encode('utf8')).hexdigest()
        if models.User.objects.filter(name=username, password=pass_wd):
            return redirect('/index/')
        else:
            mesg = '密码或用户名错误'
    return render(request, 'login.html', {'msg': mesg})


def manage(request):
    mms = ''
    if request.method == 'POST':
        uiname = request.POST.get('title')
        if models.User.objects.filter(name=uiname):
            mms = '用户名已存在'
        else:
            passd = request.POST.get('user')
            passd = hashlib.md5(passd.encode('utf8')).hexdigest()
            models.User.objects.create(name=uiname, password=passd)
    comm = models.User.objects.all()
    return render(request, 'show.html', {'mms': mms, 'commc': comm})


def edi(request):
    obj = ''
    if request.method == 'POST':
        ida = request.POST.get('uui')
        nms = request.POST.get('usn')
        # if models.User.objects.filter(uid=ida) or models.User.objects.filter(name=nms):
        #     msm = '编号或用户名已存在'
        # else:
        pdd = request.POST.get('psd')
        mpd = hashlib.md5(pdd.encode('utf8')).hexdigest()
        obj = models.User.objects.get(uid=ida)
        obj.name = nms
        obj.password = mpd
        obj.save()
        return redirect('/manage/')
    else:
        ida = request.GET.get('idi')
        try:
            obj = models.User.objects.get(uid=ida)
        except Exception as e:
            print(e)
    return render(request, 'edi.html', {'ccm': obj})