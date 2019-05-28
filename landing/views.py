from django.shortcuts import render
from django.views.decorators.http import require_POST
from scraper.olx import scrape
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


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



@require_POST
def send_email(request):
    query = request.POST.get('query')
    email = request.POST.get('email')
    result = scrape(query)
    context = {
        'query': query,
        'result': result
    }
    html_message = render_to_string('email.html', context)
    plain_messages = strip_tags(html_message)

    mail.send_mail(f'result for {query} from ihfazh site', plain_messages, 'From <mihfazhillah@gmail.com>', [email], html_message=html_message)
    return render(request, 'email_sent.html')
