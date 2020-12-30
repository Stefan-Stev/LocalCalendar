from icalendar import Calendar, Event, Alarm
from datetime import datetime, timezone, timedelta
from pytz import UTC # timezone
cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

# event = Event()
# event.add('summary', 'Python meeting about calendaring')
# event.add('dtstart', datetime(2020,4,4,8,0,0,tzinfo=UTC))
# event.add('dtend', datetime(2020,4,5,10,0,0,tzinfo=UTC))
# event.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
# event['uid'] = '20050115T101010/27346262376@mxm.dk'
# event.add('priority', 5)

reminderMinutes='20'
# alarm = Alarm()
# alarm.add("action", "DISPLAYONCONSOLE")
# alarm['uid']='1111'
# alarm.add('description', "Reminder")
# alarm.add('trigger',timedelta(minutes=-reminderMinutes))
# The only way to convince Outlook to do it correctly
#alarm.add("TRIGGER;RELATED=START", "-PT{0}M".format(reminderMinutes))
#event.add_component(alarm)
#cal.add_component(event)


event2 = Event()
event2.add('summary', 'Python meeting about calendaring')
event2.add('dtstart', datetime(2020,4,4,8,0,0,tzinfo=UTC))
event2.add('dtend', datetime(2020,4,5,10,0,0,tzinfo=UTC))
event2.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event2['uid'] = '20050115T101010/27346262376@mxm.dk'
event2.add('priority', 5)
reminderHours=3
reminderSeconds=0
alarm2 = Alarm()
alarm2.add("action", "DISPLAYONCONSOLE")
alarm2.add('description', "Reminder")
#alarm2.add("trigger", datetime(2020,4,4,7,0,0,tzinfo=UTC))
alarm2.add('beforeminutes',reminderMinutes)
alarm2.add('beforehours',reminderHours)
alarm2.add('beforeseconds',reminderSeconds)
alarm2.add('numberofreps',3)
alarm2.add('repeatafterinseconds',20)
alarm2.add('repeatafterinminutes',0)
alarm2.add('repeatafterinhours',0)
alarm2.add('repeatafterinyears',0)
event2.add_component(alarm2)
cal.add_component(event2)

f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()