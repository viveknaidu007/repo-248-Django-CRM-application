from django.shortcuts import render

def landing(request):
    return render(request, "index.html")  # Make sure the template name is correct
