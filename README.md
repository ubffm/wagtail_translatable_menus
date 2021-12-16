# wagtail_translatable_menus

This Wagtail CMS App adds translatable menus to your Wagtail CMS project. It was developed and used for the [Specialised Information Service African Studies](https://africanstudieslibrary.org).

# Installation

Clone this repository and copy the ```menu``` directory into your Wagtail Project.
Enable the application by adding it to your ```INSTALLED_APPLICATIONS``` list like so:
```python
INSTALLED_APPLICATIONS = [
	...,
	'menu',
	...
]
```

 Run ```python manage.py makemigrations``` to create any necessary migrations and ```python manage.py migrate``` to apply the migrations to your database.

# Usage

This app adds a menu to your Wagtail CMS backend that allows you to create any menu you'd like. Individual menu Items can be regular URLs *or* pages in your Wagtail Site. The menus are also translatable via [Wagtail Localize](https://www.wagtail-localize.org/), so you can even use autotranslation to translate the indivdual menu entries. **When doing so, please keep in mind to change the URLs or linked pages to the one reflecting the given language**

The menu items are orderable, so the will appear in the order you put them into, when loaded into your templates.

## Usage in templates

To automatically select the correct menu for your locale, you can use the template-tag provided with this application. Use it in your templates to select the correct menu like so:

```Jinja2
{% load static wagtailuserbar wagtailcore_tags menu_tags i18n%}

{% get_current_language as LANGUAGE_CODE %}

{% get_menu 'main-navigation' LANGUAGE_CODE as main_nav %}
<html>
	...

	<body>

	<div class="collapse navbar-collapse flex-grow-1 text-end flex-nowrap" id="navbar">
            <ul class="navbar-nav ms-auto me-5">
                {% for item in main_nav.menu_items.all %}
                    <li class="nav-item">
                        <a class="nav-link" href="{{ item.link }}" {%if item.open_in_new_tab %} target="_blank" {%endif%}>{{ item.link_title }}</a>
                    </li>
                {% endfor %}
    ...

```

# Dependencies

This application implements translatable menus for Wagtail Localize, so it depends on [Wagtail Localize](https://www.wagtail-localize.org/)

# Environment

Tested on:

- Python 3.8, 3.9, 3.10
- Django 3.1, 3.2
- Wagtail 2.13, 2.14, 2.15
