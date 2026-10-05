# Method Overriding

class Notification:
    def send(self):
        return "Preparing message to send to receipient:"


class EmailNotification(Notification):
    def send(self):
        return "Send Information to receipient in email"


class SmsNotification(Notification):
    def send(self):
        return "Send Information to receipient in sms"


email_notifiction = EmailNotification()
sms_notification = SmsNotification()
print(email_notifiction.send())
print(sms_notification.send())

# for email_notifiction and sms_notification overrided send() method in subclass is called
# Reason - we are calling with subclass object
