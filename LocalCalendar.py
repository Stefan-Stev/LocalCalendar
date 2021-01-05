import sys

from icalendar import Calendar,Event,Alarm
from datetime import datetime, timezone, timedelta

from pytz import UTC
import time
import threading
import icstojsonFile
import parser2
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
            print("DTSTAMPT ", component.get('dtstamp').dt)
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
def display_action2(lock,eveniment,f2):
    number_of_reps = int(eveniment['reps'])
    seconds = get_sec(eveniment['repeatafterseconds'],
                      eveniment['repeatafterminutes'],
                      eveniment['repeatafterhours'])
    for i in range(0, number_of_reps):
        lock.acquire()
        print("as", eveniment['action'])
        if eveniment['action'] == 'CONSOLE':

            print('-----------')
            print("Summary: ", eveniment['summary'])
            print("Start Date ", eveniment['dtstart'])
            print("End date ", eveniment['dtend'])
            print('-----------')
            lock.release()
            time.sleep(seconds)
        elif eveniment['action'] == 'FILE':
            f2.write('-----------')
            f2.write('\n')
            f2.write("Summary: " + eveniment['summary'])
            f2.write('\n')
            f2.write("Start Date: " + str(eveniment['dtstart']))
            f2.write('\n')
            f2.write("End date: " + str(eveniment['dtend']))
            f2.write('\n')
            f2.write('-----------')
            f2.write('\n')
            lock.release()
            time.sleep(seconds)
def adaugare_eveniment():

    event=Event()

    summary=input("Summary:\n")
    prioritate=input('Prioritate\n')
    print("Data Start:\n")
    an=int(input("Year:\n"))
    luna=int(input("Month:\n"))
    zi=int(input("Day:\n"))
    ora=int(input("Hour:\n"))
    minute=int(input("Minut:\n"))
    secunde=int(input("Second:\n"))
    print("Data End:\n")
    an2 = int(input("Year:\n"))
    luna2 = int(input("Month:\n"))
    zi2 = int(input("Day:\n"))
    ora2 = int(input("Hour:\n"))
    minute2 = int(input("Minut:\n"))
    secunde2 = int(input("Second:\n"))
    event.add('summary',summary)
    event.add('dtstart', datetime(an, luna, zi, ora,minute , secunde, tzinfo=UTC))
    event.add('dtend', datetime(an2, luna2,zi2,ora2, minute2, secunde2, tzinfo=UTC))
    event.add('priority',prioritate)
    event.add('dtstamp', datetime(2021, 4, 5, 0, 10, 0, tzinfo=UTC))
    event['uid'] = '20050115T101010/27346262376@mxm.dk'
    output=input("Output\n")
    reminder=input('Description\n')
    before_hours=int(input('BeforeHours\n'))
    before_minutes=int(input('BeforeMinutes\n'))
    before_seconds=int(input('BeforeSeconds\n'))
    repeat_after_hours=int(input("RepeatAfterHours\n"))
    repeat_after_minutes=int(input('RepeatAfterMinutes\n'))
    repeat_after_seconds=int(input('RepeatAfterSeconds\n'))
    repetari=int(input('NumberOfReps\n'))
    alarm = Alarm()
    alarm.add("action", output)
    alarm.add('description', reminder)
    alarm.add('beforeminutes', before_minutes)
    alarm.add('beforehours', before_hours)
    alarm.add('beforeseconds', before_seconds)
    alarm.add('numberofreps', repetari)
    alarm.add('repeatafterinseconds', repeat_after_seconds)
    alarm.add('repeatafterinminutes', repeat_after_minutes)
    alarm.add('repeatafterinhours', repeat_after_hours)
    event.add_component(alarm)

    # f=open('example.ics','rb')
    # d = f.read().decode()
    # f.close()
    # m = d.split("\n")
    # s = "\n".join(m[:-1])
    # fd = open("example.ics", "wb")
    # for i in range(len(s)):
    #     fd.write(s[i].encode())
    #
    # f = open('example.ics', 'ab')
    #
    # f.write(event.to_ical())
    # f.write('END:VCALENDAR'.encode())
    # f.close()
    f=open('example.ics','rb')
    data=f.readlines()
    data[len(data)-1]=event.to_ical()
    data.append('END:VCALENDAR'.encode())
    fd=open('example.ics','w')
    fd.write(data.__str__())

if __name__ == '__main__':

        try:
            f=open("text_display.txt","w")
        except OSError:
            print("Eroare la deschiderea fisierului text_display.txt")
            sys.exit()

        try:
            g = open('example.ics','rb')
        except OSError:
            print("Eroare la deschiderea fisieului example.ics")
            sys.exit()

        icstojsonFile.export_from_ics_to_json()
        ###daca utilizatorul vrea sa adauge evenimente noi in calendar
        raspuns = input("Vrei sa adaugi un eveniment nou?\n")
        while raspuns.lower()=='da':
            adaugare_eveniment()
            raspuns=input("Mai doriti sa adaugati evenimente?\n")
        gcal = Calendar.from_ical(g.read())
        ### sortam evenimentele in functie de prioritatea lor
        lista=gcal.subcomponents
        lista.sort(key=lambda x: x.get('PRIORITY'))
        ##
        g.close()


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
                if now>ora_trigger and now<component['dtend'].dt:
                        t=threading.Thread(target=display_action,args=(lock,component,f))
                        t.start()

        time.sleep(20)

        try:
            f.close()
        except OSError:
            print("Eroare la inchiderea fisieului")
            sys.exit()
        raspuns=input('Apasa orice tasta pentru a continua')
        lock2 = threading.Lock()
        f2=open('text_display2.txt','w')
        evenimente_format_custom=parser2.evenimente_format_custom()
        for eveniment in evenimente_format_custom:
                before_seconds=eveniment['beforeseconds']
                before_minutes=eveniment['beforeminutes']
                before_hours=eveniment['beforehours']
                seconds_trigger = timedelta(seconds=int(before_seconds))
                minutes_trigger = timedelta(minutes=int(before_minutes))
                hour_trigger = timedelta(hours=int(before_hours))
                eveniment['dtstart']=eveniment['dtstart'][:-6] ### elimin caracterele inutile din string pt a putea transforma in datetime
                ora_trigger =  datetime.strptime(eveniment['dtstart'], '%Y-%m-%d %H:%M:%S') - seconds_trigger
                ora_trigger = ora_trigger - minutes_trigger
                ora_trigger = ora_trigger - hour_trigger

                now = datetime.now()
                diferenta = now - ora_trigger
                if now > ora_trigger:
                    t = threading.Thread(target=display_action2, args=(lock2, eveniment, f2))
                    t.start()

        try:
            g.close()
        except OSError:
            print("Eroare la inchiderea fisieului")
            sys.exit()


