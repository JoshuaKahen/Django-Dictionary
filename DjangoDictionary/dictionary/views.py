# the render function renders templates
from django.shortcuts import render
from PyDictionary import PyDictionary

# this is the view that will render the index page
def homeView(request):
    title = {
    'word': "Dictionary made with Django"
    }
    return render(request, 'dictionary/index.html', title)

# this is the view that will render search page
def searchView(request):
    
    word = request.GET.get('search')
    dictionary = PyDictionary()

    meanings = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    
    context = {
            'word': word,
            'meanings':meanings,
            'synonyms':synonyms,
            'antonoyms':antonyms
        }
    return render(request, 'dictionary/search.html', context)