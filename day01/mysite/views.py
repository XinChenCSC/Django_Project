from django.http import HttpResponse

def page_2003_view(request):
    html = "<h1>This is first page</h1>"
    return HttpResponse(html)
def cal_view(request,n,op,m):
    if op not in ['add','sub','mul']:
        return HttpResponse("Invaild Input")
    res = 0
    if op == 'add':
        res = n + m
    elif op == 'sub':
        res = n - m
    elif op == 'mul':
        res = n * m
    return HttpResponse("result is %s"%(res))
def cal2_view(request,x,op,y):

    html = 'x:%s op:%s y:%s'%(x,op,y)
    return HttpResponse(html)

