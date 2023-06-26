from django.http import HttpResponse
from django.urls import reverse
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

}


def months(request):
    monthsList = ""
    for month in list(monthsinStr.keys()):
        redir = reverse("months-description", args=[month])
        monthsList += f"<li><a href=\"{redir}\">{month}</a></li>" 
    return HttpResponse(f"<ul>{monthsList}</ul>")

def monthslist(request, monthsl):
    var = list(monthsinStr.keys())
    for i in monthsinStr:
        if (monthsl.lower() == i):
            return (HttpResponse(monthsinStr.get(monthsl.lower())))
        elif int(monthsl) < 13 and int(monthsl) > 0 and monthsinStr.get(var[int(monthsl) - 1]):
            return (HttpResponse(monthsinStr.get(var[int(monthsl) - 1]))) 
        else:
            return HttpResponse(f"The url you entered '{monthsl}' is incorrect! ")







