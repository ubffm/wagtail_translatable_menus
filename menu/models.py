from django.db import models

from django_extensions.db.fields import AutoSlugField

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel, PageChooserPanel
# from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable, TranslatableMixin

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class MenuItem(TranslatableMixin, Orderable):

    link_title = models.CharField(max_length=128)
    link_url = models.URLField(blank=True)
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey('Menu', related_name='menu_items')

    panel = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        else:
            return '#'

    class Meta:
        ordering = ['sort_order']
        unique_together = ('translation_key', 'locale')


# @register_snippet
class Menu(TranslatableMixin, ClusterableModel):
    title = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='title', editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
        ], heading='Menu'),
        InlinePanel('menu_items', label='Menu Item')
    ]

    def __str__(self):
        return self.title
