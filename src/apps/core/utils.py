from calendar import HTMLCalendar
from datetime import datetime
from apps.core.models import Event

class PlansCalendar(HTMLCalendar):
	def __init__(self,*args, **kwargs):
		super().__init__(*args, **kwargs)
		today=datetime.now()
		self.year = today.year
		self.month = today.month
		self.events = []
		self.cssclass_month = 'table calendar table-borderless'


	def formatday(self, day):
		cssclass = ''
		if day[0]==0:
			return '<td class="noday">&nbsp;</td>'
		# add active class to cell if there is an event there
		for event in self.events:
			if event.date.day == day[0]: cssclass = 'active'

		return '<td class="%s">%d</td>' % (cssclass, day[0])
	
	def formatweek(self, theweek):
		s = ''.join(self.formatday(d) for d in theweek)
		return "<tr class='week'>%s</tr>" % s

	def formatmonth(self, withyear=True):
		"""
		Return a formatted month as a table.
		"""
		self.events = [x for x in Event.objects.filter(date__month=self.month) if x.is_active]
		v = []
		a = v.append
		a('<table cellpadding="0" cellspacing="0" class="%s">' % (
			self.cssclass_month))
		a('\n')
		a(self.formatmonthname(self.year, self.month, withyear=withyear))
		a('\n')
		a(self.formatweekheader())
		a('\n')
		for week in self.monthdays2calendar(self.year, self.month):
			a(self.formatweek(week))
			a('\n')
		a('</table>')
		a('\n')
		return ''.join(v)