from icalendar import Calendar
from datetime import datetime, timezone, timedelta
from pytz import UTC # timezone
import time
import threading
import icstojsonFile
lock = threading.Lock()
def get_sec(seconds_after,minutes_after,hours_after):

    seconds=3600*int(hours_after)+60*int(minutes_after)+int(seconds_after)
    return seconds




def display_action(lock,component,f):
    number_of_reps=int(component.subcomponents[0]['NUMBEROFREPS'])
    seconds=get_sec(component.subcomponents[0]['REPEATAFTERINSECONDS'],component.subcomponents[0]['REPEATAFTERINMINUTES'],component.subcomponents[0]['REPEATAFTERINHOURS'])
    for i in range(0,number_of_reps):
        lock.acquire()
        print("as",component.subcomponents[0]['ACTION'])
        if component.subcomponents[0]['ACTION']=='CONSOLE':

            print('-----------')
            print("Summary: ", component.get('summary'))
            print("Start Date ", component.get('dtstart').dt)
            print("End date ", component.get('dtend').dt)
            print("ceva ", component.get('dtstamp').dt)
            print('-----------')
            lock.release()
            time.sleep(seconds)
        elif component.subcomponents[0]['ACTION']=='FILE':
            f.write('-----------')
            f.write('\n')
            f.write("Summary: "+ component.get('summary'))
            f.write('\n')
            f.write("Start Date: "+ str(component.get('dtstart').dt))
            f.write('\n')
            f.write("End date: "+ str(component.get('dtend').dt))
            f.write('\n')
            f.write("DTSTAMPT: "+ str(component.get('dtstamp').dt))
            f.write('\n')
            f.write('-----------')
            f.write('\n')
            lock.release()
            time.sleep(seconds)

if __name__ == '__main__':
        f=open("text_display.txt","w")
        g = open('example.ics','rb')
        icstojsonFile.export_from_ics_to_json()
        # gcal2=Calendar.from_ical(g.read())
        # for component in gcal2.walk():

        gcal = Calendar.from_ical(g.read())
        ### sortam evenimentele in functie de prioritatea lor
        lista=gcal.subcomponents
        lista.sort(key=lambda x: x.get('PRIORITY'))
        ##

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
                        t=threading.Thread(target=display_action,args=(lock,component,f))
                        t.start()



        g.close()


