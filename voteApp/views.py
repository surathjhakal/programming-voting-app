from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
count = {}
languages = ['python', 'c', 'c++', 'java', 'dotnet',
             'perl', 'javascript', 'go', 'kotlin', 'bash', 'c#', 'sql', 'php', 'swift']


def index(request):
    mydict = {
        'languages': languages
    }
    return render(request, 'index.html', context=mydict)


def getQuery(request):
    value = request.POST['query']
    if value in languages:
        if value not in count:
            count[value] = 1
        else:
            count[value] += 1
    else:
        print("Nothing")
    myDict = {'globalCount': count, 'languages': languages}
    return render(request, 'index.html', context=myDict)


def sortdata(request):
    global count
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    print(count)
    mydictionary = {
        "languages": languages,
        "globalCount": count
    }
    return render(request, 'index.html', context=mydictionary)
