from django.shortcuts import render
from shoping.forms import *
from shoping.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    return render(request, 'index.html')


#注册
def register(request):
    if request.method == 'post':
        reg_form =  RegisterForm(request.POST)
        if reg_form.is_valid():
            if User.objects.filter(email = reg_form.cleand_data['email']):
                return render(request, 'register.html', {'register_form':reg_form,'msg':'用户已经存在'})
            user = User.objects.create(username=reg_form.cleand_data['username'],
                                       email = reg_form.cleand_data['email'],
                                       password = make_password(reg_form.cleaned_data["password"]),
                                       address = reg_form.cleand_data['address'],
                                       phone = reg_form.cleand_data['phone'],
                                       )
            user = authenticate(username=reg_form.cleaned_data["username"],password=reg_form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return render(request,'index.html' ,locals())
            else:
                return render(request,'register.html')
    else:
        reg_form = RegisterForm()
        return render(request,'register.html',locals())



#登录
def login(request):
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data['username']
            password = log_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request, 'index.html')
            else:
                return render(request, 'error.html', {'reason':'登录验证失败'})
    else:
        log_form = LoginForm()
        return render(request, 'login.html', locals())


def logout(request):
    logout(request)
    return render(request, 'index.html', locals())



#查看购物车
def view_cart(request):
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.id)
        carts = Car.objects.filter(user=user)
        all_goods = 0
        all_money = 0
        for cart in carts:
            all_goods += cart.count
            all_money += cart.goods.new_price*cart.count

        context = {'all_money':all_money,
                   'all_goods':all_goods,
                   'carts':carts}

        return render(request,'cart_views.html',locals())




#测试
def view_car(request,uid):
    user = User.objects.get(id=int(uid))
    carts = Car.objects.filter(user=user)
    all_goods = 0
    all_money = 0
    for cart in carts:
        all_goods += cart.count
        all_money += cart.goods.new_price*cart.count

    context = {'all_money':all_money,
    'all_goods':all_goods,
    'carts':carts}

    return render(request,'cart_views.html',locals())



#测试2
def view_cart(request):
    uid = request.GET.get('id','')
    if uid:
        user = User.objects.get(id=uid)
        carts = Car.objects.filter(user=user)
        all_goods = 0
        all_money = 0
        for cart in carts:
            all_goods += cart.count
            all_money += cart.goods.new_price*cart.count

        context = {'all_money':all_money,
        'all_goods':all_goods,
        'carts':carts}

        return render(request,'cart_views.html',context=context)
    else:

        return render(request,'cart_view.html',locals())