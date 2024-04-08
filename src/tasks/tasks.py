import smtplib
from email.message import EmailMessage

from celery import Celery
from config import SMTP_USER, SMTP_PASS, REDIS_PORT, REDIS_HOST

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'Здраствуйте {username} а вот и ваш отчет Звцените'
        '<div>'
    )
    return email


@celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
