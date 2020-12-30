from icalendar import Calendar, Event, Alarm
from datetime import datetime, timezone, timedelta
from pytz import UTC # timezone
cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Coding with my Russian friend')
event.add('dtstart', datetime(2020,12,31,8,0,0,tzinfo=UTC))
event.add('dtend', datetime(2020,4,5,10,0,0,tzinfo=UTC))
event.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event['uid'] = '20050115T101010/27346262376@mxm.dk'
event.add('priority', 2)

reminderMinutes='20'
alarm = Alarm()
alarm.add("action", "CONSOLE")
alarm.add('description', "Reminder")
#alarm2.add("trigger", datetime(2020,4,4,7,0,0,tzinfo=UTC))
alarm.add('beforeminutes',0)
alarm.add('beforehours',24)
alarm.add('beforeseconds',0)
alarm.add('numberofreps',2)
alarm.add('repeatafterinseconds',5)
alarm.add('repeatafterinminutes',0)
alarm.add('repeatafterinhours',0)
alarm.add('repeatafterinyears',0)
event.add_component(alarm)
cal.add_component(event)


event2 = Event()
event2.add('summary', 'Python meeting about calendaring')
event2.add('dtstart', datetime(2020,4,4,8,0,0,tzinfo=UTC))
event2.add('dtend', datetime(2020,4,5,10,0,0,tzinfo=UTC))
event2.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event2['uid'] = '20050115T101010/27346262376@mxm.dk'
event2.add('priority', 2)
reminderHours=3
reminderSeconds=0
alarm2 = Alarm()
alarm2.add("action", "FILE")
alarm2.add('description', "Reminder")
alarm2.add('beforeminutes',reminderMinutes)
alarm2.add('beforehours',reminderHours)
alarm2.add('beforeseconds',reminderSeconds)
alarm2.add('numberofreps',3)
alarm2.add('repeatafterinseconds',2)
alarm2.add('repeatafterinminutes',0)
alarm2.add('repeatafterinhours',0)
alarm2.add('repeatafterinyears',0)
event2.add_component(alarm2)
cal.add_component(event2)

event3 = Event()
event3.add('summary', 'Meeting with president')
event3.add('dtstart', datetime(2020,4,4,8,0,0,tzinfo=UTC))
event3.add('dtend', datetime(2020,4,5,10,0,0,tzinfo=UTC))
event3.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event3['uid'] = '20050115T101010/27346262376@mxm.dk'
event3.add('priority', 1)
reminderHours=3
reminderSeconds=0
alarm3 = Alarm()
alarm3.add("action", "CONSOLE")
alarm3.add('description', "Reminder")
alarm3.add('beforeminutes',reminderMinutes)
alarm3.add('beforehours',reminderHours)
alarm3.add('beforeseconds',reminderSeconds)
alarm3.add('numberofreps',3)
alarm3.add('repeatafterinseconds',2)
alarm3.add('repeatafterinminutes',0)
alarm3.add('repeatafterinhours',0)
alarm3.add('repeatafterinyears',0)
event3.add_component(alarm3)
cal.add_component(event3)



event4 = Event()
event4.add('summary', 'Meeting with teacher')
event4.add('dtstart', datetime(2020,4,4,8,0,0,tzinfo=UTC))
event4.add('dtend', datetime(2020,4,5,10,0,0,tzinfo=UTC))
event4.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event4['uid'] = '20050115T101010/27346262376@mxm.dk'
event4.add('priority', 1)
reminderHours=3
reminderSeconds=0
alarm4 = Alarm()
alarm4.add("action", "FILE")
alarm4.add('description', "Reminder")
alarm4.add('beforeminutes',reminderMinutes)
alarm4.add('beforehours',reminderHours)
alarm4.add('beforeseconds',reminderSeconds)
alarm4.add('numberofreps',3)
alarm4.add('repeatafterinseconds',2)
alarm4.add('repeatafterinminutes',0)
alarm4.add('repeatafterinhours',0)
alarm4.add('repeatafterinyears',0)
event4.add_component(alarm4)
cal.add_component(event4)

event5 = Event()
event5.add('summary', 'Visiting Norway')
event5.add('dtstart', datetime(2021,4,4,8,0,0,tzinfo=UTC))
event5.add('dtend', datetime(2021,4,5,10,0,0,tzinfo=UTC))
event5.add('dtstamp', datetime(2021,4,5,0,10,0,tzinfo=UTC))
event5['uid'] = '20050115T101010/27346262376@mxm.dk'
event5.add('priority', 4)
reminderHours=3
reminderSeconds=0
alarm5 = Alarm()
alarm5.add("action", "FILE")
alarm5.add('description', "Reminder")
alarm5.add('beforeminutes',20)
alarm5.add('beforehours',reminderHours)
alarm5.add('beforeseconds',reminderSeconds)
alarm5.add('numberofreps',3)
alarm5.add('repeatafterinseconds',2)
alarm5.add('repeatafterinminutes',0)
alarm5.add('repeatafterinhours',0)
alarm5.add('repeatafterinyears',0)
event5.add_component(alarm5)
cal.add_component(event5)



f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()