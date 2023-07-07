from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render
from django.urls import reverse
# from months_dynamic_list import views as notem_views

# from . import templates

# Create your views here.
monthsinStr = {
    "january": "I will be HTML developer InshaA",
    "february": "I will be CSS developer InshaA",
    "march": "I will be Javascript expert InshaA",
    "april": "I will be React.js pro developer InshaA",
    "may": "I will be python expert InshaA",
    "june": "I will be doing react projects InshaA",
    "july": "I will be doing django projects InshaA",
    "august": "I will be making portfolio in React+Django InshaA",
    "september": "I will be practicing and participating in coding challenges InshaA",
    "october": "I will be leading the team InshaA",
    "november": "I will be developing onlne freelance InshaA",
    "december": "I am now a Full Stack Developer, InshaA",
    # "listai": [1,2,3,4,5,5,5,5,555]
}
# redir = reverse("months-description")
data = {
    "id": 5,
    "monthsinStr": monthsinStr,
    "redir": 'www.google.com'
}
def monthshistory(request):
    # res = monthsinStr.get(enter)
    currenturl = request._current_scheme_host+request.path
    print("This is path")
    print(currenturl)
    return render(request,'index.html', data)
    return HttpResponse("Salam")

def handlereverse(request):
    # currenturl2 = request.get_host()+request.path
    # print(currenturl2)
    return HttpResponse("salam")

# print(notem_views.monthslist.currenturl) the variable is not accessble