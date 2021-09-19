from django.shortcuts import render, redirect
from django.views.generic import View

# # Create your views here.
# from .models import PersonDetailForm
# class ClassBasedFormView(View):
#     template_name = 'my_template'

#     def get(self, request):
#         form = PersonDetailForm()
#         return render(request, self.template_name, {'form':form})
    
#     def post(self, request):
#         form = PersonDetailForm(request.POST)
#         if form.is_valid():
#             # do logic 
#             form.save()
#             redirect('success')

#         else:
#             #invalid form
#             return render(request, self.template_name,{'form':form})