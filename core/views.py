from django.shortcuts import render
from .models import Featured,MyService,Post,Faq_image

# Create your views here.
def Home(request):
    featured = Featured.objects.all()[:8]
    services1 = MyService.objects.all()[:4]
    services2 =MyService.objects.all()[4:9]
    post = Post.objects.filter(status ='PUBLISH').order_by('-id')[:3]
    # faqs = Faq.objects.all()[:4]
    faq_image = Faq_image.objects.all()[:2]
    
    context ={
        'featured': featured,
        'services1':services1,
        'services2':services2,
        # 'faqs': faqs
    }
    return render(request, 'core/index.html', context)


def About(request):
    return render(request, 'core/about.html')


def Service(request):
    return render(request, 'core/services.html')


def Case_study(request):
    return render(request, 'core/cases.html')



def Contact(request):
    return render(request, 'core/contact.html')


def Blog(request):
    return render(request, 'core/blog.html')