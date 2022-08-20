from datetime import date, timedelta
from django.db import models
from django.dispatch import receiver

class ServiceTime(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField(unique=True)
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time.strftime("%H:%M %p"))

class Team(models.Model):
    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name

class ServiceType(models.Model):
    RECUR_OPTIONS = [
        ('a', 'Weekly'),
        ('b', 'Daily'),
        ('c', 'Every Weekday'),
        ('e', 'Every Other Week'),
        ('d', 'Monthly'),
    ]
    name = models.CharField(max_length=155, unique=True)
    recur = models.CharField(max_length=1,
                            choices=RECUR_OPTIONS,
                            null=True, default='a')
    times = models.ManyToManyField(ServiceTime)
    teams = models.ManyToManyField(Team, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def identifier(self):
        return self.name.split()[0] + str(self.id)

    @property
    def get_events(self):
        return self.event_set.all()

class Event(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=155, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_active(self):
        if self.date:
            now = date.today()
            if self.date >= now:
                return True
            else:
                return False
        return

    @property
    def get_times(self):
        return [time for time in self.service_type.times.all()]
    
    @property
    def model_name(self):
        return self.__class__.__name__
    


class EventOrder(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.event) + ": Order"

    def get_items(self):
        items = self.orderitem_set.all()
        return items

    @property
    def total_length(self):
        items = self.orderitem_set.all()
        total_seconds =  sum([item.length.total_seconds() for item in items])
        return timedelta(seconds=total_seconds)

@receiver(models.signals.post_save, sender=Event)
def create_event_order(sender, instance, created, **kwargs):
    if created:
        EventOrder.objects.create(event=instance)

class OrderItem(models.Model):
    TYPE_OPTIONS = [
        ('a', 'Item'),
        ('b', 'Header'),
    ]
    order = models.ForeignKey(EventOrder, on_delete=models.CASCADE)
    length = models.DurationField(blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    person = models.CharField(max_length=120, null=True, blank=True)
    item_type = models.CharField(max_length=1,
                            choices=TYPE_OPTIONS,
                            null=True, default='a')

    def __str__(self):
        return self.title
    
    @property
    def model_name(self):
        return self.__class__.__name__