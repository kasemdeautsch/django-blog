
from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About


class TestAboutView(TestCase):
    """Creates about me content"""

    def setUp(self):
        print('setup:')
        self.about_content = About(
            title='About the prorgr', content='visit me pls.')
        
        self.about_content.save()

    def tearDown(self):
        print('tearDown')

    def test_render_about_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""

        response = self.client.get(reverse('about'))
        
        print('test1')
        self.assertEqual(response.status_code, 200)
        # print('response.status_code----', response.status_code)
        print('test2')
        self.assertIn(b'About the prorgr', response.content)
        # self.assertIn(b'visit me pls', response.content)
        # self.assertIsInstance(
        #     response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        # print('test2')
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        print('test3')
        self.assertEqual(response.status_code, 200)
        print('test4')
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)
