from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .views import *
from .models import user_lists

# Create your tests here.
class TestSimpleApp(TestCase):
	def test_one(self):
		x = "my simple app test"
		assert 'simple app' in x

class userTests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create(username='testAccout', email='mail@mail.com', password='password123')

	def test_createList(self):
		 # Create an instance of a POST request and prepare data to send
		data = {'list_name':'test_list'}
		request = self.factory.post('/create_list/', data)

		# logged-in user by setting request.user manually.
		request.user = self.user

		# Test createlist() as if it were deployed at
		response = create_list(request)
		confirm_list = user_lists.objects.get(list_name='test_list', list_owner=self.user)

		self.assertEqual(response.status_code, 200)
		self.assertEqual('test_list', confirm_list.list_name)

class homeTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()

	def test_home(self):
		request = self.factory.get('/')
		response = home_view(request)
		self.assertEqual(response.status_code, 200)

class search_test(TestCase):
	def setUp(self):
		self.factory = RequestFactory()

	def test_search(self):
		 # Create an instance of a POST request and prepare data to send
		data = {'term':'tofu'}
		request = self.factory.post('/search/', data)

		# Test search() as if it were deployed at
		response = search(request)
	
		self.assertEqual(response.status_code, 200)
