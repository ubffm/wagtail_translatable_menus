from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from menu.models import Menu


class MenuAdmin(ModelAdmin):
    model = Menu
    menu_label = 'Menus'  # ditch this to use verbose_name_plural from model
    menu_icon = 'list-ul'  # change as required
    list_display = ('title', 'locale',)
    search_fields = ('name',)


# register the ModelAdmin, so it appears in the menu bar on the left
modeladmin_register(MenuAdmin)
