from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils import timezone
from app1.models import company,why_us,stats,food_type,starters,breakfast,lunch,dinner,testimonial,event,professionals,galleries,contact_form,booking_info
def index(request):
    all_info=company.objects.first()
    whys=why_us.objects.all()
    members=stats.objects.all()
    all_types_food=food_type.objects.all()
    starters_menu=starters.objects.all()
    all_breakfast=breakfast.objects.all()
    lunchs=lunch.objects.all()
    dinners=dinner.objects.all()
    testimonials=testimonial.objects.all()
    events=event.objects.all()
    professional=professionals.objects.all()
    gallery=galleries.objects.all()
    context={
        'company_name':all_info.company_name,
        'content':all_info.content,
        'phone':all_info.phone,
        'location':all_info.location,
        'email':all_info.email,
        'opening_hours':all_info.opening_hours,
        'video_url':all_info.video_link,
        "whys":whys,
        'members':members,
        'all_type':all_types_food,
        'starters_menu':starters_menu,
        'breakfasts':all_breakfast,
        'lunchs':lunchs,
        'dinners':dinners,
        "testimonials":testimonials,
        'events':events,
        "profs":professional,
        'galleries':gallery
        }
    return render(request,'index.html',context)
def contact_us(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    context={
        'name': name,
        'email':email,
        'subject':subject,
        'message':message
    }
    html_template= render_to_string('email.html',context)
    is_success=False
    is_error=False
    try:
        send_mail(
            subject=subject,
            message="",
            html_message=html_template,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False
        )
    except Exception as e:
        is_error=True
    else:
        is_success=True
    contact_form.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message,
        is_success=is_success,
        is_error=is_error,
        action_time=timezone.now()
    )
    return redirect('home')
def booking_room(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    date=request.POST.get('date')
    time=request.POST.get('time')
    people=request.POST.get('people')
    message=request.POST.get('message')
    context={
        'name':name,
        'email':email,
        'phone':phone,
        'date':date,
        'time':time,
        'people':people,
        'message':message
    }
    html_template= render_to_string('booking.html',context)
    booking='For booking'
    is_success=False
    is_error=False
    try:
        send_mail(
            subject=booking,
            message="",
            html_message=html_template,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False
        )
    except Exception as e:
        is_error=True
    else:
        is_success=True
    booking_info.objects.create(
        name=name,
        email=email,
        phone=phone,
        date=date,
        time=time,
        people=people,
        message=message,
        is_success=is_success,
        is_error=is_error,
        action_time=timezone.now()
    )
    return redirect('home')
