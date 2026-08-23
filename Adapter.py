from abc import ABC,abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send(to,title,body):
        pass
class NotificationClass(NotificationService):
    def send(self,to,title,body):
        print("Sending Email by Notification")
        print(f"To: {to}")
        print(f"Title: {title}")
        print(f"Body: {body}")
class GridEmailSender:
    def send_email(self,context,reciptient,subject):
        print("Sending email by Grid Email Sender")
        print(f"Recieptient: {reciptient}")
        print(f"Subject: {subject}")
        print(f"Context: {context}")


class GridSenderApadpter(NotificationService):
    def __init__(self,gridemailsenderobj: GridEmailSender):
        self.__gridemailsend=gridemailsenderobj
    def send(self,to,title,body):
        self.__gridemailsend.send_email(body,to,title)
gridemailsenderobj=GridEmailSender()
adp=GridSenderApadpter(gridemailsenderobj)
adp.send("abc2gmail.com","Application for Python Developer Position","I am interested in the Python Developer position and would appreciate the opportunity to discuss how my experience aligns with the role.")
NotificationClass().send("abc2gmail.com","Application for Python Developer Position","I am interested in the Python Developer position and would appreciate the opportunity to discuss how my experience aligns with the role.")
