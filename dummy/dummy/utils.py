import random
import string
import datetime
from django.core.mail import EmailMessage
from accounts.models import User
from students.models import Student


def generate_document_tag_id(size=20, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    year  = str(datetime.date.today().year)
    answer_tracker_id = 'CUT' + year + the_id
    try:
        # AnswerTracker.objects.get(answer_track_id=answer_tracker_id)
        generate_document_tag_id()
    except:
        return answer_tracker_id

def generate_student_number(dig=string.digits, chars =string.ascii_uppercase):
    digits = "".join(random.choice(dig) for x in range(8))
    characters = "".join(random.choice(chars) for x in range(1))
    student_id = 'C' + digits + characters
    try:
        Student.objects.get(student_id_number=student_id)
        generate_student_number()
    except:
        return student_id

def cal_final_mark(quizz_mark,quizz_total,group_mark,group_total,presentation_mark,presentation_total,test_mark,test_total):
    total = int(quizz_total)+int(group_total)+int(presentation_total)+int(test_total)
    total_mark = int(quizz_mark)+int(group_mark)+int(presentation_mark)+int(test_mark)
    final_mark = (total_mark/total) * 30
    return final_mark



def generate_password():
    generated_pass = User.objects.make_random_password()
    return generated_pass

def send_password_and_username(username, email, password):
    print('send_password_and_username')
    try:
        subject = 'Account Creation for Dummy System'
        recipient_list = [email, ]
        email_body = """\
        <html>
        <head> </head>
        <body>
            <h2>New Account Details</h2>
            <p>URL: N/A</p>
            <p>Username: %s</p>
            <p>Password: %s</p>
        </body>
        </html>
        """ % (username, password,)
        mail = EmailMessage(
            subject,
            email_body,
            'cut',
            recipient_list,
        )
        mail.content_subtype = "html"
        mail.send()
    except Exception as e:
        print(e)
