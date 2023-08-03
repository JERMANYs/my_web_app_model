# Django

## การสร้าง Project
    django-admin startproject *ขื่อโปรเจ็ค*

## การสร้าง env
    python -m venv env

## การรัน Server Django
    python manage.py runserver

## [templates](https://github.com/JERMANYs/my_web_app_model/tree/main/templates)
```python
{% extends 'base.html' %}
<!---->
{% block  title%}ติดต่อฉัน{% endblock title %}
<!---->
{% block content %}<table class="table">
  <!---->
  {{ message }}
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">ID  </th>
        <th scope="col">Prefix</th>
        <th scope="col">Name</th>
        <th scope="col">Lastname</th>
        <th scope="col">Phone</th>
        <th scope="col">Address</th>
      </tr>
    </thead>
    <tbody>
      {% for student in students %}
      <tr>
        <th scope="row">1</th>
        <td><a href="{% url 'details' student.id %}">{{ student.std_id}}</a><td>
        <td>{{ student.prefix }}</td>
        <td>{{ student.name }}</td>
        <td>{{ student.lastname }}</td>
        <td>{{ student.phone }}</td>
        <td>{{ student.address }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table> {% endblock content %}
```
## [webapp](https://github.com/JERMANYs/my_web_app_model/tree/main/webapp)

```python
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webpage.urls')),
]
```

## [webpage](https://github.com/JERMANYs/my_web_app_model/tree/main/webpage)
```python
from django.contrib import admin

# Register your models here.
from . models import student


@admin . register(student)
class Admin(admin.ModelAdmin):
    list_display = ("std_id","prefix","name", "lastname","phone")
    search_fields = ("std_id","name","lastname","phone")


```
