import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

from theDatas.models import TestModel
from theDatas.models import Test

from theDatas.models import ByCountry as bc
from theDatas.models import ByOverall as bo
from theDatas.models import ByWorld as bw
from theDatas.models import ByArea as ba
from theDatas.models import ByDate as bd
from theDatas.models import ByIncrease as bi
from theDatas.models import BySearchterm as bs

def index(request):
  all_data = TestModel.objects.all()
  template = loader.get_template('theDatas/index.html')
  context = {
    'all_data': all_data
  }
  # data = [td.city_name,td.new_people,td.no_new_days]
  return HttpResponse(template.render(context,request))

# 这个接口是读取本地数据的演示,如果数据库布不好就用这个做接口
# 这里的'by_date.json'位置是在同级目录
# 原理是打开一个本地文件,以二进制的形式直接写入Response
def load_test(request):
  json_data = open('by_date.json', encoding='utf-8')
  data = json_data.read(100000000)# 这个参数是最大字节数

  return JsonResponse(data,safe=False)

def new_load_test(request):
  # all_data = Test.objects.all()
  all = Test.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data,encoding='utf-8')
  return JsonResponse(data=data,safe=False)

def by_country(request):
  all = bc.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data,encoding='utf-8')
  return JsonResponse(data=data,safe=False)

def by_overall(request):
  all = bo.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data, encoding='utf-8')
  return JsonResponse(data=data, safe=False)

def by_world(request):
  all = bw.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data, encoding='utf-8')
  return JsonResponse(data=data, safe=False)

def by_area(request):
  all = ba.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data, encoding='utf-8')
  return JsonResponse(data=data, safe=False)

def by_date(request):
  all = bd.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data, encoding='utf-8')
  return JsonResponse(data=data, safe=False)

def by_increase(request):
  all = bi.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data, encoding='utf-8')
  return JsonResponse(data=data, safe=False)

def by_searchterm(request):
  all = bs.objects.all()
  all_data = all.to_json()
  data = json.loads(all_data, encoding='utf-8')
  return JsonResponse(data=data, safe=False)