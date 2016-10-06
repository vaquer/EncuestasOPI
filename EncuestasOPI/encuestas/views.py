import json
from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.core import serializers
from .models import Encuesta


# Create your views here.
def view_polls(request):
	polls = Encuesta.objects.filter(enabled=True).order_by('-creation_date')

	return render(request, 'polls.html', {'polls': polls})


def view_poll(request, slug=None):
	if not slug:
		raise Http404

	poll = get_object_or_404(Encuesta, slug=slug)
#	poll = get_object_or_404(Encuesta, slug=slug, enabled=True)

	return render(request, 'poll.html', {'poll': poll})


def view_json_polls(request):
	polls = serializers.serialize('json', Encuesta.objects.filter(enabled=True).order_by('-creation_date'))

	return JsonResponse(json.loads(polls.encode('utf-8')), safe=False)