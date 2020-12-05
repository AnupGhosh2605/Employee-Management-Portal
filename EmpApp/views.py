from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib import messages
from .models import registerData,projectData,adminData
from django.core.files.storage import FileSystemStorage
import sqlalchemy
import pandas as pd
import mysql.connector
from mysql.connector import Error

# Main page access to everyone
def index(request):
    return render(request,'index.html')
# Only for register user 
def intro(request):
    if request.session.has_key('is_logged') :
        email = request.session['email']
        return render(request,'index.html',{'email':email})
    return redirect('index')
    

def register(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if registerData.objects.filter(email=email).exists():
                messages.info(request,'Opps! Email already exist.')
                return redirect('index')
            else:
                user = registerData.objects.create(name=name,email=email,phone=phone,password=password)
                user.save()
                messages.info(request,'You have registered successfully...')
                return render(request,'index.html',{})
        else:
            messages.info(request,'Opps! Password is not matching.')
    
    return render(request,'index.html')

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('intro')
    if request.method =='POST':
        email = request.POST['email']
        password =request.POST['password']
        query=registerData.objects.filter(email=email, password=password).count()
        if query==1 :
            request.session['email'] = email
            request.session['is_logged'] = True
            return render(request,'index.html',{'email':email})
            #return redirect('intro')
        else:
            messages.info(request,'Invelid Credentials.')
    else:
        return redirect('index')
    return render(request,'index.html')

# Only for register user
def profile(request):
    if request.session.has_key('is_logged'):
        email = request.session['email']
        engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/employeedata')
        df = pd.read_sql_table("empapp_registerdata",engine)
        mask = df.loc[df['email'] == email]
        name = mask.name.to_string(index=False)
        email = mask.email.to_string(index=False)
        phone = mask.phone.to_string(index=False)
        return render(request,'profile.html',{'name':name , 'email':email,'phone':phone})
    return redirect('/')

# Only for register user
def edit(request):
    if request.session.has_key('is_logged'):
        email = request.session['email']
        engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/employeedata')
        df = pd.read_sql_table("empapp_registerdata",engine)
        mask = df.loc[df['email'] == email]
        name = mask.name.to_string(index=False)
        phone = mask.phone.to_string(index=False)
        return render(request,'edit.html',{'name':name ,'phone':phone})   
    return redirect('/')

# Only for register user
def update(request):
    if request.session.has_key('is_logged'):
        if request.method =='POST':
            name = request.POST['name']
            phone = request.POST['phone']
            mydb = mysql.connector.connect( 
            host ='localhost', 
            database ='employeedata', 
            user ='root', 
            password = '',
            ) 
            email = request.session['email']
            cs = mydb.cursor() 
            statement ="""UPDATE empapp_registerdata SET phone = %s , name = %s    WHERE email = %s"""
            data=(phone,name,email)
            cs.execute(statement,data) 
            mydb.commit() 
            mydb.close()
            print("updated")
            return redirect('intro')
    return redirect('/')

# Only for register user
def dashboard(request):
    if request.session.has_key('is_logged'):
        if request.method =='POST': 
            email = request.session['email']
            name = request.POST['name']
            projectName = request.POST['projectName']
            projectPercenatge = request.POST['projectPercenatge']
            upload = request.FILES['cv']
            fs =FileSystemStorage()
            url = fs.url(upload)
            user = projectData.objects.create(name=name,email=email,projectName=projectName,projectPercenatge=projectPercenatge,upload=upload,url=url)
            user.save()
            return render(request,'index.html',{'email':email ,'dash':12})
            #return redirect('intro')
        return render(request,'dashboard.html')
    return redirect('index')

# showing data of  Dashboard
def updateDashboard(request):
    if request.session.has_key('is_logged'):
        email = request.session['email']
        engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/employeedata')
        df = pd.read_sql_table("empapp_projectdata",engine)
        mask = df.loc[df['email'] == email]
        name = mask.name.to_string(index=False)
        print(name)
        projectName = mask.projectName.to_string(index=False)
        projectPercenatge = mask.projectPercenatge.to_string(index=False)
        return render(request,'updateDashboard.html',{'name':name ,'projectName':projectName,'projectPercenatge':projectPercenatge})   
    return redirect('index')

# udate dashboard data
def updashboard(request):
    if request.method =='POST': 
        email = request.session['email']
        name = request.POST['name']
        projectName = request.POST['projectName']
        projectPercenatge = request.POST['projectPercenatge']
        conn = mysql.connector.connect( 
        host ='localhost', 
        database ='employeedata', 
        user ='root', 
        password = '',
        ) 
        query = """UPDATE empapp_projectdata set name = %s, projectName = %s , projectPercenatge = %s  where email = %s"""
        data = (name,projectName,projectPercenatge,email)
        cur = conn.cursor()
        cur.execute(query,data)
        conn.commit()
        conn.close()
    else:
        return redirect('intro')
    return redirect('intro')
    

# Only for register user
def logout(request):
    del  request.session['is_logged']
    return redirect('/')


# Admin Login Board
def AdminIndex(request):
    if request.method =='POST':
        email = request.POST['email']
        password =request.POST['password']
        query=adminData.objects.filter(email=email, password=password).count()
        if query==1 :
            request.session['is_admin'] = True
            return redirect('AdminDashboard')
        else:
            messages.info(request,'Invelid Credentials.')
    return render(request,'AdminIndex.html')

# Employee Data only for Admin User
def AdminDashboard(request):
    if request.session.has_key('is_admin'):
        data = projectData.objects.all()
        return render(request,'AdminDashboard.html',{'data':data})
    return redirect('index')





# Admin Logout
def logoutAdmin(request):
    del request.session['is_admin']
    return redirect('index')
