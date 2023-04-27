from django.shortcuts import render,redirect
from myadmin.models import Area,Category,Product,City,Inquiry,Profile,Post,Quickcontact,Feedback,Comment,Report,Likes

from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth,messages
import os
from django.http import HttpResponse

def dashboard(request):
    cat1 = int(Post.objects.filter(category_id=1).count())
    cat2 = int(Post.objects.filter(category_id=2).count())
    cat3 = int(Post.objects.filter(category_id=3).count())
    cat4 = int(Post.objects.filter(category_id=4).count())
    cat5 = int(Post.objects.filter(category_id=5).count())
    cat6 = int(Post.objects.filter(category_id=6).count())
    cat7 = int(Post.objects.filter(category_id=7).count())
    cat_list = ['Robery', 'Bulglary', 'Cyber crime', 'Violence','kidnapping','Theft','Rape']
    count_list = [cat1,cat2,cat3,cat4,cat5,cat6,cat7] 
   
    context = {'cat_list':cat_list,'count_list':count_list}
    return render(request,'myadmin/dashboard.html',context)
#Add category
def add_category(request):
    context = {}
    return render(request,'myadmin/add_category.html',context)

def store_category(request):
    name    = request.POST['name']
    Category.objects.create(name=name)
    return redirect('/myadmin/add_category/')

def view_category(request):
    result = Category.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_category.html',context)

def destroy_category(request, id):
    result = Category.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_category/')

def edit_category(request, id):
    result = Category.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_category.html',context)
    
def update_category(request,id):
    name    = request.POST['name']
    data = {
               'name' : name,
           }

    Category.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/view_category/')
# Add Product

def add_product(request):
    context = {}
    return render(request,'myadmin/add_product.html',context)

def store_product(request):
    pro_name    = request.POST['pro_name']
    pro_des     = request.POST['pro_des']
    myfile=request.FILES['f']
    mylocation=os.path.join(settings.MEDIA_ROOT,'product')
    obj= FileSystemStorage(location=mylocation)
    Product.objects.create(img_name=myfile.name,pro_name=pro_name,pro_des=pro_des)
    obj.save(myfile.name,myfile)
    return redirect('/myadmin/add_product/')
def view_product(request):
    result = Product.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_product.html',context)
def destroy_product(request, id):
    result = Product.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_product/')
def edit_product(request, id):
    result = Product.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_product.html',context)
    
def update_product(request,id):
    pro_name    = request.POST['pro_name']
    pro_des     = request.POST['pro_des']
    myfile=request.FILES['images']
    mylocation=os.path.join(settings.MEDIA_ROOT,'product')
    obj= FileSystemStorage(location=mylocation)
    obj.save(myfile.name,myfile)
    Product.objects.update_or_create(pk=id, defaults={'pro_name' : pro_name,'pro_des' : pro_des,'img_name':myfile})
    return redirect('/myadmin/view_product/')

def add_city(request):
    context = {}
    return render(request,'myadmin/add_city.html',context)
def view_city(request):
    result = City.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_city.html',context)
def store_city(request):
    city_name    = request.POST['city_name']
    City.objects.create(city_name=city_name)
    return redirect('/myadmin/add_city/')
def destroy_city(request, id):
    result = City.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_city/')
def edit_city(request, id):
    result = City.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/edit_city.html',context)
def update_city(request,id):
    city_name    = request.POST['city_name']
    
    data = {
               'city_name' : city_name,
           }

    City.objects.update_or_create(pk=id, defaults=data)
    return redirect('/myadmin/view_city/')

def view_user(request):
    result= User.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_user.html',context)
def destroy_user(request, id):
    result = User.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_user/')



def view_post(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'myadmin/view_post.html',context)

def view_post_like(request):
    context = {}
    return render(request,'myadmin/view_post_like.html',context)



def add_area(request):
	city = City.objects.all()
	context = {'city':city}
	return render(request,'myadmin/add_area.html',context)
def view_area(request):
	result = Area.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_area.html',context)
def store_area(request):
	area_name    = request.POST['area_name']
	city_id = request.POST['city_id']

	Area.objects.create(area_name=area_name,city_id=city_id)
	return redirect('/myadmin/add_area/')
def destroy_area(request, id):
	result = Area.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/view_area/')
def edit_area(request, id):
	city = City.objects.all()
	result = Area.objects.get(pk=id)
	context = {'result':result,'city':city}
	return render(request,'myadmin/edit_area.html',context)
def update_area(request,id):
	area_name    = request.POST['area_name']
	city_id		 = request.POST['city_id']
	
	data = {
			   'area_name' : area_name,
			   'city_id' : city_id,
	       }

	Area.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/view_area/')

def login(request):
    context = {}
    return render(request,'myadmin/login.html',context)
def login_check(request):
    myusername = request.POST['username']
    mypassword = request.POST['password']

    result = auth.authenticate(username=myusername, password=mypassword)

    if result is None:
        messages.error(request, 'Invalid Username or Password')
        return redirect('/myadmin/login/')
    else:
        auth.login(request, result)
        return redirect('/myadmin/dashboard/')
def logout(request):
    auth.logout(request)
    return redirect('/myadmin/login/')
def forgot_password(request):
    context = {}
    return render(request,'myadmin/forgot_password.html',context)


def register(request):
    context = {}
    return render(request,'myadmin/register.html',context)

def view_inquiry(request):
    result = Inquiry.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_inquiry.html',context)
    
def destroy_inquiry(request, id):
    result = Inquiry.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_inquiry/')

def view_Quickcontact(request):
    result = Quickcontact.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_Quickcontact.html',context)
def destroy_Quickcontact(request, id):
    result = Quickcontact.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_Quickcontact/')

def view_feedback(request):
    result = Feedback.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_feedback.html',context)
    
def destroy_feedback(request, id):
    result = Feedback.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_feedback/')

def destroy_post(request,id):
    result=Post.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_post/')

def view_comment(request):
    com = Comment.objects.all()
    context = {'com':com}
    return render(request,'myadmin/view_comment.html',context)
def destroy_comment(request,id):
    result=Comment.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_comment/')

def view_post_like(request):
    res = Likes.objects.all()
    context = {'res':res}
    return render(request,'myadmin/view_post_like.html',context)

def view_report(request):
    result = Report.objects.all()
    context = {'result':result}
    return render(request,'myadmin/view_report.html',context)

def destroy_post1(request,id):
    result=Post.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/view_report/')

