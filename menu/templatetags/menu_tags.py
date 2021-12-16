from django import template

#from wagtail.core import locale as page_locale

from ..models import Menu

register = template.Library()

@register.simple_tag()
def get_menu(slug,locale):
	#loc_id = page_locale.objects.get(language_code=locale)

	try:
		return Menu.objects.get(slug=slug,locale__language_code=locale)
	except:
		return Menu.objects.get(slug=slug,locale__language_code='en')