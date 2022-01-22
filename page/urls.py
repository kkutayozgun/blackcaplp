from django.urls import path
from page.views import (Home, handle_contact_form)

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('sendmessage/', handle_contact_form, name="send_message"),
]
