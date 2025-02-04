
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutView(TestCase):
    """Creates about me content"""

    def setUp(self):
        self.about_content = About(
            title='About the prorgr', content='visit me pls.')
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About the prorgr', response.content)
        self.assertIn(b'visit me pls', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaborate_submission(self):

        post_data = {
            'name': 'hart',
            'email': 'hart@test.com',
            'message': 'Hallo, ich bin da.'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days',
                      response.content)
