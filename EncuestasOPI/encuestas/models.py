from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


# Create your models here.
class Encuesta(models.Model):
	title = models.CharField(max_length=150, blank=False)
	slug = models.SlugField()
	creation_date = models.DateTimeField(auto_now_add=True)
	enabled = models.BooleanField(default=False)
	description = models.TextField(blank=True)

	def __unicode__(self):
		return u'{0}'.format(self.slug)

	@models.permalink
	def get_absolute_url(self):
		return ('single_view', (), {'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Encuesta, self).save(*args, **kwargs)