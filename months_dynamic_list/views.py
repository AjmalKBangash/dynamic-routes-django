from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from monthly_dynamic_list_in_templates import models as tem_models
import json
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

currenturl = ''
def months(request):
    monthsList = ""
    for month in list(monthsinStr.keys()):
        redir = reverse("months-description", args=[month])
        monthsList += f"<li><a href=\"{redir}\">{month}</a></li>" 
    return HttpResponse(f"<ul>{monthsList}</ul>")

def monthslist(request, monthsl):
    ''' this is fetching data from django models and converting that python objects to json format using JsonResponse
    vari = list(tem_models.monthsurlhistory.objects.all().values())
    print("This is model")
    # print(vari)
    jsonn = JsonResponse(vari, safe = False)
    # print(json.dumps(jsonn.content))  json.dumps() method is used to encodes any Python object into JSON formatted String.
    res = json.loads(jsonn.content)     json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
    print(res[0].get('urlhistory'))

    the second shift is for practicing
    
    vari = list(tem_models.monthsurlhistory.objects.all().values())
    print("This is model")
    print(vari)
    print("this is json now")
    print(json.dumps(vari))
    '''
    # Now we saving data to django models(Database)
    currenturl = request._current_scheme_host+request.path
    urlhistoryy = tem_models.monthsurlhistory(
        urlhistory = currenturl
    )
    if currenturl == 'http://127.0.0.1:8000/favicon.ico':
        pass
    else:
        urlhistoryy.save()
    # urlhistory.save(currenturl) this is wrong buddy see up
    
    
    var = list(monthsinStr.keys())
    for i in monthsinStr:
        try:
            if (monthsl.lower() == i):
                return (HttpResponse(monthsinStr.get(monthsl.lower())))
            elif int(monthsl) < 13 and int(monthsl) > 0 and monthsinStr.get(var[int(monthsl) - 1]):
                return (HttpResponse(monthsinStr.get(var[int(monthsl) - 1]))) 
        except ValueError:
            pass
            
    return HttpResponse(f"The url you entered '{monthsl}' is incorrect! ")







