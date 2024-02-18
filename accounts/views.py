from django.shortcuts import render, redirect
from .forms import CreateUser, UserProfileForm
from .models import CustomUser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserPasswordChangeForm
from django.views import View
from .models import CustomUser
from blog.models import RecipeModel
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from .password import generate_password

# Create your views here.
def signup(request):
    errors= None
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            #extract data from form
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            #create a user with this info
            user = CustomUser.objects.create_user(
                full_name= full_name,
                email= email,
                password= password
            )
            user.save()
            #get the domain of current site
            current_site = get_current_site(request)
            mail_subject= 'Activation link sent your email id'
            message = render_to_string('accounts/confirm_email.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            email = EmailMessage(
                mail_subject, message, to=[email,]
            )
            email.send()
            messages.info(request, 'Sent a confirmation link on your email. Please confirm for active your account.')
            return redirect('sign_up')
        else:
            errors = [message for error_list in form.errors.values() for message in error_list]
    return render(request, 'accounts/sign-up.html', {'errors': errors})

def activate(request, uidb64, token):
    #User model
    User = get_user_model()
    try:
        #find request user
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk= uid)
    except:
        user = None
    #check user and active true
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Link is invalid!')

class MyRecipe(View):
    @method_decorator(login_required(login_url='sign_in'))
    def get(self, request):
        recipes = RecipeModel.objects.filter(user= request.user).order_by('-create_at')
        paginator = Paginator(recipes, 6)
        page_number = request.GET.get('page')
        recipes_obj = paginator.get_page(page_number)
        return render(request, 'accounts/my-recipe.html', {'recipes': recipes_obj})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('update_profile')
    else:
        form = UserProfileForm(instance=user)
    print(form)
    return render(request, 'accounts/profile.html', {'form': form, 'user': user})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, error)
    return render(request, 'accounts/change-password.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, email= email, password= password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Email or Password invalid!')
    return render(request, 'accounts/sign-in.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


class ProfileVisit(View):
    def get(self, request, id):
        profile_info = CustomUser.objects.get(id= id)
        recipes = RecipeModel.objects.filter(user= profile_info).order_by(('-create_at'))

        paginator = Paginator(recipes, 6)
        page_number = request.GET.get('page')
        recipes_obj = paginator.get_page(page_number)
        return render(request, 'accounts/visit-profile.html', {'profile_info': profile_info, 'recipes': recipes_obj})

class ResetPassword(View):
    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            user = CustomUser.objects.filter(email= email)
            if user.exists():
                user = user[0]
                random_password = generate_password(10)
                user.set_password(random_password)
                user.save()
                current_site = get_current_site(request)
                message = render_to_string('accounts/confirm_email.html',{
                'user': user,
                'domain': current_site.domain,
                'temporary_password': random_password,
                })
                mail_subject= 'Reset Password!'
                email = EmailMessage(
                    mail_subject, message, to=[email,]
                )
                email.send()
                messages.info(request, 'Sent a temporary password in your email.')
            else:
                messages.error(request, 'Please provide a valid email!')
        return render(request, 'accounts/reset-password.html')
    def get(self, request):
        return render(request, 'accounts/reset-password.html')