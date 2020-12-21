from django.shortcuts import render


from .models import Post

def home(request):
    return render(request,'home.html')
def Add(request):
    if request.method == 'GET':
        if request.GET.get('pn', None) and request.GET.get('sn', None):
            post = Post()
            post.PersonName = request.GET.get('pn', None)
            post.SweetName= request.GET.get('sn', None)
            post.Number=request.GET.get('num',None)
            post.save()
        return render(request, 'Add.html')
    else:
        return render(request, 'Add.html')
def see(request):
    data=Post.objects.all()
    return render(request,'see.html',{'data':data})