"""
Advanced example using decorators for autowiring dependencies.
"""

import sys
import os

# Add the parent directory to the path so we can import di_container
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from di_container.container import DIContainer, Scope
from di_container.decorators import injectable, inject
from di_container.exceptions import DIError


# Define some example classes with decorators
@injectable
class EmailService:
    """Email service for sending notifications."""
    def send_email(self, to: str, subject: str, body: str):
        return f"Email sent to {to}: {subject}"


@injectable
class SMSService:
    """SMS service for sending text messages."""
    def send_sms(self, to: str, message: str):
        return f"SMS sent to {to}: {message}"


@injectable
class NotificationService:
    """Notification service that can send emails and SMS."""
    def __init__(self, email_service: EmailService, sms_service: SMSService):
        self.email_service = email_service
        self.sms_service = sms_service
    
    def notify_user(self, user_id: str, message: str):
        email_result = self.email_service.send_email(
            to=f"user{user_id}@example.com",
            subject="Notification",
            body=message
        )
        sms_result = self.sms_service.send_sms(
            to=f"+1234567890",
            message=message
        )
        return f"{email_result}\n{sms_result}"


@inject(email_service=EmailService, sms_service=SMSService)
def create_notification_service(email_service, sms_service):
    """Factory function to create a notification service."""
    return NotificationService(email_service, sms_service)


def main():
    """Run autowire DI example."""
    print("Autowire Dependency Injection Example")
    print("=" * 30)
    
    # Create container
    container = DIContainer()
    
    # Register dependencies
    container.register(EmailService, EmailService, Scope.SINGLETON)
    container.register(SMSService, SMSService, Scope.SINGLETON)
    container.register(NotificationService, create_notification_service, Scope.SINGLETON)
    
    # Resolve dependencies
    try:
        notification_service = container.resolve(NotificationService)
        result = notification_service.notify_user("123", "Hello, World!")
        print(result)
        
    except DIError as e:
        print(f"DI Error: {e}")


if __name__ == "__main__":
    main()