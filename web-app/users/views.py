from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import DriverRegisterForm, RiderRegisterForm
from django.contrib.auth import login, authenticate
from django.views.generic import UpdateView
from .models import Myuser
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.forms.utils import ErrorList

def rider_register(request):
    if request.method == 'POST':
        form = RiderRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Your account has been created! You can login now')
            return redirect('login')
    else:
        form = RiderRegisterForm() 
    return render(request, 'users/register.html', {'form': form})


def driver_register(request):
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Your account has been created! You can login now')
            return redirect('login')
    else:
        form = DriverRegisterForm() 
    return render(request, 'users/register.html', {'form': form})

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update.html'
    model = Myuser
    fields = ['vehicle_type','license_plate', 'max_passenger']

    def get_form(self):
        form = super().get_form()
        return form

    def form_valid(self, form):
        if (form.instance.license_plate == 'None'):
            messages.warning(self.request, f'Please input a valid license plate')
            return self.form_invalid(form)

        if (not form.instance.max_passenger):
            messages.warning(self.request, f'max passenger cannot be 0')
            return self.form_invalid(form)

        return super().form_valid(form)

def SuccessUpdateView(request):
    return render(request, 'users/success-update.html')
    '''
    def get_form(self):
        form = super().get_form()
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.owner:
            return True
        return False
        '''

 
'''
@login_required
def goride(request):
    return render(request, 'users/goride.html')

@login_required
def goshare(request):
    return render(request, 'users/goshare.html')

@login_required
def godrive(request):
    return render(request, 'users/godrive.html')

              <div class="list-group">
                <a href="{%  %}" class="list-group-item list-group-item-action">
                  Go Ride
                </a>
                <a href="#" class="list-group-item list-group-item-action">Go Share</a>
                <a href="#" class="list-group-item list-group-item-action">Go Drive</a>
              </div>
'''


