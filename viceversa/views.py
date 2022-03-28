from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):

    params = {'original_text': request.GET['usertext'],
              'count_words': len(request.GET['usertext'].split()),
              'reverse_text': request.GET['usertext'][::-1]
              }

    return render(request, 'reverse.html', params)
