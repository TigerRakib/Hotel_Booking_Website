from django.contrib import admin
from app1.models import company,why_us,stats,food_type,starters,breakfast,lunch,dinner,testimonial,event,professionals,galleries,contact_form,booking_info
@admin.register(company)
class companyAdmin(admin.ModelAdmin):
    pass
@admin.register(why_us)
class why_usAdmin(admin.ModelAdmin):
    list_display=[
        'title'
    ]
@admin.register(stats)
class statsAdmin(admin.ModelAdmin):
    list_display=[
        'category'
    ]
@admin.register(food_type)
class food_typeAdmin(admin.ModelAdmin):
    list_display=[
        'type'
    ]
@admin.register(starters)
class starterAdmin(admin.ModelAdmin):
    list_display=[
        'food_name'
    ]
@admin.register(breakfast)
class breakfastAdmin(admin.ModelAdmin):
    list_display=[
        'food_name'
    ]
@admin.register(lunch)
class lunchAdmin(admin.ModelAdmin):
    list_display=[
        'food_name'
    ]
@admin.register(dinner)
class dinnerAdmin(admin.ModelAdmin):
    list_display=[
        'food_name'
    ]
@admin.register(testimonial)
class testimonialAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'designation',
        'rating'
    ]
@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    list_display=[
        'event'
    ]
@admin.register(professionals)
class professionalsAdmin(admin.ModelAdmin):
    list_display=[
        'designation'
    ]
@admin.register(galleries)
class galleriesAdmin(admin.ModelAdmin):
    list_display=[
        'id'
    ]
@admin.register(contact_form)
class contact_formAdmin(admin.ModelAdmin):
    list_display=[
        'email',
        'is_success',
        'is_error',
        'action_time'
    ]
@admin.register(booking_info)
class booking_infoAdmin(admin.ModelAdmin):
    list_display=[
        'email',
        'is_success',
        'is_error',
        'action_time'
    ]

