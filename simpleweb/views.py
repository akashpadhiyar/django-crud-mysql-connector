from django.shortcuts import render,redirect
 
from django.http import HttpResponse
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='db_ecom_stock')
print('Successfully connected to database')
cur = conn.cursor()

def home(request):
    return  render(request,'home.html')


def categorylisting(request):
    cur.execute("SELECT * FROM `tb_category`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'view.html', {'categories': data})   


def categorycreate(request):
    return render(request, 'add.html')   


def categoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['txt1']
        cur.execute("INSERT INTO `tb_category`(`category_name`) VALUES ('{}')".format(catname))
        conn.commit()
        return redirect(categorycreate) 
    else:
        return redirect(categorycreate)


def categorydelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_category` where `category_id` = {}".format(id))
    conn.commit()
    return redirect(categorylisting) 


def categoryedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_category` where `category_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'edit.html', {'categories': data})   


def categoryupdate(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['txt2']
        cur.execute("update `tb_category` set `category_name` ='{}' where `category_id`='{}'".format(catname,catid))
        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorylisting)