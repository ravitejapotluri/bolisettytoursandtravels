from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from manager.Forms import enquiryform
from manager.models import enquiry
from manager.Forms import enquiryform
from manager.models import login
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib


# Create your views here.
def index(request):

        if request.method=="POST":
            form = enquiryform(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.name = request.POST['name']
                f.email = request.POST['email']
                f.mobile = request.POST['number']
                f.destination = request.POST['destination']
                f.date = request.POST['date']

                f.save()
                sendwelcomemessage(request.POST['email'])
                return render(request, 'index.html', {'success': True})
            else:
                return render(request, 'index.html', {'invalid': True})


        return render(request, 'index.html')

def sendwelcomemessage(email):

    try:

        msg = MIMEMultipart()
        msg['From'] = 'goldenpheasant99@gmail.com'
        msg['To'] = email
        msg['Subject'] = "Python email"

        msg.attach(MIMEText('Welcome', 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("goldenpheasant99@gmail.com", "password")
        text = msg.as_string()
        server.sendmail('goldenpheasant99@gmail.com', email, text)
        # msg=MIMEMultipart('mixed')
        # msg['Subject']='Helo'
        # msg['From']='goldenpheasant99@gmail.com'
        # msg['To']=email
        #
        # server=smtplib.SMTP("smtp.gmail.com",587)
        # server.starttls()
        # server.login("goldenpheasant99@gmail.com","password")
        # server.sendmail("goldenpheasant99@gmail.com",email,msg)


    except:
        pass


def domestic(request):

    return render(request,'domestic.html')
def international(request):

    return render(request,'international.html')
def special(request):

    return render(request,'special.html')

def loginfunction(request):
    if (request.method == "POST"):
        try:
            getUser = login.objects.get(email=request.POST['email'])
            pwd = request.POST['password']
            pwd2 = getUser.password
            if(pwd==pwd2):
                result=True
            else:
                result=False
            #result = check_password(pwd, pwd2)
        except:
            return render(request, 'login.html',
                          {'invalidusername': True})
        if (result == True):
            request.session['authenticated']=True
            request.session['email']=request.POST['email']
            return redirect('/showdata/')
        else:
            return render(request, 'login.html',
                          {'invalidpassword': True})

    return render(request,'login.html')

def showdata(request):
    try:

        if(request.session['authenticated']==True):
            data = enquiry.objects.all()

            return render(request,"showdata.html",{'data':data})
        else:
            return render(request, "error.html")
    except:
        return render(request, "error.html")
def logout(request):
    request.session['authenticated'] = False
    return redirect("/login/")