from icalendar import Calendar, Event, Alarm
from datetime import datetime, timezone, timedelta
from pytz import UTC # timezone
cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Coding with my Russian friend')
event.add('dtstart', datetime(2021,1,5,0,0,tzinfo=UTC))
event.add('dtend', datetime(2021,4,5,10,0,0,tzinfo=UTC))
event.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event['uid'] = '20050115T101010/27346262376@mxm.dk'
event.add('priority', 2)

reminderMinutes='20'
alarm = Alarm()
alarm.add("action", "CONSOLE")
alarm.add('description', "Reminder")
#alarm2.add("trigger", datetime(2020,4,4,7,0,0,tzinfo=UTC))
alarm.add('beforeminutes',0)
alarm.add('beforehours',100)
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
event2.add('dtstart', datetime(2021,1,7,11,0,0,tzinfo=UTC))
event2.add('dtend', datetime(2021,4,5,10,0,0,tzinfo=UTC))
event2.add('dtstamp', datetime(2020,4,5,0,10,0,tzinfo=UTC))
event2['uid'] = '20050115T101010/27346262376@mxm.dk'
event2.add('priority', 2)
reminderHours=100
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
event3.add('dtstart', datetime(2021,1,10,8,0,0,tzinfo=UTC))
event3.add('dtend', datetime(2021,4,5,10,0,0,tzinfo=UTC))
event3.add('dtstamp', datetime(2021,4,5,0,10,0,tzinfo=UTC))
event3['uid'] = '20050115T101010/27346262376@mxm.dk'
event3.add('priority', 1)
reminderHours=100
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
event4.add('dtstart', datetime(2021,1,7,10,0,0,tzinfo=UTC))
event4.add('dtend', datetime(2021,4,5,10,0,0,tzinfo=UTC))
event4.add('dtstamp', datetime(2021,4,5,0,10,0,tzinfo=UTC))
event4['uid'] = '20050115T101010/27346262376@mxm.dk'
event4.add('priority', 1)
reminderHours=72
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


g = open('example.ics', 'rb')
gcal2=Calendar.from_ical(g.read())
fd=open('format.txt','w')

for component in gcal2.walk():
  if component.name == "VEVENT":
    fd.write('<STARTEVENT>')
    fd.write('\n')
    fd.write('SUMMARY= ')
    summary=component.get('summary')
    fd.write(summary)
    fd.write('\n')
    dtstart=str(component.get('dtstart').dt)
    fd.write('dtstart= ')
    fd.write(dtstart)
    fd.write('\n')
    fd.write('dtend= ')
    dtend=str(component.get('dtend').dt)
    fd.write(dtend)
    fd.write('\n')
    fd.write('priority= ')
    prioritate=str(component.get('priority'))
    fd.write(prioritate)
    fd.write('\n')
    fd.write('<STARTALARM>')
    fd.write('\n')
    fd.write('DESCRIPTION= ')
    descriere=component.subcomponents[0]['DESCRIPTION']
    fd.write(descriere)
    fd.write('\n')
    actiune=component.subcomponents[0]['ACTION']
    fd.write('ACTION= ')
    fd.write(actiune)
    fd.write('\n')
    beforehours=component.subcomponents[0]['BEFOREHOURS']
    beforeminutes=component.subcomponents[0]['BEFOREMINUTES']
    beforeseconds=component.subcomponents[0]['BEFORESECONDS']
    fd.write('BEFOREHOURS= ')
    fd.write(beforehours)
    fd.write('\n')
    fd.write('BEFOREMINUTES= ')
    fd.write(beforeminutes)
    fd.write('\n')
    fd.write('BEFORESECONDS= ')
    fd.write(beforeseconds)
    fd.write('\n')
    reps=component.subcomponents[0]['NUMBEROFREPS']
    fd.write('REPS: ')
    fd.write(reps)
    fd.write('\n')
    repeatafterhours=component.subcomponents[0]['REPEATAFTERINHOURS']
    fd.write('REPEATAFTERINHOURS= ')
    fd.write(repeatafterhours)
    fd.write('\n')
    repeatafterminutes=component.subcomponents[0]['REPEATAFTERINMINUTES']
    fd.write('REPEATAFTERINMINUTES= ')
    fd.write(repeatafterminutes)
    fd.write('\n')
    repeatafterseconds=component.subcomponents[0]['REPEATAFTERINSECONDS']
    fd.write('REPEATAFTERINSECONDS= ')
    fd.write(repeatafterseconds)
    fd.write('\n')
    repeatafterinyears=component.subcomponents[0]['REPEATAFTERINYEARS']
    fd.write('REPEATAFTERINYEARS= ')
    fd.write(repeatafterinyears)
    fd.write('\n')
    fd.write('<ENDALARM>')
    fd.write('\n')
    fd.write('<ENDEVENT>')
    fd.write('\n')


fd.close()