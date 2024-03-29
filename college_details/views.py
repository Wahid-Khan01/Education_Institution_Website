from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . models import IndianStates, UserProfile2, IndiaCities, Course, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
from .forms import ContactForm


def index(request):
    return render(request, 'college_details/index.html')


def select_course(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'select_course.html', {'courses': UserProfile2.COURSE_CHOICES})
    
@login_required
def add_user(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        state = request.POST.get('state')
        course = request.POST.get('course')
        
        user_profile = UserProfile2(name=name, email=email, phone=phone, date_of_birth=dob, city=city, state=state, course=course)
        user_profile.save()
        messages.success(request, 'User profile created successfully.')
        return redirect('/college_details/add_user/')
    else:
        indian_states = IndianStates.objects.all()
        india_cities = IndiaCities.objects.all()
        context = {'COURSE_CHOICES': UserProfile2.COURSE_CHOICES, 'indian_states':indian_states, 'india_cities':india_cities}
        return render(request, 'add_user.html', context)
    

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    if request.method == 'GET':
        course = request.GET.get('course')
        if course:
            users = UserProfile2.objects.filter(course=course)
        else:
            users = None
    else:
        users = None
    return render(request, 'dashboard.html', {'COURSE_CHOICES': UserProfile2.COURSE_CHOICES, 'users': users})


@login_required
def edit_user(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('home')  
    
    users = None
    indian_states = IndianStates.objects.all()
    india_cities = IndiaCities.objects.all()
    context = {'COURSE_CHOICES': UserProfile2.COURSE_CHOICES}
    success = False
    
    if request.method == 'GET':
        course = request.GET.get('course')
        if course:
            users = UserProfile2.objects.filter(course=course)
    elif request.method == 'POST':
        user_id = request.POST.get('user')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth_str = request.POST.get('date_of_birth')

        city_name = request.POST.get('city') 
        state_name = request.POST.get('state') 
        course = request.POST.get('course')

        if not user_id:
            messages.warning(request, 'No user selected.')
            return redirect('edit_user')

        user = get_object_or_404(UserProfile2, pk=user_id)

        date_of_birth = None

        if date_of_birth_str:
            try:
                date_of_birth = datetime.strptime(date_of_birth_str, "%d/%m/%Y").strftime("%Y-%m-%d")
            except ValueError:
                messages.error(request, 'Invalid date format. Date of birth must be in DD/MM/YYYY format.')
                return redirect('edit_user')

        if not any([name, email, phone, date_of_birth, city_name, state_name, course]):
            messages.warning(request, 'No changes were made as all fields were empty.')
            return redirect('edit_user') 

        if name:
            user.name = name
        if email:
            user.email = email
        if phone:
            user.phone = phone
        if date_of_birth:
            user.date_of_birth = date_of_birth
        if city_name:
            user.city = city_name 
        if state_name:
            user.state = state_name
        if course:
            user.course = course

        user.save()
        success = True
        messages.success(request, 'User profile updated successfully.')
        return redirect('edit_user') 

    return render(request, 'edit_user.html', {'users': users, 'indian_states': indian_states, 'india_cities': india_cities, 'context': context, 'success': success})

@login_required
def delete_user(request):

    if request.method == 'GET':
        course = request.GET.get('course')
        if course:
            users = UserProfile2.objects.filter(course=course)
        else:
            users = None
    else:
        users = None
    return render(request, 'delete_user.html', {'users': users, 'COURSE_CHOICES': UserProfile2.COURSE_CHOICES})

def delete_user_action(request, user_id):
    if request.method == 'DELETE':
        user = get_object_or_404(UserProfile2, pk=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def user_profile(request):
    user_name = request.user.username
    user_email = request.user.email

    try:
        user_profile = UserProfile2.objects.get(name=user_name, email=user_email)
    except UserProfile2.DoesNotExist:
        return HttpResponse('Not exist')

    return render(request, 'user_profile.html', {'user_profile': user_profile})

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/')
            elif user.is_staff:
                return redirect('/')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login1') 
    return render(request, 'signup.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # Redirect to a thank you page or show a success message
            return redirect('contact_us')
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})


def buy_course(request):
    # Assuming you have a model named Course with fields 'name', 'fees', and 'tenure'
    courses = Course.objects.all()  # Query all courses from the database
    return render(request, 'buy_course.html', {'courses': courses})
