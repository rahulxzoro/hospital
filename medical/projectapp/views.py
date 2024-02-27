from django.shortcuts import render,get_object_or_404,redirect
from . models import Types,Category
# Create your views here.
def home(request):
    obj=Types.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        date=request.POST.get('date')
        data=Types(name=name,mobile=mobile,date=date)
        data.save()
    return render(request,'index.html',{'obj':obj})

def by_category(request, c_slug):
    category = get_object_or_404(Category, slug=c_slug)
    # Logic to retrieve and display content related to the category
    return render(request, 'service.html', {'category': category})

def service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        if name and mobile and date:  
            Types.objects.create(name=name, mobile=mobile, date=date)
            return redirect('services:home')  # Redirect to the home page after successful submission
        else:
            # Handle invalid form data, for example, by rendering a form with errors
            return render(request, 'service.html', {'error': 'Invalid form data'}) 
    else:
        # Handle GET requests by rendering the form
        return render(request, 'service.html')