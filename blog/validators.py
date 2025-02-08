from django.core.validators import RegexValidator

#Validtor to check if the phone number is egyptian or not:
egyptian_phone_validator = RegexValidator(
    regex=r"^(\+20|0)?1[0125]\d{8}$",
    message="Phone number must be a valid Egyptian number (e.g., +201XXXXXXXX or 01XXXXXXXX)."
)