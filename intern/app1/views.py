from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
def index(request):
    return render(request,"app1/index.html")

def result(request):
    #print("Request object: {}".format(request.POST))
    if request.method == 'POST' and request.FILES['profile_pic'] and request.FILES['video']:
        myfile = request.FILES['profile_pic']
        videofile = request.FILES['video']
        fs = FileSystemStorage()
        video_filename = fs.save("videos/"+videofile.name, videofile)
        image_filename = fs.save("images/"+myfile.name, myfile)
        uploaded_video_url = fs.url(video_filename)
        uploaded_image_url = fs.url(image_filename)
    name= request.POST["fullname"]
    email= request.POST["email"]
    phone= request.POST["phone"]
    branch= request.POST["branch"]
    profile_pic= uploaded_image_url
    video = uploaded_video_url
    student = Student.objects.create( email=email, name=name,phone=phone,branch=branch,profile_pic=profile_pic,video = video)
    query_result = Student.objects.latest('Student_id')
    context = {
            'query_result': query_result
        }

    return render(request,'app1/dup.html', context=context)

# def Display_view(ListView):
#     model = Student
#     template_name = 'image.html'

def display(request):
    query_result = Student.objects.all()
    context = {
            'query_result': query_result
        }
    return render(request, 'app1/display.html', context=context)
