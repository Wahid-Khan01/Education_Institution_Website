from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from . models import IndianStates, UserProfile2, IndiaCities, Course, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
from .forms import  UserProfileForm
from django.core.paginator import Paginator
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


import csv


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
    users = UserProfile2.objects.all().order_by('name')

    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {'page_obj': page_obj})

def download_pdf(request):
    # Fetch data from the database
    users = UserProfile2.objects.all()

    # Generate PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="example.pdf"'
    doc = SimpleDocTemplate(response, pagesize=letter)
    
    # Define table data and style
    data = [["Name", "Email", "Phone", "Date of Birth", "City", "State", "Course"]]
    for user in users:
        data.append([user.name, user.email, user.phone, user.date_of_birth, user.city, user.state, user.course])

    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    # Add table to the PDF document
    doc.build([table])
    return response


def download_csv(request):
    users = UserProfile2.objects.all().order_by('name')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_profiles.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Date of Birth', 'City', 'State', 'Course'])
    for user in users:
        # Convert date_of_birth to string in format 'Month Day, Year'
        date_of_birth_str = user.date_of_birth.strftime('%B %d, %Y')
        writer.writerow([
            user.name,
            user.email,
            user.phone,
            date_of_birth_str,
            user.city,
            user.state,
            user.course
        ])

    return response




@login_required
def edit_user_list(request):
    users = UserProfile2.objects.all().order_by('name')
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'edit_user_list.html', {'page_obj': page_obj})

@login_required
def edit_user(request, user_id=None):
    if not request.user.is_superuser and not request.user.is_staff:
        return redirect('home')  

    if user_id:
        # If user ID is provided, fetch the user object based on the user_id
        user = get_object_or_404(UserProfile2, pk=user_id)

        if request.method == 'POST':
            # If form is submitted, handle form submission and update user details
            form = UserProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('edit_user_list')  # Redirect to user profile page or any other page
        else:
            # If method is GET or form is not submitted, pre-fill the form with existing user details
            form = UserProfileForm(instance=user)

        return render(request, 'edit_user.html', {'form': form})
    
    else:
        # If user ID is not provided, display a list of users to select from
        users = UserProfile2.objects.all().order_by('name')
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'edit_user_list.html', {'page_obj': page_obj})
    


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


@login_required
def buy_course(request):
    courses = Course.objects.all()
    
    return render(request, 'buy_course.html', {'courses': courses})

@login_required
def contact_us(request):
    course_name = None
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        course_name = request.POST.get('course')  # Retrieve course name from the form
        message = request.POST.get('message')
        
        # Get the course object based on the course name
        try:
            selected_course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            selected_course = None
        
        # Create the contact object with the retrieved course
        contact = Contact(name=name, email=email, phone=phone, city=city, state=state, message=message, course=selected_course)
        contact.save()
        messages.success(request, 'Successful')
        
        return redirect('contact_us')
    else:
        course_name = request.GET.get('course')  # Retrieve course name from the URL
        cities = IndiaCities.objects.all()
        states = IndianStates.objects.all()
        return render(request, 'contact_us.html', {'user': request.user, 'selected_course_name': course_name, 'cities':cities, 'states':states})

