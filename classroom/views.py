from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

# Create your views here.
# def home_view(request):
#     return render(request, 'classroom/home.html')

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    template_name = 'classroom/contact.html'
    form_class = ContactForm

    #on success
    #remember this is a url and not the path to template
    # success_url = '/classroom/thank_you/' # you can use this or you can use reverse_lazy
    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form) #this is always the last statement. If you want to do anything before this, you can do that
    