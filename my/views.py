from django.shortcuts import render
from my.models import My
from my.forms import SearchIPForm, SearchIPSelectForm, SearchIPRangeForm
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.

def vlan203(request):
    vlan = My.netManager.get_203_all()
    return render(request, 'vlan203.html', locals())

def vlan10(request):
    vlan = My.netManager.get_10_all()
    return render(request, 'vlan10.html', locals())

def vlan203_IP(request):
    if request.POST:
        f = SearchIPForm(request.POST)
        if f.is_valid():
            ip = f.cleaned_data['ip']
            vlan_ip = My.netManager.get_203_ip(ip)
            ip = ''
            f = SearchIPForm(initial={'ip': '請輸入IP'})
    else:
        f = SearchIPForm(initial={'ip': '請輸入IP'})
    return render(request, 'vlan203_IP.html', locals())

def vlan203_select_IP(request):
    if request.POST:
        f = SearchIPSelectForm(request.POST)
        if f.is_valid():
            ip = f.cleaned_data['ip']
            vlan_ip = My.netManager.get_203_ip(ip)
            ip = ''
            f = SearchIPSelectForm()
    else:
        f = SearchIPSelectForm()
    return render(request, 'vlan203_select_IP.html', locals())

def vlan203_range_IP(request):
    if request.POST:
        f = SearchIPRangeForm(request.POST)
        if f.is_valid():
            ip1 = f.cleaned_data['ip1']
            ip2 = f.cleaned_data['ip2']
            vlan_ip = My.netManager.get_203_range(int(ip1),int(ip2))
            print(vlan_ip)
            ip1 = ''
            ip2 = ''
            f = SearchIPRangeForm()
    else:
        f = SearchIPRangeForm()
    return render(request, 'vlan203_range_IP.html', locals())

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/index/')
    uname = request.POST.get('uname', '')
    pword = request.POST.get('pword', '')
    user = auth.authenticate(username=uname, password=pword)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def index(request):
    return render(request, 'index.html', locals())