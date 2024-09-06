from django.shortcuts import render
from . import models
from .models import book,Users
from django.http import HttpResponseRedirect, HttpResponse
from .forms import bookForm
def index(request):
    
    books=book.objects.all()
    return render(request, 'viewbook.html', {'books': books})

def addbook(request): 
    if request.method == 'POST':
        tit = request.POST['title']
        pri = request.POST['price']
        desc=request.POST['description']
        book=models.book(title=tit, price=pri,description=desc)
        book.save()
        return HttpResponseRedirect('/')
    return render(request, 'addbook.html')

def editbook(request):
    if request.method=='POST':

        tit=request.POST['title']
        pri=request.POST['price']
        desc=request.POST['description']
        bobj=models.book.objects.get(id=request.POST['bookid'])
        bobj.title=tit
        bobj.price=pri
        bobj.description=desc
        # print(tit,' ',pri)
        bobj.save()
        # books=book.objects.all()
        return HttpResponseRedirect('/')
    
    if request.method=='GET':
       bobj=models.book.objects.get(id=request.GET['bookid'])
       return render(request,'editbook.html',{'books':bobj})
    
def deletebook(request):
    obj=models.book.objects.get(id=request.GET['bookid'])
    obj.delete()
    return HttpResponseRedirect('/')

def details(request):
    obj=models.book.objects.get(id=request.GET['bookid'])
    return render(request,'details.html',{
        'book':obj,
    })

def users(request):
    users=Users.objects.all()
    return render(request, 'users.html', {'users': users})

def register_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        user=models.Users(name=name, book_reading=None)
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'register-user.html')

def issue(request):
    if request.method == 'POST':
        name = request.POST['name']
        book_id = request.POST['book']

        # print(name)
        # print(book_id)
        user = models.Users.objects.get(id=name)
        book = models.book.objects.get(id=book_id)
        user.book_reading = book
        user.is_reading = True
        user.save()
        book.is_available = False
        book.save()
        return HttpResponseRedirect('/users/')
    else:
        context = {'form': bookForm()}
        return render(request, 'issue.html', context)


def returnbook(request):
    user = models.Users.objects.get(id=request.GET['userid'])
    if user.book_reading:
        # Mark the book as available
        book = user.book_reading
        book.is_available = True
        book.save()
        
        # Remove the book from the user's record
        user.book_reading = None
        user.save()
    
    return HttpResponseRedirect('/')
