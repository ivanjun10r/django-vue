from django.shortcuts import render

# A simple view to render index page
def vue_test(request):
    return render(request, 'base/index.html')
