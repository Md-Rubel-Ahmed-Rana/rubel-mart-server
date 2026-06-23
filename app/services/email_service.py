import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings
from datetime import datetime 
from app.services.template_service import ( TemplateService )

class EmailService:

    @staticmethod
    async def _send_email(
        to: str,
        subject: str,
        html: str
    ):
        message = MIMEMultipart()

        message["From"] = settings.EMAIL_FROM
        message["To"] = to
        message["Subject"] = subject

        message.attach(
            MIMEText(
                html,
                "html"
            )
        )

        print("HOST:", settings.EMAIL_HOST)
        print("PORT:", settings.EMAIL_PORT)

        socket.create_connection(
            (
                settings.EMAIL_HOST,
                int(settings.EMAIL_PORT)
            ),
            timeout=10
        )

        print("SMTP Reachable")

        with smtplib.SMTP(
            settings.EMAIL_HOST,
            settings.EMAIL_PORT
        ) as server:

            server.starttls()

            server.login(
                settings.EMAIL_USER,
                settings.EMAIL_PASSWORD
            )

            server.send_message(
                message
            )


    @staticmethod
    async def send_verification_email(
        email: str,
        name: str,
    ):
        
        html = TemplateService.render( 
            "emails/auth/verification.html", 
            { 
                "title": "Account Verification", 
                "name": name, 
                "otp": "123456", 
                "year": datetime.now().year, 
                "logo_url": "https://res.cloudinary.com/dv2ocmcyo/image/upload/v1782229601/rubel-mart-logo_ihlhjn.png", 
                "support_email": "mdrubelahmedrana521@gmail.com", 
            } 
        )

        await EmailService._send_email(
            to=email,
            subject="Verify Your Email",
            html=html
        )