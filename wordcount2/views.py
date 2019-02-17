from django.http import HttpResponse # Renders strings
from django.shortcuts import render # Renders HTML pages
import operator

def home(request):
    return render(request, 'home.html', {'Test': 'This is passed in through the dictionary.'})

def eggs(request):
    return HttpResponse('Eggs are great!')

def count(request):
    fulltextVar = request.GET['fulltext'] # This will grab all the text
    wordList = fulltextVar.split() # This splits all the text wherever there is a space
    
    # Check to see which words appear the most.
    # Create dictionary.
    wordDictionary = {}

    # Loop through each word in the dictionary.
    for word in wordList:
        if word in wordDictionary:
            # Increase
            wordDictionary[word] += 1
        else:
            # Add word to dictioanry
            wordDictionary[word] = 1

    # We are going to sort all the items.
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    # We use the len() to get the count. Notice we used a dictionary.
    return render(request, 'count.html', {'fulltext': fulltextVar, 'count':len(wordList), 'sortOutput':sortedWords}) 

def about(request):
    return render(request, 'about.html')