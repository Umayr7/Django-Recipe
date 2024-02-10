"""
Passowrd Policy Validation
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PasswordPolicyValidator:
    """Password Policy Valdiator"""
    """
        minimun 8 characters
        at least one uppercase letter
        at least one lowercase letter
        at least one special character
        at least three digit
    """

    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _('Password must be at least {0} \
                  characters long').format(self.min_length),
                code='password_too_short',
            )

        if not any(char.isupper() for char in password):
            raise ValidationError(
                _('Password must contain at least one uppercase letter'),
                code='password_no_upper',
            )

        if not any(char.islower() for char in password):
            raise ValidationError(
                _('Password must contain at least one lowercase letter'),
                code='password_no_lower',
            )

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(
                _('Password must contain at least one special character'),
                code='password_no_special',
            )

        if sum(char.isdigit() for char in password) < 3:
            raise ValidationError(
                _('Password must contain at least three digits'),
                code='password_insufficient_digits',
            )

    def get_help_text(self):
        return _(
            "Your password must be at least {} characters long and \
                include at least 1 uppercase letter, 1 lowercase letter, \
                    1 special character, and 3 numeric \
                        characters.".format(self.min_length)
        )
