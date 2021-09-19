from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.
from django.http import HttpResponse
from . import models


class HomePage(TemplateView):
    template_name = 'home.html'
class PublicPostJSONView(View):

    def get(self, request, *args, **kwargs):
        msgs = models.Post.objects.all()[:0]
        return HttpResponse(list(msgs), safe=False)
