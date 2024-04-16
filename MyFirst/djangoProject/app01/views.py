import requests
from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    return HttpResponse("欢迎")

#默认去templates找html,根据setting中app的注册顺序查找
def user_list(request):
    #优先去项目根目录的templates查找
    #然后根据app注册顺序，在每个app目录下templates查找
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def tpl(request):

    name = "毋庸"
    roles = ["管理员","CEO","保安"]
    user = {"name":"嘎斯","salary":100,"role":"T1"}

    data_list = [
        {"name": "嘎斯", "salary": 100, "role": "T1"},
        {"name": "萨达", "salary": 200, "role": "T2"},
        {"name": "干扰", "salary": 300, "role": "T3"},
    ]


    return render(request,"tpl.html",{"n1":name,"n2":roles,"n3":user,"n4":data_list})


def news(request):

    #定义一些东西，字典或列表、或去数据库  网络请求去联通新闻
    #向地址https://www.chinaunicom.com/43/menu01/1/news?id=a2d2f702-4267-429f-b60c-ca2e56492924
    #第三方库requests
    header = {
        "User - Agent":
            "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 122.0.0.0Safari / 537.36Edg / 122.0.0.0"
    }
    res = requests.get("https://www.bilibili.com/video/BV1zx4y1o7Ry/?spm_id_from=333.337.search-card.all.click&vd_source=df86fc5c74aeb5be46cca42b5ae7ac30",headers=header)
    # data_list = res.json()
    print(res.json())


    return render(request,"news.html")

def something(request):

    print(request.method)

    print(request.GET)

    print(request.POST)

    #return render(request,"something.html",{"title":"是的"})

    #让浏览器重定向
    return redirect("https://www.bilibili.com/")

def login(request):
    if request.method =="GET":
        return render(request,"login.html")
    else:
        #print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        if username == "admin" and password == "123":
            #return HttpResponse("登陆成功")
            return redirect("https://www.bilibili.com/")
        else:
            #return HttpResponse("登陆失败")
            return render(request,"login.html",{"error_msg":"用户名或密码错误"})


from .models import Dapartment,UserInfo
def orm(request):
    #测试orm表中数据

    #添加
    # UserInfo.objects.create(name='萨格', password='123', age=18)
    # UserInfo.objects.create(name='天然碱', password='rh', age=28)
    # UserInfo.objects.create(name='热红外', password='dftyh', age=14)

    # #删除 (filter是加条件）
    # UserInfo.objects.filter(id=1).delete()#把id=1的删除
    # #将所有数据删除
    # UserInfo.objects.all().delete()

    # #获取数据
    # data_list = UserInfo.objects.all() #获取到的是列表
    # for obj in data_list :
    #     print(obj.id,obj.name,obj.password,obj.age)
    #
    # #根据条件获取到所有符合的数据（返回列表），加了first就是获取第一条符合的数据（返回对象）
    # text = UserInfo.objects.filter(id=2).first()
    # print(text.name,text.password,text.age)  #因为只有一个对象，所以直接输出

    #更新数据
    UserInfo.objects.all().update(password=111)
    UserInfo.objects.filter(id=3).update(password=321)
    UserInfo.objects.filter(name="天然碱").update(age=221)

    return HttpResponse("成功")


def info(request):
    #获取数据库中所有用户信息
    data = UserInfo.objects.all()
    #print(data)


    return render(request,"info.html",{"data":data})

def infoAdd(request):
    if request == "GET":
        return render(request,"infoAdd.html")
    else:
        #获取数据
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        age = request.POST.get("age")

        #添加数据库
        if user:
            UserInfo.objects.create(name=user,password=pwd,age=age)

        return render(request,"info.html",{"op":"添加成功"})

def infoDelete(request):
    nid = request.POST.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("info.html")
