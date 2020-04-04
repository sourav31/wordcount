from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordtot = fulltext.split()
    worddict = {}

    for word in wordtot:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedword = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html',{"fulltext":fulltext, "wordtot":len(wordtot), "worddict":worddict, "wordlist":worddict.items(), "sortedword":sortedword})


def about(request):
    return render(request, 'about.html')
