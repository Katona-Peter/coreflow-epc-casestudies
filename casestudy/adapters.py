from allauth.account.adapter import DefaultAccountAdapter
from django.contrib import messages

class CustomAccountAdapter(DefaultAccountAdapter):
    def add_message(self, request, level, message_template, message_context=None, extra_tags=''):
        # Clear all previous messages before adding a new login message
        list(messages.get_messages(request))
        super().add_message(request, level, message_template, message_context, extra_tags)
