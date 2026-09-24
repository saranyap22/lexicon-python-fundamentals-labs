# Polymorphism

class Notification:
    def send(self):
        return "Message successfully constructed "


class EmailNotification:
    def send(self):
        return "Email sent successfully to receipient"


class SmsNotification:
    def send(self):
        return "Sms sent successfully to receipient"


notifications = [
    Notification(),
    EmailNotification(),
    SmsNotification()
]

for notification in notifications:
    print(notification.send())

# While looping through objects the send() method from corresponding classes called automatically
# Note here we have not used inheritence
