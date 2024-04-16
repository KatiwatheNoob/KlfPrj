
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactSubmission
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the submission in the database
            submission = form.save(commit=False)
            submission.save()

            # Send the email
            send_contact_email(submission)

            return render(request, 'base/contact.html')  # Render success page
    else:
        form = ContactForm()

    return render(request, 'base/contact.html', {'form': form})

def send_contact_email(submission):
    # Render the email content using the provided HTML template
    email_content = render_to_string('email_template.html', {
        'first_name': submission.first_name,
        'last_name': submission.last_name,
        'email': submission.email,
        'subject': submission.subject,
        'message': submission.message,
        'sent_at': timezone.now().strftime('%d-%m-%Y %H:%M:%S')  # Format the time as needed
    })

    # Create an EmailMultiAlternatives object to support HTML content
    email = EmailMultiAlternatives(
        subject='New Contact Form Submission',
        body='This is a plain text email, please enable HTML to view the message.',  # Plain text alternative
        from_email='mbakaz44@gmail.com',  # Update with your email
        to=['roykatiwa@gmail.com'],  # Update with recipient email
    )

    # Attach the HTML content
    email.attach_alternative(email_content, "text/html")

    # Send the email
    email.send()

# Create your views here.


def home(request):
    return render(request, 'base/home.html')






def about(request):
    return render(request, 'base/about.html')

def faqs(request):
    return render(request, 'base/faqs.html')

def Terms(request):
    return render(request, 'base/t&c.html')

#sevices
def permits(request):
    return render(request, 'services/permits.html')

def passes(request):
    return render(request, 'services/passes.html')

def visas(request):
    return render(request, 'services/visas.html')

def permanentResidency(request):
    return render(request, 'services/permanent-residency.html')

def citizenship(request):
    return render(request, 'services/citizenship.html')

#permits
def classC(request):
    return render(request, 'permits/class-c.html')
def classD(request):
    return render(request, 'permits/class-d.html')
def classG(request):
    return render(request, 'permits/class-g.html')
def classI(request):
    return render(request, 'permits/class-i.html')
def classK(request):
    return render(request, 'permits/class-k.html')
def classM(request):
    return render(request, 'permits/class-m.html')

#passes
def dependantPass(request):
    return render(request, 'passes/dependant-pass.html')
def extensionPass(request):
    return render(request, 'passes/extension-pass.html')
def reEntryPass(request):
    return render(request, 'passes/re-entry-pass.html')
def specialPass(request):
    return render(request, 'passes/special-pass.html')
def studentPass(request):
    return render(request, 'passes/student-pass.html')

#permanet residency
def categoryA(request):
    return render(request, 'permanent-residency/category-a.html')
def categoryB(request):
    return render(request, 'permanent-residency/category-b.html')
def categoryC(request):
    return render(request, 'permanent-residency/category-c.html')
def categoryD(request):
    return render(request, 'permanent-residency/category-d.html')




