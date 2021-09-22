import re
from django.urls.base import reverse_lazy
from django.http import HttpResponse
from .forms import PersonDetailForm, UnSubscribeForm,\
     SubscribeForm, ImportantDateForm
from .models import ImportantDate

from django.shortcuts import render, redirect
from django.views import generic 

# Create your views here.


class ClassBasedFormView(generic.View):
    template_name = 'cbv-form.html'

    def get(self, request):
        form = PersonDetailForm(vip = True)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = PersonDetailForm(request.POST)
        if form.is_valid() :
            ## success 
            # print(form.cleaned_data)
            return redirect('formschapter:cbv-form')
        else:
            #invalid form data 
            return render(request, self.template_name,
                            {'form':form})           


class GenericFormView(generic.FormView):
    template_name = 'cbv-form.html'
    form_class = PersonDetailForm
    success_url = reverse_lazy('formschapter:gcbv-form')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['vip'] = self.request.user.groups.filter(name = "VIP").exists()
        return kwargs

## handle multiple forms in a single view Pattern
class NewsletterView(generic.TemplateView):
    template_name = 'newsletter.html'
    subscribe_form_class = SubscribeForm
    unsubscribe_form_class = UnSubscribeForm

    def get(self, request, *args, **kwargs):
        kwargs.setdefault('subscribe_form', self.subscribe_form_class())
        kwargs.setdefault('unsubscribe_form', self.unsubscribe_form_class())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data':self.request.POST,
            'files':self.request.FILES,

        }

        if 'subscribe_btn' in request.POST:
            form = self.subscribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, subscribe_form = form)
             # Use the form.cleaned_data["email"]
            print("Subscribed to {}".format(form.cleaned_data["email"]))
            return redirect("home")

        elif "unsubscribe_btn" in request.POST:
            form = self.unsubscribe_form_class(**form_args)
            if not form.is_valid():
                return self.get(request,
                                unsubscribe_form=form)
            # Use the form.cleaned_data["email"]
            print("Unsubscribed from {}".format(form.cleaned_data["email"]))
            return redirect("home")
        return super().get(request)



## CRUD patter views
# 1. detail 
class ImpDateDetail(generic.DetailView):
    model = ImportantDate


#2. create 
class ImpDateCreate(generic.CreateView):
    model = ImportantDate
    form_class = ImportantDateForm

#3. update
class  ImpDateUpdate(generic.UpdateView):
    model = ImportantDate
    form_class = ImportantDateForm

#4. delete 
class ImpDateDelete(generic.DeleteView):
    model = ImportantDate
    success_url = reverse_lazy(
        'formschapter:impdate-list'
    )

#5. list 


class ImpDateList(generic.ListView):
    model = ImportantDate


## secutiry chapter 12 
class XSSDemoView(generic.View):
    
    def get(self, request):
        """
            this code is insecure and prone to xss attacks
            do not ever never use it
        """
        if 'q' in request.GET:
            # manually avoid this attack by filtering the input 
            # q = re.search('\w*', request.GET['q'])
            return HttpResponse ("searched for {}".format(
                request.GET['q']
            ))
        else:
            return HttpResponse("""
                <form method= "get"> 
               
                <input type="text" name="q" placeholder="Search" value="" >
                <input type="submit" value="Search" name="searchbtn">
                </form>
            """)
