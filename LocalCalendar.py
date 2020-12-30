from icalendar import Calendar, Event, Alarm
from datetime import datetime, timezone, timedelta
from pytz import UTC # timezone
import time

def get_sec(seconds_after,minutes_after,hours_after):

    seconds=3600*int(hours_after)+60*int(minutes_after)+int(seconds_after)
    return seconds
def repeatafter(ora_trigger,seconds_after,minutes_after,hours_after,number_of_reps):
        for i in range(0,int(number_of_reps)):
           seconds=get_sec(seconds_after,minutes_after,hours_after)
           time.sleep(seconds)
           print("Summary: ", component.get('summary'))
           print("Start Date ", component.get('dtstart').dt)
           print("End date ", component.get('dtend'))
           print("ceva ", component.get('dtstamp'))



if __name__ == '__main__':
        g = open('example.ics','rb')

        gcal = Calendar.from_ical(g.read())
        print(gcal)
        global x
        for component in gcal.walk():
            if component.name == "VEVENT":
                before_seconds=component.subcomponents[0]['BEFORESECONDS']
                seconds_trigger=timedelta(seconds=int(before_seconds))
                ora_trigger=component.get('dtstart').dt-seconds_trigger
                before_minutes = component.subcomponents[0]['BEFOREMINUTES']
                minutes_trigger = timedelta(minutes=int(before_minutes))
                ora_trigger=ora_trigger-minutes_trigger
                before_hours=component.subcomponents[0]['BEFOREHOURS']
                hour_trigger=timedelta(hours=int(before_hours))
                ora_trigger=ora_trigger-hour_trigger

                print("Ora la care incepe eventul este",component.get('dtstart').dt)
                print("Ora trigger este" ,ora_trigger)
                now=datetime.now(timezone.utc)
                diferenta=now-ora_trigger
                if now>ora_trigger:
                        print("Summary: ",component.get('summary'))
                        print("Start Date " ,component.get('dtstart').dt)
                        print("End date ",component.get('dtend'))
                        print("ceva ",component.get('dtstamp'))
                        print(component.subcomponents[0]['ACTION'])
                        repeatafter(ora_trigger,component.subcomponents[0]['REPEATAFTERINSECONDS'],component.subcomponents[0]['REPEATAFTERINMINUTES'],component.subcomponents[0]['REPEATAFTERINHOURS'],component.subcomponents[0]['NUMBEROFREPS'])

        g.close()


