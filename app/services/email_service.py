import resend
from app.core.config import settings
from app.utils.template import (
    render_template
)

resend.api_key = settings.RESEND_API_KEY


class EmailService:

    @staticmethod
    async def _send_email(
        to: str,
        subject: str,
        html: str
    ):

        resend.Emails.send(
            {
                "from": settings.EMAIL_FROM,
                "to": [to],
                "subject": subject,
                "html": html
            }
        )

    @staticmethod
    async def send_verification_email(
        email: str,
        name: str,
        verification_url: str
    ):

        html = render_template(
            "verify_email.html",
            name=name,
            verification_url=verification_url
        )

        await EmailService._send_email(
            to=email,
            subject="Verify Your Email",
            html=html
        )