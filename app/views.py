from collections import Counter
from django.shortcuts import render_to_response

# в реальных проектах так не стоит делать
# так как при перезапуске приложения cчетчики обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    if 'test' in request.GET.get('from-landing'):
        counter_click['test'] += 1
        counter_show['index'] += 1
        return render_to_response('index.html')
    else:
        counter_click['original'] += 1
        counter_show['index'] += 1
        return render_to_response('index.html')


def landing(request):
    if 'original' in request.GET.get('ab-test-arg'):
        landing_page = render_to_response('landing.html')
        return landing_page
    elif 'test' in request.GET.get('ab-test-arg'):
        landing_page_test = render_to_response('landing_alternate.html')
        return landing_page_test


def stats(request):
    test_conversion = counter_show['index']/counter_click['test']
    original_conversion = counter_show['index']/counter_click['original']
    context = {
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    }
    return render_to_response('stats.html', context)
