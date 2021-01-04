import re


rx_dict={
    'summary': re.compile(r'SUMMARY= (?P<summary>.*)\n'),
    'dtstart':re.compile(r'dtstart= (?P<dtstart>.*)\n'),
    'dtend':re.compile(r'dtend= (?P<dtend>.*)\n'),
    'action':re.compile(r'ACTION= (?P<action>.*)\n'),
    'priority':re.compile(r'priority= (?P<priority>.*)\n'),
    'beforehours':re.compile(r'BEFOREHOURS= (?P<beforehours>.*)\n'),
    'beforeminutes':re.compile(r'BEFOREMINUTES= (?P<beforeminutes>.*)\n'),
    'beforeseconds':re.compile(r'BEFORESECONDS= (?P<beforeseconds>.*)\n'),
    'reps':re.compile(r'REPS: (?P<reps>.*)\n'),
    'repeatafterhours':re.compile(r'REPEATAFTERINHOURS= (?P<repeatafterhours>.*)\n'),
    'repeatafterminutes':re.compile(r'REPEATAFTERINMINUTES= (?P<repeatafterminutes>.*)\n'),
    'repeatafterseconds':re.compile(r'REPEATAFTERINSECONDS= (?P<repeatafterseconds>.*)\n')

}


def parse_line(linie):
    for key,rx in rx_dict.items():
        match=rx.search(linie)
        if match:
            return key,match
    return None, None

def evenimente_format_custom():
    evenimente=list()

    with open('format.txt','r') as f:

        line=f.readline()
        summary='0'
        dtstart='0'
        dtend='0'
        action='0'
        beforehours='0'
        beforeminutes='0'
        beforeseconds='0'
        reps='0'
        repeatafterhours='0'
        repeatafterseconds='0'
        repeatafterminutes='0'
        priority='0'
        while line:
            eveniment = dict()
            key,match=parse_line(line)
            if '<ENDEVENT>' in line:
               eveniment['summary']=summary
               eveniment['dtstart']=dtstart
               eveniment['dtend']=dtend
               eveniment['action']=action
               eveniment['beforehours']=beforehours
               eveniment['beforeminutes']=beforeminutes
               eveniment['beforeseconds']=beforeseconds
               eveniment['reps']=reps
               eveniment['repeatafterhours']=repeatafterhours
               eveniment['repeatafterminutes']=repeatafterminutes
               eveniment['repeatafterseconds']=repeatafterseconds
               eveniment['priority']=priority
               evenimente.append(eveniment)

            if key=='summary':
                summary=match.group('summary')
                #print(summary)
            if key=='dtstart':
                dtstart=match.group('dtstart')
               # print(dtstart)
            if key == 'dtend':
                dtend = match.group('dtend')
               # print(dtend)
            if key == 'action':
                action = match.group('action')
               # print(action)
            if key == 'beforehours':
                beforehours = match.group('beforehours')
                #print(beforehours)
            if key == 'beforeminutes':
                beforeminutes = match.group('beforeminutes')
               # print(beforeminutes)
            if key == 'beforeseconds':
                beforeseconds = match.group('beforeseconds')
                #print(dtstart)
            if key == 'reps':
                reps = match.group('reps')
                #print(reps)
            if key == 'repeatafterhours':
                repeatafterhours = match.group('repeatafterhours')
               # print(repeatafterhours)
            if key == 'repeatafterminutes':
                repeatafterminutes = match.group('repeatafterminutes')
               # print(repeatafterminutes)
            if key == 'repeatafterseconds':
                repeatafterseconds = match.group('repeatafterseconds')
               # print(repeatafterseconds)
            if key == 'priority':
                priority = match.group('priority')
               # print(priority)

            line=f.readline()

        return evenimente