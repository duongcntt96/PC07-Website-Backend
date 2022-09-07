from django.shortcuts import render
from django.http import HttpResponse
from docs.models import Doc
from .models import Post, Bai_viet
import threading

# Create your views here.
def index(request):
	data = Post.objects.all()
	for post in data:
		post.body=post.body[0:300]+'...'
	data = Bai_viet.objects.all()
	return render(request, 'home/home.html', { 'data' : data })

def post(request,id):
	data = Post.objects.get(id=id)
	try:
		threading.Thread(target=create,args=(id,)).start()
	except:
		print("Lỗi")
	return render(request, 'home/post.html', { 'data' : data })
def create(id):
	# Import the required module for text 
	# to speech conversion
	from gtts import gTTS
	import os
	data = Post.objects.get(id=id)
	mytext = data.body
	id = data.id
	language = 'vi'
	myobj = gTTS(text=mytext, lang=language, slow=False)
	myobj.save("static/audio/"+str(id)+".mp3")
	# os.system("start welcome.mp3")

def contact(request):
	return render(request, 'home/contact.html')

def about(request):
	return render(request, 'home/about.html')

def law(request):
	data = {"data": Doc.objects.all()}
	return render(request, 'home/law.html',data)

from .forms import feedBackForm
from django.http import HttpResponseRedirect 

def feedback(request):
    form = feedBackForm()
    if request.method == 'POST':
        form = feedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(request, 'home/feedback.html', {'form': form})
    