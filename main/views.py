from django.shortcuts import render,redirect
from .urls import *
from  .models import *
# from Admin.urls import *
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def Index(request):
    product = Product.objects.all()
    photo = PhotoMain.objects.first()
    photo2 = PhotoCarucel.objects.all()
    context={
        'product':product,
        'photo1' : photo,
        'carousel':photo2
    }
    return render(request,'index.html',context)
    


def Contact1(request):
    
    return render(request,'contact-page.html')
    
@login_required
def Send_Msg(request):
    r=request.POST
    if request.method=='POST':
        name=r['name']
        email=r['email']
        text=r['text']
        Contact.objects.create(name=name,email=email,text=text)
        info = '<strong>{}</strong>. Xabaringiz Yuborildi! , Tez orada aloqaga chiqamiz'.format(name)
        messages.success(request,info)

        return redirect('/contact/')

def new_price(product):
    price = product.price * ((100 - product.discount) / 100)

    return price

def Add_to_Cart(request):
    pr = request.GET.get('product')
    prod = Product.objects.get(id=id)
    savat = Shop.objects.filter(client=request.user, status=0)
    if len(savat) == 0:
        svt = Shop.objects.create(client=request.user)
    else:
        svt = savat[0]
    new_p = new_price(prod)
    svt.total += new_p
    my_items = ShopItems.objects.filter(shop__client=request.user, shop__status=0, product=prod)
    if len(my_items) == 0:
        ShopItems.objects.create(shop=svt, product=prod, quantity=1, totalPay=new_p)
    else:
        current_item = my_items[0]
        current_item.quantity += 1
        current_item.totalPay += new_p
        current_item.save()

    svt.save()
   
    messages.success(request, f'Savatchaga <strong>{prod.name}</strong> qo`shildi.')
    
    
   
    return redirect('/')
def Cart(request):
    
    # try:
    #     count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    # except:
    #     count = 0
    # product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    # # shopping = Shop.objects.get()
    # try:
    #     shop1=Shop.objects.filter(client=request.user, status=0)[0]
    #     print('try ishladi')
    # except:
    #     print('except ishladi')
    #     shop1={'total':0}
    # print(shop1)
    

    # context = {
    #     'filteredprod':product1,
    #     'order':Shop.objects.first(),
    #     'count':count,
        
        
        

    #     }
    return render(request,'cart-page.html')


def Karta(request):
    return redirect("https://www.google.ru/maps/search/andijon+,eski+shahar/@40.7774022,72.0481789,10z/data=!3m1!4b1?hl=uz")




def Blog(request):
    blog = BlogPage.objects.all()
    context = {
        'blog':blog
    }
    return render(request,'blog-page.html',context)

def Register(request):
   
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for <strong>{}</strong>'.format(user))
            return redirect('/login/')
    else:
        form = UserCreationForm()
    
    context={
        'form':form
    }
    return render(request, 'registration/register.html',context)

def Login(request):
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0 
    
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        info = '<strong>{}</strong>. Account was logged in !'.format(user)

        messages.success(request,info)


        if user is not None:
            login(request,user)
            redirect('/')
        
        else:
            messages.success(request,'Username or password is incorrect!')
    context={
        'count':count,
        'filteredprod':product1,

    }
    return render(request,'registration/login.html',context)    

def Logout(request):
    r=request.user
    logout(request)
    info = '<strong>{}</strong>. You have successfully logged out!'.format(r)
    messages.success(request,info)
    print(messages)
    return redirect('/')