from django.shortcuts import render, redirect
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
from django.contrib import messages
from email.mime.multipart import MIMEMultipart
import smtplib, ssl, getpass
from . models import viewer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send_newsletter(receiver_email):
        sender_email = "inforehubdeveloper@gmail.com"
        password = 'yobmydltqhklduch'
        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Authentication Token"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = f"Hi,\n\nYour token is: token\n\nBest regards,\nKingsley"
        html = f"""\
        <html>
        <head>
            <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 16px;
                line-height: 1.4;
                color: #333;
                background-color: #f2f2f2;
                margin: 0;
                padding: 0;
            }}
            h1 {{
                font-size: 24px;
                margin-top: 20px;
                margin-bottom: 10px;
                text_allign: center;
            }}
            p {{
                margin: 0 0 10px;
            }}
            b {{
                color: #007bff;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}
            </style>
        </head>
        <body>
            <div class="container">
            <h1>Thank you for suscribing to our newsletter</h1>
            <p>We will make sure to frequently update you on exciting changes and innovative ideas</b></p>
            <p>Best regards,<br>RehubDevelopers</p>
            </div>
        </body>
        </html>
        """
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())



# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('send_nwls') == 'submit':
            email = request.POST.get('email')
            try:
                existing_viewer = viewer.objects.filter(email=email)
                if existing_viewer.exists():
                    messages.error(request, 'You have already subscribed to our newsletter')
                else:
                    send_newsletter(email)
                    viewer.objects.get_or_create(email=email)
                    messages.success(request, f'{email} has successfully registered to the newsletter')
            except Exception:
                messages.error(request, 'Something went wrong. Please try again.')
            print(request.POST.get('email'))
        # Set a session variable to indicate that the modal has been closed
        request.session['modal_closed'] = True
    return render(request, 'app/index.html')

def about_us(request):
    if request.method == 'POST':
        if request.POST.get('send_nwls') == 'submit':
            email = request.POST.get('email')
            try:
                existing_viewer = viewer.objects.filter(email=email)
                if existing_viewer.exists():
                    messages.error(request, 'You have already subscribed to our newsletter')
                else:
                    send_newsletter(email)
                    viewer.objects.get_or_create(email=email)
                    messages.success(request, f'{email} has successfully registered to the newsletter')
            except Exception:
                messages.error(request, 'Something went wrong. Please try again.')
            print(request.POST.get('email'))
        # Set a session variable to indicate that the modal has been closed
        request.session['modal_closed'] = True
    return render(request, 'app/about-us.html')

def services(request):
    if request.method == 'POST':
        if request.POST.get('send_nwls') == 'submit':
            email = request.POST.get('email')
            try:
                existing_viewer = viewer.objects.filter(email=email)
                if existing_viewer.exists():
                    messages.error(request, 'You have already subscribed to our newsletter')
                else:
                    send_newsletter(email)
                    viewer.objects.get_or_create(email=email)
                    messages.success(request, f'{email} has successfully registered to the newsletter')
            except Exception:
                messages.error(request, 'Something went wrong. Please try again.')
            print(request.POST.get('email'))
        # Set a session variable to indicate that the modal has been closed
        request.session['modal_closed'] = True
    return render(request, 'app/services.html')

def projects(request):
    if request.method == 'POST':
        if request.POST.get('send_nwls') == 'submit':
            email = request.POST.get('email')
            try:
                existing_viewer = viewer.objects.filter(email=email)
                if existing_viewer.exists():
                    messages.error(request,'you have already suscribed to our newsletter')
                else: 
                    send_newsletter(email)
                    viewer.objects.get_or_create(email=email)
                    messages.success(request,f'{email} has successfully registerd to newsletter')
            except Exception:
                messages.error(request,'Something went wrong try again')
            print(request.POST.get('email'))
    return render(request, 'app/projects.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        country = request.POST.get('country')
        email_con = request.POST.get('email_con')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if request.POST.get('send_nwls') == 'submit':
            
            try:
                existing_viewer = viewer.objects.filter(email=email)
                if existing_viewer.exists():
                    messages.error(request, 'You have already subscribed to our newsletter')
                else:
                    send_newsletter(email)
                    viewer.objects.get_or_create(email=email)
                    messages.success(request, f'{email} has successfully registered to the newsletter')
            except Exception:
                messages.error(request, 'Something went wrong. Please try again.')
            print(request.POST.get('email'))
        # Set a session variable to indicate that the modal has been closed
        request.session['modal_closed'] = True
        subject = f"Contact Form Submission from {name}"
        message = f"Name: {name}\nCountry/State: {country}\nEmail: {email_con}\nPhone: {phone}\nMessage: {message}"
        send_mail(subject, message, email_con, [settings.CONTACT_EMAIL])
    return render(request, 'app/contact.html')

    