from django.shortcuts import render
from django.views.decorators.http import require_POST
from scraper.olx import scrape


# Create your views here.


def index(request):
    return render(request, 'index.html')


@require_POST
def search(request):
    q = request.POST.get('query', 'nothing')
    result = scrape(q)
    context = {
        'query': q,
        'result': result
    }
    return render(request, 'search_result.html', context)
