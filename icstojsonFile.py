import jicson


def export_from_ics_to_json():
    # read from file
    result = str(jicson.fromFile('./example.ics'))
    print(result)
    f=open('calendar.json','w')
    f.write(result)
    f.close()
    print("Am scris in fisierul json")



####https://www.vipinajayakumar.com/parsing-text-with-python/
