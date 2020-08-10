from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
from .models import Products, Nav, Blended_workshops, Jobfair, Internship, Testimonials, MediaTestimonials, Award
from datetime import datetime
from django.utils import timezone
from .forms import ContactForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobFairSerializer
from django.contrib import messages
import urllib, json
from django.views.generic import TemplateView
from .utils import *

today = datetime.today().strftime('%Y-%m-%d')

def home(request):
    if request.method == 'POST':
        c = ContactForm(request.POST)
        if c.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values ={
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
                }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                c.save()
                messages.add_message(request,messages.INFO,'Message submitted!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('/spoken#contact')
            #c = ContactForm()
    else:
        c = ContactForm()

    # return HttpResponse("Hello, world. You're at the spoken landing page.")
    navs = Nav.objects.filter(status=1)
    products = Products.objects.all().order_by('order')
    now = timezone.now()
    jobfairs = Jobfair.objects.all().order_by('-jobfair_start_date')[:3]
    internships = Internship.objects.all().order_by('-internship_start_date')[:3]
    workshops = Blended_workshops.objects.all().order_by('-workshop_start_date')[:3]
    testimonials = Testimonials.objects.all()[:9]
    media_testimonials = MediaTestimonials.objects.all()[:3]
    awards = Award.objects.all().order_by('order');
    context = {'jobfairs':jobfairs,'internships':internships,'workshops':workshops,'products':products, 
    'nav_list':navs, 'form':c, 'testimonials':testimonials,'media_testimonials':media_testimonials,'media_url' : settings.MEDIA_URL,
    'awards':awards,}

    context['SITE_KEY'] = settings.GOOGLE_RECAPTCHA_SITE_KEY

    return render(request,'spoken/home.html',context)

#api/jobfairs/
class JobFairList(APIView):
    def get(self,request):
        jobfairs = Jobfair.objects.all()
        serializer = JobFairSerializer(jobfairs,many=True)
        return Response(serializer.data)


    def post(self):
        pass

def jobfairs(request):
    d = datetime.now()
    current_year = d.year
    context = {'current_year':current_year}
    return render(request,'spoken/jobfairs.html',context)

def jobfair_detail(request,jobfair_id):
    jobfair_obj = Jobfair.objects.filter(jobfair_id=jobfair_id)[0]
    context = {'jobfair_id':jobfair_id,'jobfair':jobfair_obj}
    return render(request,'spoken/jobfair_detail.html',context)



class TutorialSearch(TemplateView):
    template_name = 'spoken/tutorial_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_foss = self.request.GET.get('search_foss', None)
        search_language = self.request.GET.get('search_language', None)
        if search_foss and search_language:
            tutorials = get_tutorials(search_foss, search_language)
            if tutorials:
                context["foss"] = search_foss
                context["language"] = search_language
                context["tutorials"] = tutorials
        context["foss_lang_list"] = get_all_foss_lang()
        return context

class TutorialWatch(TemplateView):
    template_name = 'spoken/tutorial_watch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foss = self.request.GET.get('foss', None)
        language = self.request.GET.get('language', None)
        tutorial = self.request.GET.get('tutorial', None)
        context["tutorial"] = get_tutorial_detail(foss, language, tutorial)
        return context
    
    
