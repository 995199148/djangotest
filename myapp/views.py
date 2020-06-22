from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import clientnum
from django.shortcuts import redirect

# 首页
def index(request):
    mydatalist = []
    mydatadict = {}
    # 倒叙排列 获取排名
    mydata = clientnum.objects.order_by("-num").values_list("cid","num")
    for index, line in enumerate(mydata):
        mydatalist.append([index+1] + list(line))
        mydatadict[line[0]] = [index+1] + list(line)
    request.encoding = 'utf-8'
    cid = request.GET.get('cid')
    startindex = request.GET.get('start')
    endindex = request.GET.get('end')
    # 利用切片 切取对应排名
    if startindex:
        mydatalist = mydatalist[int(startindex)-1:]
    if endindex:
        mydatalist = mydatalist[:int(endindex)-1]
    if cid:
        cindex = mydatadict.get(int(cid))
        if cindex:
            mydatalist.append(cindex)
    return render(request, "index.html", {"mydata": list(mydatalist)})


# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def postdata(request):
    ctx = {}
    if request.POST:
        cid = request.POST['cid']
        num = request.POST['num']
        # 存在的修改不存在的新增
        obj, flag = clientnum.objects.get_or_create(cid=cid)
        obj.num = num
        obj.save()
        # 操作完成重定向
        response = redirect('/')
        return response

    return render(request, "postdata.html", {})