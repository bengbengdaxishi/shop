from django.shortcuts import render
from shoping.forms import *
from shoping.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
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

    return render(request, 'cart_views.html', context=context)






def detail(request):

    if   request.GET.get('did', None):
         did = request.GET.get('did', None)
         fur = Furniture.objects.get(pk=did)
         comments = Comment.objects.filter(fur_id=fur.id)
         users = []
         for c in comments:
             user = User.objects.get(id=c.user_id)
             users.append(user)
             print (c.comm)

         return render(request,'detail.html', {'users':users, 'comments':comments, 'fur':fur})
    else:
        return render(request, 'detail.html' )



def cleanCart(request,cid):
    user = User.objects.get(pk=cid)
    cart = Car.objects.filter(user=user).delete()
    return render(request, 'clean_car.html', locals())


def add_cart(request, uid, chid, fur_count):
    uid = uid
    chid = int(chid)
    fur_count = int(fur_count)
    user = User.objects.get(pk=uid)
    fur = Furniture.objects.get(pk=chid)
    carts = Car.objects.filter(user=user, goods=fur)
    if len(carts)>=1:
        cart = carts[0]
        cart.count = cart.count + fur_count
        cart.save()
    else:
        cart =Car()
        cart.user_id = uid
        cart.goods_id = chid
        cart.count = fur_count
        cart.save()



    # return redirect('/cart/2')
    url = reverse("view_car",kwargs={'uid':uid})
    return redirect(url)


def all_goods(request):
    all_goods = Furniture.objects.all()
    return render(request, 'all_goods.html',locals())



#提交订单页面
def order(request):
    if request.user.is_authenticated():
        user = User.objects.get(pk=request.user.id)


