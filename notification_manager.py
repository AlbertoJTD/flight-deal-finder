import smtplib

EMAIL = "HERE_GOES_YOUR_EMAIL"
PASSWORD_APP = "HERE_GOES_YOUR_PASSWORD_APP_FROM_GMAIL"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD_APP

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=self.email,
                                msg=f"Subject:Low price alert\n\n{message}")
