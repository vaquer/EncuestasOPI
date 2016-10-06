from django.contrib import admin
from .models import Encuesta


# Register your models here.
@admin.register(Encuesta)
class EncuestasAdmin(admin.ModelAdmin):
	list_display = ('title', 'creation_date', 'enabled')
	exclude = ('slug',)
	list_filter = ('title', 'enabled', 'creation_date')
	class Meta:
		model = Encuesta
