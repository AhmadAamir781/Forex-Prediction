from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages as django_messages
from django.contrib.auth.decorators import login_required
from .models import ContactMessage
from .forms import CreateUserForm, ContactForm
from django.contrib.auth import logout
from .ARIMAA import predict 

    
def Register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            if not request.path.startswith('/admin/'):
                django_messages.success(request, 'You have successfully registered!')
            return redirect('account:login')
        else:
            django_messages.error(request, 'Registration failed. Please correct the errors below.')

    context = {"form": form}
    return render(request, "Account/Register.html", context)


class CustomLoginView(LoginView):
    template_name = 'Account/Login.html'

    def form_invalid(self, form):
        django_messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('account:home') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_superuser:
            if self.request.session.pop('new_user_registered', False):
                context['new_user_registered_message'] = 'You have been registered successfully. Please log in.'
        return context
 
@login_required
def home(request):
    return render(request, 'Sites/Home.html')

@login_required
def prediction(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol', 'XAUUSD')
        model_type = request.POST.get('model', 'ARIMA')
        data = predict(symbol, model_type)
        return render(request, 'Sites/prediction.html', {'data': data, 'symbol': symbol, 'model': model_type})
    else:
        # Render the initial form
        return render(request, 'Sites/prediction.html')

@login_required
def About(request):
    return render(request, 'Sites/About.html')

@login_required
def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.user_id = request.user.id
            contact_message.save()
            return HttpResponse("Your message has been sent successfully!")
    else:
        form = ContactForm()
    return render(request, 'Sites/Contact.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('account:login')  
