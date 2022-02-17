from django.shortcuts import render


def login_page(request):
    context = {

    }
    return render(request, 'authentication/login_page.html', context)
