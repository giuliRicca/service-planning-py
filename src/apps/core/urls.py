from django.urls import path, include
from apps.core import views

urlpatterns = [
    path("schedule/", views.schedule_view, name='schedule'),
    path("plans/", views.plans_view, name='plans'),
    path("plans/<int:id>/", views.event_view, name='event'),
    path("plans/<int:id>/<int:item_id>/", views.event_view, name='event'),
    path("plans/add/", views.add_edit_event, name='add_edit_event'),
    path("plans/edit/<int:id>", views.add_edit_event, name='add_edit_event'),
    path("delete/<str:model>/<int:id>/", views.delete_view, name='delete'),
    path("plans/edit_item/<int:item_id>/", views.edit_item_view, name='edit_item'),
    path("service_types/add/", views.service_types_add, name='new_service_type'),
    path('export/csv/<int:id>', views.export_order_csv, name='export_order_csv'),
    path("auth/", include('apps.auth.urls')),
]