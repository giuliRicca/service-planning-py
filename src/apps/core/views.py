# apps/core/views.py
import csv
from datetime import timedelta
from django.apps import apps
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from apps.core.utils import PlansCalendar
from apps.core.models import OrderItem, ServiceType, Event, EventOrder
from apps.core.forms import OrderItemForm, ServiceTypeForm, EventForm


@login_required(login_url='login')
def schedule_view(request):
    context = {}
    context['events'] = [x for x in Event.objects.all() if x.is_active]
    context['calendar'] = PlansCalendar().formatmonth()
    return render(request, 'core/schedule.html', context=context)

@login_required(login_url='login')
def plans_view(request):
    context = {}
    context['events'] = [x for x in Event.objects.all() if x.is_active]
    context['service_types'] = ServiceType.objects.all()
    context['calendar'] = PlansCalendar().formatmonth()
    return render(request, 'core/plans.html', context=context)


@login_required(login_url='login')
def service_types_add(request):
    context = {}
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plans')
        context['form'] = form

    context['form'] = ServiceTypeForm()

    return render(request, 'core/service_types.html', context)


@login_required(login_url="login")
def event_view(request, id, item_id=None):
    context = {}
    context['event'] = Event.objects.get(id=id)
    item = get_object_or_404(OrderItem, pk=item_id) if item_id else None
    context['edit'] = True if item else False

    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=item or None)
        if form.is_valid():
            item = form.save(commit=False)
            item.order = context['event'].eventorder
            item.length = timedelta(
                minutes=int(request.POST.get('minutes')),
                seconds=int(request.POST.get('seconds'))
            )
            item.save()
        else:
            print(form.errors.as_data())

    context['form'] = OrderItemForm(instance=item or None)

    return render(request, "core/event.html", context)

@login_required(login_url="login")
def add_edit_event(request, id=None):
    context = {}
    event = get_object_or_404(Event, pk=id) if id else None
    
    form = EventForm(instance=event if event else None)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event if event else None)
        if form.is_valid():
            form.save()
            return redirect('plans')
    
    context['form'] = form
    context['edit'] = True if event else False
    return render(request, 'core/add_edit_events.html', context)

@login_required(login_url="login")
def edit_item_view(request, item_id):
    context = {}
    item = get_object_or_404(OrderItem, pk=item_id)
    if not item: return redirect('plans')
    
    context['event'] = Event.objects.get(id=item.order.event.id)
    context['edit'] = True

    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.length = timedelta(
                minutes=int(request.POST.get('minutes')),
                seconds=int(request.POST.get('seconds'))
            )
            item.save()

            return redirect('event', id=context['event'].id)
        else:
            print(form.errors.as_data())

    context['form'] = OrderItemForm(instance=item)

    return render(request, "core/event.html", context)
 
@login_required(login_url='login')
def delete_view(request, model, id):
    model = apps.get_model(app_label='apps_core', model_name=model) 
    item = get_object_or_404(model, pk=id) if model else None
    if not item: return
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def export_order_csv(request, id):
    order = get_object_or_404(EventOrder, pk=id)
    # if order is not found redirect to previous page
    if not order: return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # if exists then...
    order_items = order.get_items().values_list('length', 'title', 'description', 'person', 'item_type')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['length', 'title', 'description', 'person', 'item_type'])
    for order_item in order_items:
        writer.writerow(order_item)
        
    return response
