from django.shortcuts import render


def greeting(request):
    name = request.GET.getlist('name')[0]
    message = request.GET.getlist('message')[0]
    template = 'index.html'
    context = {
        'name': name,
        'message': message
    }
    return render(request, template, context)
