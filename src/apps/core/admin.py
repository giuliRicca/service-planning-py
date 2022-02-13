from django.contrib import admin
from apps.core import models

admin.site.register([
    models.Event, 
    models.ServiceTime, 
    models.ServiceType, 
    models.Team,
    models.EventOrder,
    models.OrderItem,

])
