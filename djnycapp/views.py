from django.http import Http404, HttpResponse
from django.contrib.auth.models import User

def UserAutoComplete(request):
    try:
        q = request.GET['q']
    except:
        raise Http404
    return HttpResponse('\n'.join(["%s|%s" % (str(x), x.id) for x in User.objects.filter(username__icontains=q)]))
