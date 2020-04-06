from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Habbit, Memo
import datetime

# Create your views here.

def index(req):
    startDate = datetime.datetime.now()
    nowDate = startDate.strftime('%Y/%m/%d')
    non_give_up_habbit_list = []
    for habbit in Habbit.objects.all():
        if habbit.give_up == False:
            non_give_up_habbit_list.append(habbit)
        else:
            pass
    content = {'date':nowDate,'habbits': non_give_up_habbit_list}
    return render(req, 'memoApp/index.html', content)

def record(req):
    startDate = datetime.datetime.now()
    nowDate = startDate.strftime('%Y/%m/%d')
    non_give_up_habbit_list = []
    for habbit in Habbit.objects.all():
        if habbit.give_up == True:
            non_give_up_habbit_list.append(habbit)
        else:
            pass
    for habbit in non_give_up_habbit_list:
        givenUpdate=habbit.start_datetime + datetime.timedelta(days=habbit.daysCount)
        habbit.givenup_date=givenUpdate.strftime('%Y/%m/%d')
        habbit.save()
    content = {'date':nowDate,'habbits': non_give_up_habbit_list}
    return render(req, 'memoApp/record.html', content)

def control(req):
    non_give_up_habbit_list=[]
    for habbit in Habbit.objects.all():
        if habbit.give_up==False:
            non_give_up_habbit_list.append(habbit)
        else:
            pass
    content={'habbits': non_give_up_habbit_list }
    return render(req, 'memoApp/control.html',content)

def create(req):
    habbit_name=req.POST['habbitName']
    startDate = datetime.datetime.now()
    nowDate = startDate.strftime('%Y/%m/%d')
    days66 = startDate + datetime.timedelta(days=66)
    finishDate = days66.strftime('%Y/%m/%d')
    newHabbit=Habbit(habbitName=habbit_name, startDate=nowDate, progress="", finishDate=finishDate, daysCount=0, daysFail=0, daysSucceed=0)
    newHabbit.save()
    return HttpResponseRedirect(reverse('controlPage'))

def delete(req):
    give_up_habbit=Habbit.objects.get(id=req.POST['habbitId'])
    give_up_habbit.give_up = True
    give_up_habbit.save()
    return HttpResponseRedirect(reverse('controlPage'))

def order(req):
    non_give_up_habbit_list=[]
    order_habbits=Habbit.objects.all().order_by(req.GET['by'])
    for habbit in order_habbits:
        if habbit.give_up == False:
            non_give_up_habbit_list.append(habbit)
        else:
            pass
    content = {'habbits': non_give_up_habbit_list}
    return render(req, 'memoApp/control.html', content)

def ordered(req):
    startDate = datetime.datetime.now()
    nowDate = startDate.strftime('%Y/%m/%d')
    non_give_up_habbit_list = []
    for habbit in Habbit.objects.all():
        if habbit.give_up == False:
            non_give_up_habbit_list.append(habbit)
        else:
            pass
    content = {'date':nowDate,'habbits': non_give_up_habbit_list}
    return render(req, 'memoApp/index.html', content)

def check(req):
    habbit_posted=Habbit.objects.get(id=req.POST['habbitId'])
    great_job_user=Habbit.objects.get(id=req.POST['habbitId'])
    great_job_user.progress+=">"
    great_job_user.daysSucceed+=1
    great_job_user.save()
    return HttpResponseRedirect(reverse('mainPage'))

def fix(req):
    try:
        fixed_value=Habbit.objects.get(id=req.POST['habbitId'])
        fixed_list=list(fixed_value.progress)
        fixed_list.pop()
        fixed_result="".join(fixed_list)
        fixed_value.progress=fixed_result
        fixed_value.daysSucceed-=1
        fixed_value.save()
        return HttpResponseRedirect(reverse('controlPage'))
    except Exception:
        return HttpResponseRedirect(reverse('controlPage'))

def refresh(req):
    for habbit in Habbit.objects.all():
        if habbit.give_up==False:
            time1=habbit.start_datetime
            time2=datetime.datetime.now()
            days_count=(time2-time1).days
            habbit.daysCount=int(days_count)
            habbit.daysFail=habbit.daysCount-habbit.daysSucceed
            habbit.save()
        else:
            pass
    return HttpResponseRedirect(reverse('mainPage'))

def deleteRecord(req):
    record_to_del=Habbit.objects.get(id=req.POST['recordDel'])
    record_to_del.delete()
    return HttpResponseRedirect(reverse('recordPage'))

def memo(req, habbit_id):
    go_to_memo=Habbit.objects.get(id=habbit_id)
    memo_list=[]
    habbitId=habbit_id
    for memo in Memo.objects.all():
        if int(habbitId)==int(memo.habbit.id):
            memo_list.append(memo)
    content={'memo_id':go_to_memo, 'memos': memo_list}
    return render(req, 'memoApp/memo.html', content)

def memoPage(req,habbit_id):
    if req.method=="GET":
        today=datetime.datetime.now()
        content={'date':today.strftime('%Y/%m/%d')}
        return render(req, 'memoApp/memoPage.html', content)
    else:
        new_memo=Memo(contents=req.POST['contents'], habbit=Habbit.objects.get(id=habbit_id))
        new_memo.save()
        habbitId=habbit_id
        return HttpResponseRedirect(reverse('memoPage', kwargs={'habbit_id': habbitId}))

def deleteMemo(req,habbit_id):
    habbitId=habbit_id
    delete_memo=Memo.objects.get(id=req.POST['memoId'])
    delete_memo.delete()
    return HttpResponseRedirect(reverse('memoPage', kwargs={'habbit_id': habbitId}))