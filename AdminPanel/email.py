from django.core.mail import send_mail

from django.conf import settings



def send_companyremoved_mail(email):
    
    subject='Removed from our system'
    message=(
        f'HELLO, \n'
        f'Sorry to inform you that you have been removed from our system because of as you breached our internal guidlines policies '
        f'\n \n \n \n \n Admin ARS')
    
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True
def send_candidate_removed_mail(email):
    subject='Removed from our system'
    message=(
        f'Dear Candidate,'
        f'Sorry to inform you that you have been removed from our system because of as you breached our internal guidlines policies '
        f'\n \n \n \n \n Admin ARS')
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True
