from django.core.validators import RegexValidator

# Ensure the phone number is a valid Egyptian number:
egyptian_phone_validator = RegexValidator(
    regex=r"^(\+20|0)1[0125]\d{8}$",
    message="Phone number must be a valid Egyptian number (e.g., +201XXXXXXXX or 01XXXXXXXX)."
)
