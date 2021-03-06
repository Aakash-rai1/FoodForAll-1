from django.shortcuts import render
from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     return HttpResponse('It works')
from django.contrib.auth.models import User

from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponse,redirect


class HomeView(TemplateView):
    template_name = "home.html"

    

    def get(self, request):
        form = SubcriberForm()
        carosels = Carosel.objects.all()
        partners = Partner.objects.all()
        donaters = Donater.objects.all()
        args = {'carosels': carosels,
                'partners': partners, 
                'donaters': donaters,
                'form':form
                                     }
        # args1= {'partners': partners}
        
        return render(request, self.template_name,args)
    
    # def get(self, request):
        
    #     partners = Partner.objects.all()
        
    #     args1 = {'partners': partners} 
    #     return render(request, self.template_name, args1)

    def post(self, request):
        form = SubcriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/home')

        args = {'form':form }
        return render(request,self.template_name, args)




from home.models import Post, Carosel, Partner, Donater,EventInfo
from home.forms import HomeForm, SubcriberForm, ContactForm
from django.views.generic import ListView, CreateView 

class postfood(TemplateView):
    template_name = "postfood.html"

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        users = User.objects.exclude(id=request.user.id)
        args = {'form':form , 'posts':posts,'users':users}
        return render(request,self.template_name, args )

    def post(self, request):
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.foodimg = request.foodimg
            post.user = request.user
            post.save()

            # text = form.cleaned_data['postfood']
            # form = HomeForm()
            return redirect ('/postfood')
        

        args = {'form':form , }
        return render(request,self.template_name, args)

class Contact(TemplateView):
    template_name = "contact.html"

    def get(self, request):
        form = ContactForm()
        args ={'form':form}

        return render(request, self.template_name,args)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/contact')

        args = {'form':form }
        return render(request,self.template_name, args)

class About(TemplateView):
    template_name = "about.html"



class Event(TemplateView):
    template_name = "event.html"

    def get(self, request):
        events = EventInfo.objects.all().order_by('-uploaddate')
        args = { 'events':events}
        return render(request,self.template_name, args )

class FoodInfo(TemplateView):
    template_name = "foodinfo.html"

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        users = User.objects.exclude(id=request.user.id)
        args = {'form':form , 'posts':posts,  'users':users}
        return render(request,self.template_name, args )

    







