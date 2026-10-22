from django.test import TestCase
from django.urls import reverse

from recap_app.models import StudentModel


class StudentCreateViewTests(TestCase):
    def test_get_renders_student_form(self):
        response = self.client.get(reverse('student_create'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Registration Form')

    def test_post_creates_student_and_redirects(self):
        response = self.client.post(
            reverse('student_create'),
            {
                'name': 'Arafat',
                'email': 'arafat@example.com',
                'gender': 'Male',
            },
        )

        self.assertRedirects(response, reverse('student_list'))
        self.assertTrue(
            StudentModel.objects.filter(email='arafat@example.com').exists()
        )

    def test_invalid_post_renders_form_errors(self):
        response = self.client.post(
            reverse('student_create'),
            {'name': 'Arafat', 'email': 'not-an-email'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid email address.')
        self.assertEqual(StudentModel.objects.count(), 0)
