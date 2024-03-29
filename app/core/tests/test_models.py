"""
Tests for Schema Models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'Testpass@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['test2@EXAMPLE.COM', 'test2@example.com'],
            ['test3@EXAMPLE.COM', 'test3@example.com'],
            ['test4@EXAMPLE.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'Testpass@123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user with no email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Testpass@123')

    def test_create_superiser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'Testpass@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
