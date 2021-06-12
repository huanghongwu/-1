# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %% [markdown]
# 

# %%
print(1)


# %%
12

# %% [markdown]
# # 1号标题
# ### 3号标题
# 
# #### 无序列表
# * 8709
# * 1244344
# + 376977689
# - 8736272
# 
# #### 有序列表
# 1. 8709
# 2. 1244344
# 3. 376977689
# 4. 8736272
# 
# #### 换行
# 87663
# 
# 454
# 
# 
# 644
# %% [markdown]
# '''python
# def fuc1():
# pass
# '''
# %% [markdown]
# [跳转百度](http://www.baidu.com)
# ![图片](Screenshot_20200528_212905.jpg)
# %% [markdown]
# request的使用

# %%
from urllib import request
url = "http://www.baidu.com"
res = request.urlopen(url)
print(res.info())

print(res.getcode())

print(res.url)

print(res.read().decode("utf-8"))


# %%
url = "http://www.dianping.com"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
}
req = request.Request(url=url,headers=head)
res = request.urlopen(req)

print(res.read().decode("utf-8"))








# %% [markdown]
# requests的使用

# %%
import requests

url = "http://www.baidu.com"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
}
res = requests.get(url=url,headers=head)

print(res.encoding) #查看content-type,如果没有content-type，则为默认的utf-8, 如果设置了charset，就以charset为准，有content-type但没有设置charset且指定类型为text，则编码为ISO-8859-1
print(res.headers)


# %%
print(res.text)
res.encoding="utf-8"
print(res.text)
print(res.status_code)

# %% [markdown]
# beautifulsoup 简单使用

# %%
from bs4 import BeautifulSoup
import requests

url = "http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b1_c513"
res = requests.get(url)
# print(res.headers)
res.encoding = "gb18030"

html = res.text

soup = BeautifulSoup(html)

# print(html)
# print(soup.find('h2').text)

print(soup.div.table.contents[7])

for i in soup.div.table.contents:
    try:
        #print(i)
        print(i.a.contents)
        print(i.find(class_ = "icon-rise"))
    except:
        pass

# print(a)
# b = a.find_all('a')

#for i in b:
    #print(i.attrs["href"])


# %%
for i in b:
    #print(i.attrs["href"])

    url='http://wsjkw.sc.gov.cn'+i.attrs["href"]

    res = requests.get(url)

    res.encoding = "utf-8"

    html = res.text

    soup = BeautifulSoup(html)

    first_p=soup.p

    second_p=first_p.find_next('p')

    print(second_p)


# %% [markdown]
# 
# 湖北
# https://voice.baidu.com/newpneumonia/getv2?target=trend&isCaseIn=1&from=mola-virus&area=%E6%B9%96%E5%8C%97&stage=publish 
# 
# 
# 重庆
# https://voice.baidu.com/newpneumonia/getv2?target=trend&isCaseIn=1&from=mola-virus&area=%E9%87%8D%E5%BA%86&stage=publish
# 
# 
# 
# 

# %%
import json
url='https://voice.baidu.com/newpneumonia/getv2?target=trend&isCaseIn=1&from=mola-virus&area='+str('英国')+'&stage=publish'

res = requests.get(url)

res.encoding = "utf-8"

html = res.text

d = json.loads(html)
# print(d)
data_all = d
#print(d)
#data_all =dict(d["data"])

#print(d["data"])
#print(d)
print(type(data_all))
print(data_all)


# soup = BeautifulSoup(html)

# print(soup)

# first_p=soup.p

# second_p=first_p.find_next('p')

# print(second_p)


# %%
print(data_all["data"][0]["trend"]["updateDate"])
      
   #   ["trend"]["updateDate"])


# %%
print(data_all["data"][0]["trend"]["list"][0]["name"])
print(data_all["data"][0]["trend"]["list"][0]["data"])


# %%
print(data_all["data"][0]["trend"]["list"][1]["name"])
print(data_all["data"][0]["trend"]["list"][1]["data"])


# %%
print(data_all["data"][0]["trend"]["list"][2]["name"])
print(data_all["data"][0]["trend"]["list"][2]["data"])


# %%
print(data_all["data"][0]["trend"]["list"][3]["name"])
print(data_all["data"][0]["trend"]["list"][3]["data"])

# %% [markdown]
# 北京市 天津市 上海市 重庆市
# 
# 河北省 山西省 辽宁省 吉林省 黑龙江省 江苏省 浙江省 安徽省 福建省 江西省 山东省 河南省 湖北省 湖南省 广东省 海南省 四川省 贵州省 云南省 陕西省 甘肃省 青海省 台湾省
# 
# 内蒙古自治区 广西壮族自治区 西藏自治区 宁夏回族自治区 新疆维吾尔自治区
# 
# 香港特别行政区 澳门特别行政区
# 
# 
# 返回历史数据：
# 
# **日期-省-累计-治愈-死亡-新增
# 
# 累计人数需要在网页中单独查找
# 

# %%
import requests
import time

def get_data(data_all):
    
    fore1_history={}
    
    #获取12.31的索引，索引之前的用2020，索引之后的用2021
    
    
    
    if len(data_all["data"][0]["trend"]["updateDate"])>300:
        
        NUM_1 = data_all["data"][0]["trend"]["updateDate"].index('12.31')

        for j in range(0,NUM_1+1):

            ds='2020.'+data_all["data"][0]["trend"]["updateDate"][j]

            tup=time.strptime(ds,'%Y.%m.%d')

            ds=time.strftime('%Y-%m-%d',tup)

            confirm=data_all["data"][0]["trend"]["list"][0]["data"][j]

            heal=data_all["data"][0]["trend"]["list"][1]["data"][j]

            dead=data_all["data"][0]["trend"]["list"][2]["data"][j]

            add=data_all["data"][0]["trend"]["list"][3]["data"][j]

            fore1_history[ds]={'confirm':confirm,'heal':heal,'dead':dead,'add':add}

            #history[i]=fore_history

        for k in range(NUM_1+1,len(data_all["data"][0]["trend"]["updateDate"])):

            ds='2021.'+data_all["data"][0]["trend"]["updateDate"][k]

            tup=time.strptime(ds,'%Y.%m.%d')

            ds=time.strftime('%Y-%m-%d',tup)

            confirm=data_all["data"][0]["trend"]["list"][0]["data"][k]

            heal=data_all["data"][0]["trend"]["list"][1]["data"][k]

            dead=data_all["data"][0]["trend"]["list"][2]["data"][k]

            add=data_all["data"][0]["trend"]["list"][3]["data"][k]

            fore1_history[ds]={'confirm':confirm,'heal':heal,'dead':dead,'add':add}
            
    else:
        
        for k in range(0,len(data_all["data"][0]["trend"]["updateDate"])):
            

            ds='2020.'+data_all["data"][0]["trend"]["updateDate"][k]

            tup=time.strptime(ds,'%Y.%m.%d')

            ds=time.strftime('%Y-%m-%d',tup)

            confirm=data_all["data"][0]["trend"]["list"][0]["data"][k]

            heal=data_all["data"][0]["trend"]["list"][1]["data"][k]

            dead=data_all["data"][0]["trend"]["list"][2]["data"][k]

            add=data_all["data"][0]["trend"]["list"][3]["data"][k]

            fore1_history[ds]={'confirm':confirm,'heal':heal,'dead':dead,'add':add}
        
    return fore1_history








#爬虫：设置每半小时爬一次

def get_baidu_data():
    
    #以字典的形式返回各省每天的历史数据

    list1=['北京','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','四川','海南','贵州','云南','陕西','甘肃','青海','内蒙古','广西','西藏','宁夏','新疆','台湾','香港','澳门']

    
    #list1=['澳门']


    history={}
    
    for i in list1:
        
        url='https://voice.baidu.com/newpneumonia/getv2?target=trend&isCaseIn=1&from=mola-virus&area='+str(i)+'&stage=publish'
        
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"
        }

        res = requests.get(url=url,headers=head)

        res.encoding = "utf-8"

        html = res.text

        d = json.loads(html)

        data_all = d
        
        if i=='澳门':
            
            data_all["data"][0]["trend"]["list"][3]["data"].append(0)
            
            #print(data_all["data"][0]["trend"]["list"][3]["data"])
            
        if i=='香港':
            
            data_all["data"][0]["trend"]["list"][3]["data"].append(0)
            
            data_all["data"][0]["trend"]["list"][3]["data"].append(0)
            
            #print(data_all["data"][0]["trend"]["list"][3]["data"])
        
        #print(data_all["data"][0]["trend"]["updateDate"])
        
        #print(data_all["data"][0]["trend"]["list"][3]["data"])
        
        history[i] = get_data(data_all)
        
    return history
        
#         print(data_all["data"][0]["trend"]["updateDate"].index('12.31'))
        
#         print(data_all["data"][0]["trend"]["updateDate"])
            
    
            
            
                       
                       
                       
                       
                       
                       
                       
                       
                       
                       
      
      


# %%
print(get_baidu_data())


# %%

#可以先判断数据是否更新


def data_trend():

    #返回各地每月15日的confirm，heal，dead，add

    list_1=['2020-02-15','2020-03-15','2020-04-15','2020-05-15','2020-06-15','2020-07-15','2020-08-15','2020-09-15','2020-10-15','2020-11-15','2020-12-15','2021-01-15','2021-02-15','2021-03-16','2021-04-15']

    list_2=['北京','天津','上海','重庆','河北','山西','辽宁','吉林','黑龙江','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','四川','海南','贵州','云南','陕西','甘肃','青海','内蒙古','广西','西藏','宁夏','新疆']


    dict_1_1={}

    dict_1_2 = get_baidu_data()

    for i_3 in list_1:
        
        list_5=[]

        for i_4 in list_2:

            list_5.append(dict_1_2[i_4][i_3])

        dict_1_1[i_3]=list_5
    
    return dict_1_1


# %%
print((data_trend()['2020-06-15']))


# %%
#做疫情变化趋势图时所需

def data_trend_add():
    
    #返回每月15日全国的confirm，heal，dead，add
    
    list_1=['2020-02-15','2020-03-15','2020-04-15','2020-05-15','2020-06-15','2020-07-15','2020-08-15','2020-09-15','2020-10-15','2020-11-15','2020-12-15','2021-01-15','2021-02-15','2021-03-16','2021-04-15']
    
    dict=data_trend()
    
    list=[]
    
   
    
    dict_2={}
    
    num=len(dict['2020-02-15'])
    
    for k in list_1:
        
        dict_1={}
        
        sum_confirm=0
    
        sum_heal=0
    
        sum_dead=0
    
        sum_add=0
    
        for i in range(0,num):
            
            sum_confirm+=dict[k][i]['confirm']
            
            sum_heal+=dict[k][i]['heal']
            
            sum_dead+=dict[k][i]['dead']
            
            sum_add+=dict[k][i]['add']
            
        dict_1['confirm']=sum_confirm
        
        dict_1['heal']=sum_heal
        
        dict_1['dead']=sum_dead
        
        dict_1['add']=sum_add
        
        dict_2[k]=dict_1
    
    return dict_2
        
        
    


# %%
print(data_trend_add())


# %%
#增量分析

#累计新增，新增治愈，新增死亡，新增感染

def add_data():
    
    #以列表返回时间-累计增加-新增治愈-新增死亡-新增感染
    
    dict1=data_trend_add()
    
    list2=[]
    
    
    
    list1=list(dict1)
    
    for i in range(0,(len(list1)-1)):
    
        list3=[]
    
        confirm_add = dict1[list1[i+1]]['confirm']-dict1[list1[i]]['confirm']
        
        heal_add = dict1[list1[i+1]]['heal']-dict1[list1[i]]['heal']
        
        dead_add = dict1[list1[i+1]]['dead']-dict1[list1[i]]['dead']
        
        add_add = dict1[list1[i+1]]['add']
        
        list3.append(confirm_add)
        
        list3.append(heal_add)
        
        list3.append(dead_add)
        
        list3.append(add_add)
        
        list2.append(list1[i+1])
        
        list2.append(list3)
        
    return list2
        
        
        
        
        
        
        
                   
                   
        
        
    


















# %%
print(add_data())


# %%
#创建连接--数据库




#断开连接




# %%
#主要的爬虫程序，定时执行

def dict_date():
    
    #返回列表 [日期，省份，confirm，heal，dead，add]

    data_dict=get_baidu_data()

    list_3=list(data_dict)           #以省份为主键

    list1=[]
    
    list_4=list(data_dict[list_3[0]])   #找到北京的完整日期

    for i_1 in list_4:
        
        for i_2 in list_3:
            
            list2=[]
            
            #data_dict[i_2][i_1]['date']='NONE'
            #data_dict[i_2][i_1]['province']='NONE'

            #如果对应位置没有数据则pass
            try:
                #data_dict[i_2][i_1]['date']='NONE'
                
                #data_dict[i_2][i_1]['province']='NONE'
                
                list2.append(i_1)
                
                list2.append(i_2)
                
                list2.append(data_dict[i_2][i_1].get('confirm'))
                
                list2.append(data_dict[i_2][i_1].get('heal'))
                
                list2.append(data_dict[i_2][i_1].get('dead'))
                
                list2.append(data_dict[i_2][i_1].get('add'))
                
            except:
                
                #list2.append(i_1)
                
                #list2.append(i_2)
                
                list2.append(None)
                
                list2.append(None)
                
                list2.append(None)
                
                list2.append(None)
                
            list1.append(list2)

                #print({'confirm': None, 'heal': None, 'dead': None, 'add': None, 'date':i_1, 'province':i_2})
                
    return list1




# %%
spider_list = dict_date()

print(spider_list)


# %%
#后面绘制剩余疫情人数分布图时需要

#初始化剩余人数



def surplus_1():
        
    #当前剩余人数=当前累计人数-治愈人数-死亡人数
    
    #以列表的形式返回当前剩余感染人数
    
    #后面用来做感染人数分布图
    
    data_dict=get_baidu_data()
    
    list1=list(data_dict)           #以省份为主键
    
    list2=list(data_dict[list1[0]])
    
         #最新日期list2[-1] 
        
    list4=[]
    
    print(list2[-1])
        
    for j in list1:
        
        list3=[]
        
        try:
                
            list3.append(list2[-1])
            
            list3.append(j)
                
            data = data_dict[j][list2[-1]].get('confirm')-data_dict[j][list2[-1]].get('heal')-data_dict[j][list2[-1]].get('dead')
            
            list3.append(data)
 
        except:
                
                #list2.append(i_1)
                
                #list2.append(i_2)
                
            list3.append(None)
                
        list4.append(list3)

                #print({'confirm': None, 'heal': None, 'dead': None, 'add': None, 'date':i_1, 'province':i_2})
                
    return list4


    
#[(16049, datetime.datetime(2021, 5, 12, 0, 0), '北京', 1057, 1046, 9, 0), (16

#list1[0][1][0]


#[(16083, datetime.datetime(2021, 5, 13, 0, 0), '北京', 1057, 1046, 9, 0), (
    
def surplus_2(list0):
        
    #当前剩余人数=当前累计人数-治愈人数-死亡人数
    
    #以列表的形式返回当前剩余感染人数
    
    #后面用来做感染人数分布图
    
    list4=[]
    
    data_list1=list0
    
    for i in data_list1:
        
        list3=[]
        
        try:
            
            list3.append(i[1])
            
            list3.append(i[2])
                
            data = i[3]-i[4]-i[5]
            
            list3.append(data)
            
        except:
            
            list3.append(None)
            
        list4.append(list3)
        
    return list4





# %%
#初始化剩余人数列表surplus_1_list

surplus_1_list = surplus_1()

print((surplus_1_list))


# %%
'''需要往数据库中存入的数据包括:
1.全国各省历史感染数据：时间-省份-confirm-heal-dead-add
2.全国所有省总的感染数据：时间-confirm-heal-dead-add  以一个月为周期
3.全国各省最新剩余感染人数：时间-省份-剩余人数
4.新增人数列表，新增趋势  以1个月为周期
5.当前剩余人数前5省份，剩余人数top5'''

#新增数据


def surplus_top_5():
    
    #返回剩余感染top5
    
    list1=surplus_1_list
    
    for k in range(0,len(list1)):
    
        if list1[k][2]==None:

            list1[k][2]=0
        
    
    list2=[]
    
    
    
    for i in range(0,5):
        
        for j in range(0,((len(list1)-1)-i)):
            
            if list1[j][2]>list1[j+1][2]:
                
                x=list1[j]
                
                list1[j]=list1[j+1]
                
                list1[j+1]=x
                
            else:
                
                pass
            
    list2.append(list1[-1])
    
    list2.append(list1[-2])
    
    list2.append(list1[-3])
    
    list2.append(list1[-4])
    
    list2.append(list1[-5])
    
    return list2

def surplus_top5(list0):
    
    #从传入的最新剩余列表list1中找到人数最多的5个地区
    
    list1=list0
    
    for k in range(0,len(list1)):
    
        if list1[k][2]==None:

            list1[k][2]=0
        
    
    list2=[]
    
    
    
    for i in range(0,5):
        
        for j in range(0,((len(list1)-1)-i)):
            
            if list1[j][2]>list1[j+1][2]:
                
                x=list1[j]
                
                list1[j]=list1[j+1]
                
                list1[j+1]=x
                
            else:
                
                pass
            
    list2.append(list1[-1])
    
    list2.append(list1[-2])
    
    list2.append(list1[-3])
    
    list2.append(list1[-4])
    
    list2.append(list1[-5])
    
    return list2
    
    
                
                
        



# %%
print(surplus_top_5())


# %%
# 建立连接
import pymysql
import time
import json
import traceback


# %%
def get_conn():
    
    conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='cov'
    )

    cursor=conn.cursor()
    
    return conn,cursor

    #sql='insert into runoob123 values(%s,%s,%s,%s)'  #增

    #(99,87,76,strftime(%Y-%m-%d))

    #sql='delete from runoob123 where runoob_id=1'   #删

    #sql='update runoob123 set runoob_title=31 where runoob_id=4'                 #改

    #sql='select * from runoob123'   #查

    #cursor.execute(sql,[11,87,76,time.strftime('%Y-%m-%d')])

    #conn.commit()

    #res=cursor.fetchall()

    #print(res)
    
def close_conn(conn,cursor):

    cursor.close()

    conn.close()


# %%
import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='cov'
)

cursor=conn.cursor()


#sql="insert into chaina_yq(datetime,province,confirm,heal,dead,add23) values(%s,%s,%s,%s,%s,%s)"  #增

#(99,87,76,strftime(%Y-%m-%d))

#sql='delete from runoob123 where runoob_id=1'   #删

sql='update current_data set confirm=104764 where id=1'                 #改

#sql='select * from runoob123'   #查

cursor.execute(sql)

conn.commit()

#res=cursor.fetchall()

#print(res)


cursor.close()

conn.close()


# %%
#更新数据

#初始化各省所有数据列表

List_all = dict_date()

print(len(List_all))


# %%
'''将List_all的最新日期与dict_date()返回的最新日期做对比，如果不等增在List_all中插入各省最新数据，并在数据库中插入最新数据

下次执行时，继续将List_all的最新日期与dict_date()通过爬虫返回的最新日期做对比

  List_all列表  的更新和数据库的更新

还要  同步更新  各省剩余感染人数列表  今天剩余 = 昨天剩余-(今天累计治愈-昨天累计治愈）-(今天累计死亡-昨天累计死亡）+今天新增感染
更新剩余人数列表surplus_1_list

      同步更新  top5列表，利用最新的surplus_1_list排序找到top5'''

#  本节函数  

#全国各省详细数据初始化写入及每日更新

#全国各省剩余感染人数分布

#全国剩余感染人数top5                           #一小时比较一次


#全国疫情总体变化趋势  累计感染曲线--累计治愈曲线--累计死亡曲线

#全国总体感染人数增量趋势   新增治愈曲线--新增死亡曲线--新增感染曲线


#全国最新感染数据  累计感染--累计治愈--累计死亡

#百度热搜词云图  字号越大热度越高


#写入数据库函数  初始化

def write_List_all():
    
    #初始化数据
    
    conn=None
    
    cursor=None
    
    try:         
        
        conn,cursor=get_conn()
        
        sql='insert into chaina_yq (datetime1,province,confirm,heal,dead,add1) values (%s,%s,%s,%s,%s,%s)'
    
        print('开始插入数据')
        
        for i in List_all:
                
            cursor.execute(sql,i)
                
        conn.commit()
            
        print('插入完毕')
        
        
    except:
        
        traceback.print_exc()
        
    finally:
        
        close_conn(conn,cursor)
    
#     k=1
    
#     list1=[['2020-01-31','重庆',3,4,5,6]]
    
#     try:
        
#         conn,cursor=get_conn()
        
#         sql='insert into chaina_yq (datetime1,province,confirm,heal,dead,add1) values (%s,%s,%s,%s,%s,%s)'
        
#         for item in list1:
            
#             print(item)
                
#             cursor.execute(sql,item)
                
#         conn.commit()
        
#         #close_conn(conn,cursor)
        
#     except:
        
#         traceback.print_exc()
        
#     finally:
        
#         close_conn(conn,cursor)


#清空数据表

def clear__chaina_yq():
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE chaina_yq'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor)
    
    

def clear__province_surplus():
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE province_surplus'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor)
    
    
def clear__total_trend():
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE total_trend'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor)
    
    
def clear__add_trend():
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE add_trend'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor)    
    
    
def clear__current_data():
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE current_data'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor) 
    
  

def clear__baidu_hot():
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE baidu_hot'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor) 
    
    
    
    
    
    
    
    
    
    

def clear__top5():
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()

    sql1='TRUNCATE TABLE top5'

    cursor.execute(sql1)

    conn.commit()

    close_conn(conn,cursor)
    
    
    
    
    
    
    
    
    
    
    




def write_surplus_all():
    
    #初始化数据
    
    conn=None
    
    cursor=None
    
    try:         
        
        conn,cursor=get_conn()
        
        sql='insert into province_surplus (datetime1,province,surplus1) values (%s,%s,%s)'
    
        print('开始插入数据')
        
        for i in surplus_1_list:
                
            cursor.execute(sql,i)
                
        conn.commit()
            
        print('插入完毕')
        
        
    except:
        
        traceback.print_exc()
        
    finally:
        
        close_conn(conn,cursor)
        
        
        
        #将surplus_top_5返回的列表写入top5数据库
        
def write_top5():
    
    #初始化数据
    
    conn=None
    
    cursor=None
    
    try:         
        
        conn,cursor=get_conn()
        
        sql='insert into top5 (datetime1,province,surplus1) values (%s,%s,%s)'
    
        print('开始插入数据')
        
        for i in surplus_top_5():
                
            cursor.execute(sql,i)
                
        conn.commit()
            
        print('插入完毕')
        
        
    except:
        
        traceback.print_exc()
        
    finally:
        
        close_conn(conn,cursor)

        
        


        


# %%
#print(write_surplus_all())

print(write_top5())


# %%
#更新数据库

#List_all[-1][0]？=dict_date()[-1][0]

def update_List_all():
    
    conn=None
    
    cursor=None
    
    list1=spider_list
    
    if List_all[-1][0]!=list1[-1][0]:
        
        try:
        
            print('开始更新数据')

            conn,cursor=get_conn()

            sql='insert into chaina_yq (datetime1,province,confirm,heal,dead,add1) values (%s,%s,%s,%s,%s,%s)'

            for i in range(-34,0):

                cursor.execute(sql,list1[i])

                List_all.append(list1[i])

            conn.commit()

            print('插入完毕')
        
        except:
        
            traceback.print_exc()
        
        finally:
        
            close_conn(conn,cursor)
            
    else:
        
        print('已是最新数据')
        
        

    
    
    
    
    
    
    
        


# %%
def read_chaina_yq():
#从数据库读数据

#返回最新日期

    conn=None

    cursor=None

    conn,cursor=get_conn()

    #select * FROM z_cashier_data where id = (SELECT max(z_cashier_data.id) from z_cashier_data where abstract_code = "1001");

    sql1='select datetime1 from chaina_yq where num=(select max(num) from chaina_yq)'  #where num=1(select max(chaina_yq.num) from chaina_yq)

    cursor.execute(sql1)

    res1=cursor.fetchone()  #res=cursor.fetchall()

    #conn.commit()

    #return res

    

    close_conn(conn,cursor)
    
    return res1[0]


def read_province_surplus():
#从数据库读数据

#返回最新日期

    conn=None

    cursor=None

    conn,cursor=get_conn()

    #select * FROM z_cashier_data where id = (SELECT max(z_cashier_data.id) from z_cashier_data where abstract_code = "1001");

    sql1='select datetime1 from province_surplus where id=1'  #where num=1(select max(chaina_yq.num) from chaina_yq)

    cursor.execute(sql1)

    res1=cursor.fetchone()  #res=cursor.fetchall()

    #conn.commit()

    #return res

    

    close_conn(conn,cursor)
    
    return res1[0]



def read_province_surplus1():
    
    #返回剩余列表数据（一共34个）
    
    
    
    list2=[]
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()
    
    
    for i in range(1,35):
        
        list1=[]

        #print(i)

        res2=0
    
        sql2='select * from province_surplus where id=%s'

        cursor.execute(sql2,i)

        res2=cursor.fetchone()
        
        #print(res2)
        
        #print(res2[1])
        
        list1.append(res2[1])
        
        list1.append(res2[2])
        
        list1.append(res2[3])

        list2.append(list1)
        
    close_conn(conn,cursor)
        
    return list2
    
    




def read_top5():
#从top5数据库读数据

#返回最新日期

    conn=None

    cursor=None

    conn,cursor=get_conn()

    #select * FROM z_cashier_data where id = (SELECT max(z_cashier_data.id) from z_cashier_data where abstract_code = "1001");

    sql1='select datetime1 from top5 where id=1'  #where num=1(select max(chaina_yq.num) from chaina_yq)

    cursor.execute(sql1)

    res1=cursor.fetchone()  #res=cursor.fetchall()

    #conn.commit()

    #return res

    

    close_conn(conn,cursor)
    
    return res1[0]



    
    
    
    


# %%
#print(read_List_all())

print(read_top5())

print(read_province_surplus1())

#print(read_province_surplus())


# %%
import datetime

def read_province_data():
    #读取数据库并返回34个省最新数据----列表-元组
    
    conn,cursor=get_conn()
    
    sql1='select max(num) from chaina_yq'
    
    cursor.execute(sql1)

    res1=cursor.fetchone()
    
    #print(res1[0])
    
    close_conn(conn,cursor)
    
    list1=[]
    
    conn=None

    cursor=None
    
    conn,cursor=get_conn()
    
    
    for i in range(res1[0]-33,res1[0]+1):

        #print(i)

        res2=0
    
        sql2='select * from chaina_yq where num=%s'

        cursor.execute(sql2,i)

        res2=cursor.fetchone()
        
        #print(res2)

        list1.append(res2)
        
    close_conn(conn,cursor)
        
    return list1

def read_spider_list():
    
    list1=[]
    
    list2=[]
    
    #返回爬虫列表的最新的34个数据,以列表返回最新一天的34个省份数据
    
    list1=spider_list
    
    #print(list1[-33])
    
    for i in range(-34,0):
        
        list2.append(list1[i])
        
    #print(list2)
        
    #for j in range(0,34):

        #list2[j][0]=datetime.datetime.strptime(z,'%Y-%m-%d')
        
    return list2
    
    #return datetime.datetime.strptime(list2[0][0],'%Y-%m-%d')
    
    
    
    
    
    

    


# %%
#print(read_province_data())

print(read_spider_list())


# %%
#更新各省剩余感染人数  ['2021-05-11', '北京', 2]

def updata_province_surplus():
    
    conn=None
    
    cursor=None
    
    List1=[]
    
    List2=[]
    
    spider_list[-1][0]
    
    #print(spider_list)
    
    

    if surplus_1_list[0][0]!=spider_list[-1][0]:
        
        

        #TRUNCATE TABLE 表名  删除旧数据
        conn,cursor=get_conn()

        sql1='TRUNCATE TABLE Province_surplus'

        cursor.execute(sql1)

        conn.commit()

        close_conn(conn,cursor)

        conn=None

        cursor=None


        #更新数据





        for i in range(-34,0):  #今日数据

            List1.append(spider_list[i])

        for j in range(-68,-34):  #昨日数据

            List2.append(spider_list[i])

        #今天剩余 = 昨天剩余-(今天累计治愈-昨天累计治愈）-(今天累计死亡-昨天累计死亡）+今天新增感染

        for m in range(0,34):
            
            try:

                surplus_1_list[m][2]=int(surplus_1_list[m][2])-(int(List1[m][3])-int(List2[m][3]))-(int(List1[m][4])-int(List2[m][4]))+int(List1[m][5])

            except:
                
                surplus_1_list[m][2]=None
                
        print('开始更新数据')

        conn,cursor=get_conn()

        sql='insert into Province_surplus (datetime1,province,surplus1) values (%s,%s,%s)'
            
        for n in surplus_1_list:

            cursor.execute(sql,n)

        conn.commit()

        print('插入完毕')

        close_conn(conn,cursor)
            
            #traceback.print_exc()

    else:

        print('已是最新数据')





# %%
#更新每个省剩余感染人数列表，---先从拿到数据库最新日期，查询剩余列表的最新日期，如果两者不等则清空剩余列表然后
#计算剩余人数并写入剩余列表
def updata_province_surplus1():
    
    #read_province_data
    
    if read_province_surplus()!=read_chaina_yq():
        
        clear__province_surplus()

        print('开始更新剩余感染人数')

        list1=read_province_data()

        #print(list1)

        list2=surplus_2(list1)

        #print(list2)

        conn=None

        cursor=None

        conn,cursor=get_conn()

        sql='insert into province_surplus (datetime1,province,surplus1) values (%s,%s,%s)'

        for n in list2:

            cursor.execute(sql,n)

        conn.commit()

        print('插入完毕')

        close_conn(conn,cursor)
        
    else:

        print('已是最新数据')
        
        
        
def update_province_data():
    
    #先从数据库读出最新日期，与爬虫爬取最新日期作比较，如果相等则不更新，如果不相等则更新
    
    if read_chaina_yq()!=spider_list[-1][0]:
        
        print(read_chaina_yq(),spider_list[-1][0])
        
        print('开始更新各省今日疫情数据')
        
        list1=read_province_data()
        
        #read_spider_list()返回爬虫爬取的最新34个数据--列表-列表
        
        conn=None

        cursor=None

        conn,cursor=get_conn()
        
        sql='insert into chaina_yq (datetime1,province,confirm,heal,dead,add1) value(%s,%s,%s,%s,%s,%s)'
        
        for i in read_spider_list():
            
            cursor.execute(sql,i)
            
        conn.commit()

        print('插入完毕')
        
        close_conn(conn,cursor)
        
    else:

        print('已是最新数据')
        
        
def updata_top5():
    
    #从top5数据库读取最新日期，与chaina_yq数据库中的最新日期作比较，如果相等则不更新，如果不等则更新
    
    #list1=read_province_surplus1()
    
    #print(list1)
    
    #list2=surplus_top5(list1)
        
    #print(list2)
    
    if read_top5()!=read_chaina_yq():
        
        clear__top5()

        print('开始更新各省今日疫情数据')

        list1=read_province_surplus1()

        #read_spider_list()返回爬虫爬取的最新34个数据--列表-列表

        list2=surplus_top5(list1)

        #print(list2)

        conn=None

        cursor=None

        conn,cursor=get_conn()

        sql='insert into top5 (datetime1,province,surplus1) value(%s,%s,%s)'

        for i in list2:

            cursor.execute(sql,i)

        conn.commit()

        print('插入完毕')

        close_conn(conn,cursor)
        
    else:

        print('已是最新数据')

        
        
    
    
            
        



# %%
print(updata_top5())


# %%
print(update_province_data())


# %%
print(updata_province_surplus1())


# %%
clear__province_surplus()


# %%
clear__top5()


# %%
#将  ‘全国疫情总体变化趋势  和  全国总体感染人数增量趋势‘  存入数据库    一个月更新一次

#本节函数

#全国疫情总体变化趋势  累计感染曲线--累计治愈曲线--累计死亡曲线

#全国总体感染人数增量趋势   新增治愈曲线--新增死亡曲线--新增感染曲线




#在chaina_yq列表中 取 每月15日的confirm、heal、dead数据存入新的数据库total_trend，如果为None则存入None

#用chaina_yq列表中

#获取  datetime1=‘2020-2-1’且province='北京' 的索引，取出接下来的34个数据

#从chaina_yq数据库取出'2020-2-1----2021-5-1'每月初一的数据，暂存在临时列表中，对列表中的所有confirm,heal,dead进行累加，如果没有数据就加0



def find_index():
    
    #返回北京在'2020-2-1----2021-5-1'每月初一的索引---列表
    
    list1=['2020-02-01','2020-03-01','2020-04-01','2020-05-02','2020-06-01','2020-07-01','2020-08-01','2020-09-01','2020-10-01','2020-11-01','2020-12-01','2021-01-01','2021-02-01','2021-03-01','2021-04-01','2021-05-01']
    
    list3=[]
    
    conn=None

    cursor=None

    conn,cursor=get_conn()

    sql='select num from chaina_yq where datetime1=%s and province=%s'
    
    for i in list1:
        
        list2=[]
        
        cursor.execute(sql,[i,'北京'])
        
        res1=cursor.fetchone()  #res=cursor.fetchall()
        
        list2.append(i)
        
        list2.append(res1)
        
        #print(list2[1][0])  
        
        list3.append(list2)         #用list3[0][1][0]可以拿出索引号

    conn.commit()

    close_conn(conn,cursor)
    
    return list3




def total_trend_1():
    
    #返回confirm，heal，dead每隔一月的累计数据
    
    #以索引号为起点取出连续的34个列表存入新的列表，对新列表的confirm，heal，dead进行累加，如果为空则加0
    
    #一共16个月
    
    list1=[]
    
    list2=[]
    
    list3=[]
    
    list4=[]
    
    conn=None

    cursor=None
    
    #list4=['confirm','heal','dead']
    
    #print(len(find_index()))
    
    #print(find_index()[0][1][0])
    
    for i in range(0,len(find_index())):
            
        sum1=0
        
        for j in range(0,34):

            res1=0

            conn,cursor=get_conn()

            sql='select confirm from chaina_yq where num=%s'

            cursor.execute(sql,(find_index()[i][1][0]+j))

            #print(find_index()[i][1][0]+j)

            res1=cursor.fetchone()

            #print(res1)

            try:

                sum1+=res1[0]

            except:

                sum1+=0

        list1.append(sum1)
                
    conn.commit()

    close_conn(conn,cursor)
    
    
    
    for i in range(0,len(find_index())):
            
        sum1=0
        
        for j in range(0,34):

            res1=0

            conn,cursor=get_conn()

            sql='select heal from chaina_yq where num=%s'

            cursor.execute(sql,(find_index()[i][1][0]+j))

            #print(find_index()[i][1][0]+j)

            res1=cursor.fetchone()

            #print(res1)

            try:

                sum1+=res1[0]

            except:

                sum1+=0

        list2.append(sum1)
                
    conn.commit()

    close_conn(conn,cursor)
    
    
    
    
    for i in range(0,len(find_index())):
            
        sum1=0
        
        for j in range(0,34):

            res1=0

            conn,cursor=get_conn()

            sql='select dead from chaina_yq where num=%s'

            cursor.execute(sql,(find_index()[i][1][0]+j))

            #print(find_index()[i][1][0]+j)

            res1=cursor.fetchone()

            #print(res1)

            try:

                sum1+=res1[0]

            except:

                sum1+=0

        list3.append(sum1)
                
    conn.commit()

    close_conn(conn,cursor)
    
    list4.append(list1)
    
    list4.append(list2)
    
    list4.append(list3)
    
    return list4
                










# %%

total_list=total_trend_1()

print(total_list)


# %%
#将整体趋势数据写入数据库

def write_total_trend_1():
    
    conn=None

    cursor=None
    
    list1=['2020-02-01','2020-03-01','2020-04-01','2020-05-02','2020-06-01','2020-07-01','2020-08-01','2020-09-01','2020-10-01','2020-11-01','2020-12-01','2021-01-01','2021-02-01','2021-03-01','2021-04-01','2021-05-01']
    
    list2=total_list
    
    conn,cursor=get_conn()

    sql="insert into total_trend(datetime1,confirm,heal,dead) value(%s,%s,%s,%s)"

    for i in range(0,len(list1)):

        cursor.execute(sql,[list1[i],list2[0][i],list2[1][i],list2[2][i]])

    conn.commit()
    
    close_conn(conn,cursor)
        
        
        
        
    
    
    
    
    


# %%
clear__total_trend()

print(write_total_trend_1())


# %%



# %%
#对total_list中的数据做减法，计算增加趋势

def add_trend():
    
    list1=[]
    
    list2=[]
    
    list3=[]
    
    list4=[]
    
    for i in range(0,len(total_list[0])-1):
        
        x = total_list[0][i+1]-total_list[0][i]
        
        y = total_list[1][i+1]-total_list[1][i]
        
        z = total_list[2][i+1]-total_list[2][i]
        
        list1.append(x)
        
        list2.append(y)
        
        list3.append(z)
        
    list4.append(list1)
    
    list4.append(list2)
    
    list4.append(list3)
        
    return list4
    


# %%


print(add_trend())


# %%
#将整体增加趋势数据写入数据库

def write_add_trend():
    
    conn=None

    cursor=None
    
    list1=['2020-02-01','2020-03-01','2020-04-01','2020-05-02','2020-06-01','2020-07-01','2020-08-01','2020-09-01','2020-10-01','2020-11-01','2020-12-01','2021-01-01','2021-02-01','2021-03-01','2021-04-01']
    
    list2=add_trend()
    
    conn,cursor=get_conn()

    sql="insert into add_trend(datetime1,confirm,heal,dead) value(%s,%s,%s,%s)"

    for i in range(0,len(list1)):

        cursor.execute(sql,[list1[i],list2[0][i],list2[1][i],list2[2][i]])

    conn.commit()
    
    close_conn(conn,cursor)


# %%
#插入新增数据

print(write_add_trend())


# %%
print(find_index()[15][1][0])


# %%
#执行爬虫爬取  全国最新感染数据  和  百度热搜热点词汇  ，可以设置5分钟执行一次，如果网站更新数据则将新的感染数据写入数据库，

#将新的百度搜索题目（前20条）存入数据库

#本节函数

#全国最新感染数据  累计感染--累计治愈--累计死亡          实时爬取--每5分钟爬一次

#百度热搜词云图  字号越大热度越高                        每天爬前20条

url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab1'

from selenium.webdriver import Chrome,ChromeOptions

option=ChromeOptions()

option.add_argument("--headless")  #去头

option.add_argument("--no-sandbox")

browser=Chrome(options=option)

browser.get(url)

time.sleep(1)

but=browser.find_element_by_css_selector('#ptab-1 > div.Virus_1-1-302_2SKAfr > div.Common_1-1-302_3lDRV2 > span')

but.click()

c=browser.find_elements_by_xpath('//*[@id="ptab-1"]/div[3]/div/div[2]/a/div ')

for i in c:

    print(i.text)


# %%
#将百度热搜用列表返回
from selenium.webdriver import Chrome,ChromeOptions
import pymysql
def baidu_hot_content():
    
    list1=[]
    
    url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab1'
    
    option=ChromeOptions()

    option.add_argument("--headless")  #去头

    option.add_argument("--no-sandbox")

    browser=Chrome(options=option)

    browser.get(url)

    time.sleep(1)

    but=browser.find_element_by_css_selector('#ptab-1 > div.Virus_1-1-302_2SKAfr > div.Common_1-1-302_3lDRV2 > span')

    but.click()

    c=browser.find_elements_by_xpath('//*[@id="ptab-1"]/div[3]/div/div[2]/a/div ')

    for i in c:

        list1.append(i.text)
        
    return list1


#将热搜依次存入数据库

def write_hot_content():
    
    conn=None
    
    cursor=None
    
    list1=baidu_hot_content()
    
    conn,cursor=get_conn()
    
    sql="insert into baidu_hot(datetime1,content) value(%s,%s)"
    
    ds=time.strftime('%Y-%m-%d %X')
    
    for i in range(0,len(list1)):
        
        cursor.execute(sql,(ds,list1[i]))
        
    conn.commit()
    
    close_conn(conn,cursor)



# %%
clear__baidu_hot()
write_hot_content()


# %%
from bs4 import BeautifulSoup
import requests
import re

url = "https://www.360kuai.com/mob/subject/400?sign=360_6aa05217"
res = requests.get(url)

res.encoding = "utf-8"

html = res.text

soup = BeautifulSoup(html)

#print(html)
#print(soup)
#print(soup.find('h2').text)

pat='"feiyanTrend":{"total":{"diagnosed":(.*?),"suspected":".*?","overseasInput":.*?,"died":(.*?),"cured":(.*?),"serious":".*?","asymptom":.*?,"currentConfirmed":.*?,"modifyTime":"(.*?)","dailyPic":""}'

a=re.findall(pat,html)

#print(a[0])

clear__current_data()

conn,cursor=get_conn()
    
sql="insert into current_data(confirm,dead,heal,dt) value(%s,%s,%s,%s)"

cursor.execute(sql,(a[0]))

conn.commit()

close_conn(conn,cursor)


#a=soup.find('div',class_="contMain")


#b = a.find_all('a')

#for i in b:
    #print(i.attrs["href"])


