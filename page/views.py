from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"


def handle_contact_form(request):
    sender = settings.DEFAULT_FROM_EMAIL
    receivers = settings.CONTACT_FORM_RECEIVER
    if request.method == 'POST':
        try:
            full_name = request.POST.get('full_name', default="")
            treatment_choice = request.POST.get('treatment-choice', default="")
            email = request.POST.get('email', default="")
            phone = request.POST.get('phone', default="")
            contact_method = request.POST.get('contact-method', default="")

            email_template = get_template('emailtemps/contact_email_template.html')
            subject = f"Black Cap {full_name} tarafından iletişim formu dolduruldu"

            context = {
                'full_name': full_name,
                'treatment_choice': treatment_choice,
                'email': email,
                'phone': phone,
                'contact_method': contact_method,
            }

            content = email_template.render(context)
            msg = EmailMultiAlternatives(subject, "", sender, receivers)
            msg.attach_alternative(content, 'text/html')
            msg.send()
        except Exception as e:
            print(e)
            messages.error(request, "Mesajınız gönderilirken hata oluştu!")
        else:
            messages.success(request, "Mesajınız başarıyla gönderildi! Size en kısa sürede geri dönüş yapacağız.")

        return redirect(request.META['HTTP_REFERER'] + "#contact_form")
