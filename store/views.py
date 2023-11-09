from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from django.db import connection
from django.db.models import F, Sum,Subquery,OuterRef, Case, When, Value, IntegerField
from django.db.models.functions import Coalesce
from django.contrib.auth.decorators import login_required



from .forms import LocForm,CatForm,ItemForm,AllocateForm
from .models import Category,Location,Item,Allocation
from core.models import Request

# Create your views here.
@login_required(login_url='/user/login')
def store(request):
    with connection.cursor() as cursor:
        query = """
        SELECT `store_category`.`title` AS `category`,
            SUM(`store_item`.`quantity`) AS `total_quantity_items`,
            0 AS `total_quantity_requests`
        FROM `store_item`
        INNER JOIN `store_category` ON (`store_item`.`category_id` = `store_category`.`id`)
        GROUP BY `store_category`.`title`
        UNION ALL
        SELECT `store_category`.`title` AS `category`,
            0 AS `total_quantity_items`,
            SUM(CASE WHEN `core_request`.`status` = 'approved' THEN `core_request`.`quantity` ELSE 0 END) AS `total_quantity_requests`
        FROM `core_request`
        INNER JOIN `store_category` ON (`core_request`.`category_id` = `store_category`.`id`)
        GROUP BY `store_category`.`title`
        """
        result = None  # Initialize result variable
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            # Log or print the error
            print(f"Error executing query: {e}")

        category_totals = {}
        for row in result:
            category = row[0]
            total_items = row[1]
            total_requests = row[2]
            if category in category_totals:
                category_totals[category][0] += total_items
                category_totals[category][1] += total_requests
            else:
                category_totals[category] = [total_items, total_requests]

        modified_result = []
        for category, totals in category_totals.items():
            total_items, total_requests = totals
            remainder = total_items - total_requests
            modified_result.append((category, total_items, total_requests, remainder))

        context = {'result': modified_result,
                   'title':'Store'}
        return render(request, 'store/store.html', context)

@login_required
def location(request):
        forms = Location.objects.filter(status='active')
        if request.method == 'POST':
            form = LocForm(request.POST)
        
            if form.is_valid():
                form.save()           
                messages.success(request,'The location was added')
                return redirect('location')
            else:
                return redirect('location')
        else:
            form = LocForm()
        return render(request, 'store/location.html', {'title':'Location','location':forms, 'form':form})

@login_required
def edit_loc(request, slug):
    loc = Location.objects.filter(status='active').get(slug=slug)
    
    if request.method == 'POST':
        form = LocForm(request.POST,instance=loc)

        if form.is_valid():
            form.save()
            messages.success(request,'The changes was saved!')
            return redirect('location')
    else:
        form = LocForm(instance=loc)

    return render(request, 'store/edit_form.html', {'title':'Edit_Location', 'form':form})

@login_required
def delete_loc(request, slug):
    product = Location.objects.filter(status='active').get(slug=slug)
    product.status = 'inactive'
    product.save()

    messages.error(request,'The location was deleted Successfully!')

    return redirect ('location')

@login_required
def category(request):
        forms = Category.objects.filter(status='active')
        if request.method == 'POST':
            form = CatForm(request.POST)
        
            if form.is_valid():
                form.save()           
                messages.success(request,'The Category was added')
                return redirect('category')
            else:
                return redirect('category')
        else:
            form = CatForm()
        return render(request, 'store/category.html', {'title':'Category','category':forms, 'form':form})

@login_required
def edit_cat(request, slug):
    Cat = Category.objects.filter(status='active').get(slug=slug)
    
    if request.method == 'POST':
        form = CatForm(request.POST,instance=Cat)

        if form.is_valid():
            form.save()
            messages.success(request,'The changes was saved!')
            return redirect('category')
    else:
        form = CatForm(instance=Cat)

    return render(request, 'store/edit_form.html', {'title':'Edit_Category', 'form':form})

@login_required
def delete_Cat(request, slug):
    product = Category.objects.filter(status='active').get(slug=slug)
    product.status = 'inactive'
    product.save()

    messages.error(request,'The Category deleted Successfully!')

    return redirect ('category')

@login_required
def item(request):
        forms = Item.objects.filter(status='active')
        if request.method == 'POST':
            form = ItemForm(request.POST)
        
            if form.is_valid():
                title = request.POST.get('title')
                product = form.save(commit=False)
                product.slug = slugify(title)
                product.save()          
                messages.success(request,'The Item was added succesfully')
                return redirect('item')
            else:
                return redirect('item')
        else:
            form = ItemForm()
        return render(request, 'store/item.html', {'title':'Item','item':forms, 'form':form})

@login_required
def edit_Item(request, slug):
    Cat = Item.objects.filter(status='active').get(slug=slug)
    
    if request.method == 'POST':
        form = ItemForm(request.POST,instance=Cat)

        if form.is_valid():
            form.save()
            messages.success(request,'The changes was saved!')
            return redirect('category')
    else:
        form = ItemForm(instance=Cat)

    return render(request, 'store/edit_form.html', {'title':'Edit_Item', 'form':form})

@login_required
def delete_item(request, slug):
    # fetch the object related to passed id
    obj = get_object_or_404(Item, slug=slug)
    obj.delete()
    messages.error(request,'the item was deleted successfully!')
    return redirect("item")

@login_required
def allocate(request):
        forms = Allocation.objects.filter(status='active')
        if request.method == 'POST':
            form = AllocateForm(request.POST)
        
            if form.is_valid():
                title = request.POST.get('category')
                product = form.save(commit=False)
                product.slug = slugify(title)
                product.save()          
                messages.success(request,'The Item was added succesfully')
                return redirect('allocate')
            else:
                return redirect('allocate')
        else:
            form = AllocateForm()
        return render(request, 'store/allocate.html', {'title':'Allocation','item':forms, 'form':form})

@login_required
def edit_allocate(request, slug):
    Cat = Allocation.objects.filter(status='active').get(slug=slug)
    
    if request.method == 'POST':
        form = AllocateForm(request.POST,instance=Cat)

        if form.is_valid():
            form.save()
            messages.success(request,'The changes was saved!')
            return redirect('allocate')
    else:
        form = AllocateForm(instance=Cat)

    return render(request, 'store/edit_form.html', {'title':'Edit_Allocate', 'form':form})

@login_required
def delete_allocate(request, slug):
    # fetch the object related to passed id
    obj = get_object_or_404(Allocation, slug=slug)
    obj.delete()
    messages.error(request,'the item was deleted successfully!')
    return redirect("allocate")



def store2(request):
    # Subquery to calculate total quantity for items per category
    item_subquery = Item.objects.filter(category=OuterRef('pk')).values('category').annotate(
        total_quantity_items=Coalesce(Sum('quantity'), Value(0), output_field=IntegerField())
    ).values('total_quantity_items')

    # Subquery to calculate total quantity for approved requests per category
    request_subquery = Request.objects.filter(category=OuterRef('pk'), status='approved').values('category').annotate(
        total_quantity_requests=Coalesce(Sum('quantity'), Value(0), output_field=IntegerField())
    ).values('total_quantity_requests')

    # Main query to get categories and totals
    result = Category.objects.annotate(
        total_quantity_items=Subquery(item_subquery),
        total_quantity_requests=Subquery(request_subquery),
    ).values('title', 'total_quantity_items', 'total_quantity_requests')

    # Calculate the remainder
    result = result.annotate(
        remainder=F('total_quantity_items') - F('total_quantity_requests')
    )

    # Get the final result as a list of dictionaries
    result_data = list(result)

    context = {'result': result_data
               }
    return render(request, 'store/store.html', context)



 
