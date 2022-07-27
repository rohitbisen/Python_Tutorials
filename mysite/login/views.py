from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def login_form(request):
    return render(request, 'login_page.html')

@csrf_exempt
def submit_form(request):
    username = request.POST['username']
    password = request.POST['password']

    if(username == 'rohitbisen45' and password == '1230'):
        return HttpResponse('Welcome')
    else:
        return HttpResponse('invalid username or password')
       

