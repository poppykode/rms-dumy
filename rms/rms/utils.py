import random
import string
import datetime
from students.models import Student

def generate_achieve_id(size=20, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    year  = str(datetime.date.today().year)
    tracker_id = 'CUT' + year + the_id +'-ARCHIEVED'
    try:
        Student.objects.get(archieve_id=tracker_id)
        generate_achieve_id()
    except:
        return tracker_id    