from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.utils.text import slugify


from .models import note,Userprofile
from .forms import NoteForm,UpdateForm,UpdStatus


# Create your views here.
def register(request):
        user = User.objects.all()
        if request.method == 'POST':
           form = UpdateForm(request.POST)
           username = request.POST['username']
           email = request.POST['email']
           password = request.POST['password1']
           password2 = request.POST['password2']
           if password == password2:
                if User.objects.filter(email=email).exists():
                      messages.info(request,'Email Already Used')
                      return redirect('register')
                elif User.objects.filter(username=username).exists():
                        messages.info(request, 'Username Already Used')
                        return redirect('register')
                else:
                        if form.is_valid():
                            user = form.save()
                            userprofile = Userprofile.objects.create(user=user)
                            userprofile.save()
                            messages.success(request,f'{username} created successfully')
                            return redirect('register')
                        else:
                            messages.error(request, 'password not the same')
                            return redirect('register')
           else:
                messages.info(request, 'password not the same')
                return redirect('register')
        else:
            form = UpdateForm(request.POST)

            return render(request, 'user/signup.html', {'form':form,'users':user})

def Update(request):
    
    user = Userprofile.objects.all()  # Assuming 'user' is the ForeignKey or OneToOneField linking to the User model
    if request.method == 'POST':
        form = UpdStatus(request.POST)
        if form.is_valid():
            selected_user_profile = form.cleaned_data['user']            
            selected_user_profile.is_admin = True
            selected_user_profile.save()
            return redirect('success_view')  # Redirect to a success view
    else:
        form = UpdStatus()

    return render(request, 'user/status.html', {'form': form, 'user':user})
        

def login(request):
      if request.method =='POST':
            username = request.POST['username']
            password =request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                  auth.login(request,user)
                  messages.success(request, f'You are logged in as {username}')
                  return redirect('dashboard')
            else:
                  messages.warning(request, 'Credentials Invalid')
                  return redirect('login')
      else:
            return render (request, 'user/login.html')


            
def logout(request):
      auth.logout(request)
      messages.error(request,'Your session hsas ended!')
      return redirect('login')

@login_required
def delete(request,pk):
    obj = get_object_or_404(User, pk=pk)
    obj.delete()
    messages.error(request,'the item was deleted successfully!')
    return redirect("register")

@login_required
def record(request):
        forms = note.objects.all()
        if request.method == 'POST':
            form = NoteForm(request.POST)
        
            if form.is_valid():
                title = request.POST.get('title')
                product = form.save(commit=False)
                product.slug = slugify(title)
                product.save()          
                messages.success(request,'The Note was created succesfully')
                return redirect('record')
            else:
                return redirect('record')
        else:
            form = NoteForm()
        return render(request, 'user/note.html', {'title':'Credentials','item':forms, 'form':form})

@login_required
def edit_note(request, slug):
    Cat = note.objects.filter(status='active').get(slug=slug)    
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=Cat)

        if form.is_valid():
            form.save()
            messages.success(request,'The changes was saved!')
            return redirect('record')
    else:
        form = NoteForm(instance=Cat)

    return render(request, 'store/edit_form.html', {'title':'Edit_Item', 'form':form})

@login_required
def delete_note(request, slug):
    obj = get_object_or_404(note, slug=slug)
    obj.delete()
    messages.error(request,'the record was deleted successfully!')
    return redirect("record")
