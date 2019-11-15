from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404

def demo(request):
    return HttpResponse('<h1>Anh yêu  <a href= ''https://www.facebook.com/heoheo.linhlinh?epa=SEARCH_BOX''>Linh Vũ</a></h1>')


# def detail(request, question_id):
#     return HttpResponse('Your ID is {}'.format(question_id))


def index(request):
    latest_question_list = Question.objects.order_by('-id')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

# def detail_1(request, question_id):
#     try:
#         if Question.objects.filter(id=question_id).exists():
#             return render(request, 'polls/index.html')
#     except:
#         raise Http404('Not found!')


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    #
    # except:
    #     raise Http404("Can not found")
    # return render(request, "polls/detail.html", {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/index.html', {'question': question})


def result(request, question_id):
    return HttpResponse("You are looking for question {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("You are voting for question {}".format(question_id))