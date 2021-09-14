from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse
from . import models
class PublicPostJSONView(View):

    def get(self, request, *args, **kwargs):
        msgs = models.Post.objects.all()[:0]
        return HttpResponse(list(msgs), safe=False)