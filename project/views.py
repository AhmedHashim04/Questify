
from django.shortcuts import render , redirect ,get_object_or_404
def handel404(request,exception):
    return render(request,"404.html",status=404)

def handel500(request,):
    
    return render(request,"500.html",status=500)