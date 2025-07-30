
from django.shortcuts import render
from .models import Event, Category,Backgroundimg
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='register')
def gic2(request):
    background = Backgroundimg.objects.all()
    return render(request,'gic2.html',{'background':background})

@login_required(login_url='register')
def gallery_view(request):
    year = request.GET.get('year')
    category_id = request.GET.get('category')
    search_query = request.GET.get('search')

    events = Event.objects.annotate(photo_count=Count('photos'))

    if year:
        events = events.filter(year=year)
    if category_id and category_id != "all":
        events = events.filter(category_id=category_id)
    if search_query:
        events = events.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    categories = Category.objects.all()
    years = Event.objects.values_list('year', flat=True).distinct().order_by('-year')

    context = {
        'events': events,
        'categories': categories,
        'years': years,
    }
    return render(request, 'gallery.html', context)

@login_required(login_url='register')
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    photos = event.photos.all()
    return render(request, 'image_detail.html', {'event': event, 'photos': photos})

@login_required(login_url='register')
def contact(request):
    return render(request, 'contact.html')