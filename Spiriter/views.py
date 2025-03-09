from django.shortcuts import render
from UserInterface.models import Token, EndUser
from UserInterface.views import is_logged_in

@is_logged_in
def Spiriter(request):
    user = Token.objects.get(token=request.session.get('token')).user
    context = {
        'endUser': user,
        'user': user.type
    }
    return render(request, 'spiriter.html', context)

