from django.contrib import admin

# Register your models here.

from .models import Featured,MyService,Post,Faq_image

admin.site.register(Featured)
admin.site.register(MyService)
admin.site.register(Post)
# admin.site.register(Faq)
admin.site.register(Faq_image)