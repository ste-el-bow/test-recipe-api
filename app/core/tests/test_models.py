from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""
        email = "dup@dup.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
                                                    email=email,
                                                    password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if newly created user has normalized email"""
        email = "dupa@DUPA.com"
        user = get_user_model().objects.create_user(
                                                    email=email,
                                                    password='test123pass')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ if email not provided it should raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                                                email=None,
                                                password='test123pass')

    def test_create_superuser(self):
        """test create superuser"""
        user = get_user_model().objects.create_superuser(
                                                        email="dupa@DUPA.com",
                                                        password='test123pass')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
