from app.models.object import ObjectModel
import re

class ObjectProcessingService:
    def process_object(self, new_object: ObjectModel) -> ObjectModel:
        # Validate email and mobile number
        self.validate_email(new_object.email)
        self.validate_mobile_number(new_object.mobile_number)

        return new_object

    def validate_email(self, email: str) -> None:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format")

    def validate_mobile_number(self, mobile_number: str) -> None:
        if not re.match(r'^\d{8}$', mobile_number):
            raise ValueError("Mobile number must be 8 digits")

def get_object_processing_service():
    return ObjectProcessingService()