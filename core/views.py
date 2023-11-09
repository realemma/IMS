from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.decorators import login_required



from store.models import Category,Location,Item,Allocation
from .models import Request
from .forms import RequestForm,ApproveForm


# Create your views here.
@login_required
def dashboard(request):
    forms = Request.objects.filter(status= 'uncompleted')


    if request.method == 'POST':
        form = RequestForm(request.POST)
        category_id = request.POST.get('category')
        location_id = request.POST.get('location')
        
        category = Category.objects.get(id=category_id)
        location = Location.objects.get(id=location_id)

                # Calculate the total quantity allocated for the same category and location
        total_allocated = Allocation.objects.filter(category=category, location=location).aggregate(models.Sum('quantity'))['quantity__sum'] 
        #requested = Request.objects.filter(category=category, location=location).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        new_transaction_id = generate_transaction_id()
        quantity_posted = int(request.POST.get('quantity'))


        if total_allocated is not None:  
            # Calculate the total quantity requested for the same category and location
            requested = Request.objects.filter(category=category, location=location).exclude(status='rejected').aggregate(models.Sum('quantity'))['quantity__sum'] or 0

            total_request = requested + quantity_posted
            print(total_allocated)
            print(total_request)
            print(requested)



            if total_allocated  >= total_request:
                    # Process the form data
                if form.is_valid():
                    product = form.save(commit=False)
                    product.transaction_id = new_transaction_id
                    product.slug = slugify(new_transaction_id)
                    product.save() 
                    # Set other fields as needed

                    # Save the Request object

                    messages.success(request, 'Request Created Successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Request exceeds Allocation')
            return redirect('dashboard')          
        else:
            messages.error(request, 'Allocation should be done before Request')
    else:
        form = RequestForm()

    return render(request, 'core/index.html', {'title': 'New Request', 'form': form , 'item':forms})

def generate_transaction_id():
    last_request = Request.objects.order_by('-transaction_id').first()

    if last_request:
        last_id = int(last_request.transaction_id[3:])
        next_id = last_id + 1
    else:
        next_id = 1

    return f'REQ{next_id:03}'

@login_required
def Uncom(request, slug):
    forms = Request.objects.filter(status='uncompleted').get(slug=slug)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=forms)
        category_id = request.POST.get('category')
        location_id = request.POST.get('location')
        
        category = Category.objects.get(id=category_id)
        location = Location.objects.get(id=location_id)

                # Calculate the total quantity allocated for the same category and location
        total_allocated = Allocation.objects.filter(category=category, location=location).aggregate(models.Sum('quantity'))['quantity__sum'] 
        #requested = Request.objects.filter(category=category, location=location).aggregate(models.Sum('quantity'))['quantity__sum'] or 0
        new_transaction_id = generate_transaction_id()
        quantity_posted = int(request.POST.get('quantity'))


        if total_allocated is not None:  
            # Calculate the total quantity requested for the same category and location
            requested = Request.objects.filter(category=category, location=location , status= 'pending' or 'approved').exclude(status='rejected' or 'uncompleted').aggregate(models.Sum('quantity'))['quantity__sum'] or 0

            total_request = requested + quantity_posted
            print(total_allocated)
            print(total_request)
            print(requested)



            if total_allocated  >= total_request:
                    # Process the form data
                if form.is_valid():
                    product = form.save(commit=False)
                    product.status = product.PENDING
                    product.save() 
                    # Set other fields as needed
                    # Save the Request object
                    messages.success(request, 'Request Submitted Successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Request exceeds Allocation')
            return redirect('dashboard')          
        else:
            messages.error(request, 'Allocation should be done before Request')
    else:
        form = RequestForm(instance=forms)

    return render(request, 'core/edit_item.html', {'title': 'Edit_Request', 'form': form , 'item':forms})

@login_required
def pend(request):
    forms = Request.objects.filter(status='pending')
    return render(request, 'core/index.html', {'title': 'Pending Request', 'pend':'index.html' , 'item':forms})

@login_required
def pend_app(request, slug):
    forms = Request.objects.filter(status='pending').get(slug=slug)

    if request.method == 'POST':
        form = ApproveForm(request.POST, instance=forms)
                    # Process the form data
        if form.is_valid():
            product = form.save(commit=False)
            product.status = product.APPROVED
            product.save() 
                    # Set other fields as needed
            messages.success(request, 'Request Approved Successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error in entry')
    else:
        form = ApproveForm(instance=forms)

    return render(request, 'core/edit_item.html', {'title': 'Edit_Request', 'form': form , 'item':forms})

@login_required
def pend_reject(request, slug):
    forms = Request.objects.filter(status='pending').get(slug=slug)

    if request.method == 'POST':
        form = ApproveForm(request.POST, instance=forms)
                    # Process the form data
        if form.is_valid():
            product = form.save(commit=False)
            product.status = product.REJECTED
            product.save() 
                    # Set other fields as needed
            messages.info(request, 'Request Rejected Successfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error in entry')
    else:
        form = ApproveForm(instance=forms)

    return render(request, 'core/edit_item.html', {'title': 'Edit_Request', 'form': form , 'item':forms})


@login_required
def approve(request):
    forms = Request.objects.filter(status='approved')

    return render(request, 'core/index.html', {'title': 'Approved Request','status':'approve', 'pend':'index.html' , 'item':forms})

@login_required
def approve_edit(request,slug):
    forms = Request.objects.filter(status='approved').get(slug=slug)

    return render(request, 'core/view.html', {'title': 'Approved Request','status':'approve', 'pend':'index.html' , 'Req':forms})


@login_required
def reject(request):
    forms = Request.objects.filter(status='rejected')

    return render(request, 'core/index.html', {'title': 'Rejected Request','status':'approve', 'pend':'index.html' , 'item':forms})

@login_required
def reject_edit(request,slug):
    forms = Request.objects.filter(status='rejected').get(slug=slug)

    return render(request, 'core/view.html', {'title': 'Rejected Request','status':'approve', 'pend':'index.html' , 'Req':forms})

