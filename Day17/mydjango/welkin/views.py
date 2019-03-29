from django.shortcuts import render, redirect, reverse
from django.views import View
from welkin import models
import hashlib

# Create your views here.


def index(request):
    return render(request,'index.html')


def dele(request):
    iid = request.GET.get('idi')
    models.User.objects.filter(uid=iid).delete()
    return redirect(reverse('show'))


def delt(request):
    sid = request.GET.get('idi')
    sid = int(sid)
    models.Mainframe.objects.filter(id=sid).delete()
    return redirect(reverse('asd'))


def login(request):
    mesg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('pwd')
        pass_wd = hashlib.md5(passwd.encode('utf8')).hexdigest()
        if models.User.objects.filter(name=username, password=pass_wd):
            return redirect(reverse('index'))
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
        pdd = request.POST.get('psd')
        mpd = hashlib.md5(pdd.encode('utf8')).hexdigest()
        obj = models.User.objects.get(uid=ida)
        obj.name = nms
        obj.password = mpd
        obj.save()
        return redirect(reverse('show'))
    else:
        ida = request.GET.get('idi')
        try:
            obj = models.User.objects.get(uid=ida)
        except Exception as e:
            print(e)
    return render(request, 'edi.html', {'ccm': obj})


class Sedi(View):

    def get(self, request):
        sida = request.GET.get('idi')
        obj = models.Mainframe.objects.get(id=sida)
        apl = models.Appline.objects.all()
        return render(request, 'sedi.html', {'ccm': obj, 'apl': apl})

    def post(self, request):
        ida = request.POST.get('uui')
        nms = request.POST.get('usn')
        pdd = request.POST.get('psd')
        lins = request.POST.get('appline')
        # mpd = hashlib.md5(pdd.encode('utf8')).hexdigest()
        obj = models.Mainframe.objects.get(id=ida)
        obj.hostname = nms
        obj.paswd = pdd
        obj.line_id = lins
        obj.save()
        return redirect(reverse('asd'))


class Apline(View):
    def get(self, request):
        ali = models.Appline.objects.all()
        return render(request, 'alines.html', {'ali': ali})

    def post(self, request):
        apm = request.POST.get('appline')
        models.Appline.objects.create(appname=apm)
        return redirect(reverse('apline'))


def ldelt(request):
    llid = request.GET.get('idi')
    llid = int(llid)
    ret = models.Appline.objects.get(lid=llid)
    ret.line_user.clear()
    ret.delete()
    return redirect(reverse('apline'))



# def tes(request, oo='11'):
#     ss = oo
#     vv = '22'
#     print(ss)
#     return render(request, 'test.html',{'vv':vv})


# def asd(request):
#     mms = ''
#     if request.method == 'POST':
#         uiname = request.POST.get('title')
#         if models.Mainframe.objects.filter(hostname=uiname):
#             mms = '主机名已存在'
#         else:
#             passd = request.POST.get('user')
#             # passd = hashlib.md5(passd.encode('utf8')).hexdigest()
#             models.Mainframe.objects.create(hostname=uiname, paswd=passd)
#     comm = models.Mainframe.objects.all()
#     apli = models.Appline.objects.all()
#     return render(request, 'maintion.html', {'mms': mms, 'commc': comm, 'apli': apli})

class ser_page(View):


    def __init__(self):
        self.mms = ''
        self.comm = models.Mainframe.objects.all()
        self.apli = models.Appline.objects.all()

    def get(self, request):
        return render(request, 'maintion.html', {'mms': self.mms, 'commc': self.comm, 'apli': self.apli})

    def post(self, request):
        uiname = request.POST.get('title')
        if models.Mainframe.objects.filter(hostname=uiname):
            self.mms = '主机名已存在'
        else:
            appli = request.POST.get('appline')
            passd = request.POST.get('user')
            # passd = hashlib.md5(passd.encode('utf8')).hexdigest()
            models.Mainframe.objects.create(hostname=uiname, paswd=passd, line_id=appli)
        return render(request, 'maintion.html', {'mms': self.mms, 'commc': self.comm, 'apli': self.apli})