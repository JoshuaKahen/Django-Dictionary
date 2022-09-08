# the render function renders templates
from django.shortcuts import render
import bs4
import requests

# this is the view that will render the index page
def homeView(request):
    title = {
    'word': "Dictionary made with Django"
    }
    return render(request, 'dictionary/index.html', title)

# this is the view that will render search page
def searchView(request):
    
    word = request.GET.get('search')

    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://www.thesaurus.com/browse/'+word)
    se = ""
    ae = ""

    if res:
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value': '1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''

    if res2:
        soup2 = bs4.BeautifulSoup(res2.text, 'lxml')

        synonyms = soup2.find('div', {'class':'css-ixatld e15rdun50'}).find_all('a', {'class':'css-1kg1yv8 eh475bn0'})
        ss = []

        for b in synonyms[0:]:
            re = b.text.strip()
            ss.append(re)
        se = ss
        

        antonyms = soup2.find_all('a', {'class':'css-15bafsg eh475bn0'})
        aa = []
        for c in antonyms[0:]:
            r = c.text.strip()
            aa.append(r)
        ae = aa
    


    context = {
        'word' : word,
        'meaning' : meaning1,
        'se' : se,
        'ae' : ae,
        'mt' : []
    }

    return render(request, 'dictionary/search.html', context)