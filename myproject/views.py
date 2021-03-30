from django.http import HttpResponse


def myView(request,id):





    return HttpResponse("<h1>Hello"+str(id)+"</h1>")