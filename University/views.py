from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import University 


#home page
@login_required
def home_view(request):
    return render(request, 'University/home.html')

@login_required
def university_home(request):
    universities = University.objects.all()
    return render(request, "University/university_home.html", {"universities": universities})

#view page
@login_required
def display_view(request):
    data = University.objects.all()
    return render(request,'University/display.html',{"universities": data})

#add university
@login_required
def add_view(request):
    if request.method == "POST":
        name = request.POST.get("u_name")
        code = request.POST.get("u_code")
        city = request.POST.get("u_city")
        state = request.POST.get("u_state")
        email = request.POST.get("u_email")
        contact = request.POST.get("u_contact")
        
        if University.objects.filter(u_email=email).exists():
            return render(request, "University/add.html", {
                "error": "This email already exists."
            })
        obj = University(
            u_name=name,
            u_code=code,
            u_city=city,
            u_state=state,
            u_email=email,
            u_contact=contact
        )
        obj.save()

        return redirect('universities:display_university')   # ✔ fixed

    return render(request, "University/add.html")

#update data
from django.shortcuts import render, redirect, get_object_or_404
from .models import University

@login_required
def update_view(request, pk):
    obj = get_object_or_404(University, id=pk)

    if request.method == "POST":
        obj.u_name = request.POST.get("u_name")
        obj.u_code = request.POST.get("u_code")
        obj.u_city = request.POST.get("u_city")
        obj.u_state = request.POST.get("u_state")
        obj.u_email = request.POST.get("u_email")
        obj.u_contact = request.POST.get("u_contact")
        obj.save()

        return redirect('universities:display_university')

    context = {'data': obj}
    return render(request, 'University/update.html', context)

#delete one 
@login_required
def delete_view(request, pk):
    obj = get_object_or_404(University, id=pk)
    obj.delete()
    return redirect('universities:display_university')

