from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world . Long dep trai')


def demo(request):
    return HttpResponse('<h1>Anh yêu em <a href= ''https://www.facebook.com/heoheo.linhlinh?epa=SEARCH_BOX''>Linh Vũ</a></h1>')