"""Testsuit for user api"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("account:create")
CREATE_TOKEN_URL = reverse("account:token")


def create_user(**params):
    """create and return user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of create user api"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_seccess(self):
        """test create user is successful"""
        payload = {
            "email": "test@example.com",
            "password": "passWord123",
            "name": "name",
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with this email already exists"""
        payload = {
            "email": "test@example.com",
            "password": "passWord123",
            "name": "name",
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password less then 5 characters"""
        payload = {
            "email": "test@example.com",
            "password": "sh",
            "name": "name",
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = (
            get_user_model().objects.filter(email=payload["email"]).exists()
        )
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test if toke is created for user"""
        new_user = {
            "email": "test@example.com",
            "password": "passWord123",
            "name": "name",
        }

        payload = {
            "email": new_user["email"],
            "password": new_user["password"],
        }

        create_user(**new_user)
        res = self.client.post(CREATE_TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("token", res.data)