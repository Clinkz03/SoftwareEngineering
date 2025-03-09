from django.test import TestCase
from django.urls import reverse
from .models import Category, Customer, Product, Order
from django.contrib.auth.models import User
import time

class FunctionalTests(TestCase):
    def setUp(self):
        # Create categories
        self.category = Category.objects.create(name='T-Shirts')

        # Create a customer
        self.customer = Customer.objects.create(
            first_name='John', last_name='Doe', phone='heyser', password='janjan12345'
        )
        # Create products
        self.product1 = Product.objects.create(
            name='Classic Tee', price=25.00, category=self.category, size='M', description='A comfortable t-shirt.', image='uploads/product/tee.jpg'
        )
        self.product2 = Product.objects.create(
            name='Summer Shirt', price=35.00, category=self.category, size='L', description='A light summer shirt.', image='uploads/product/shirt.jpg'
        )
        # Create a Django user for authentication
        self.user = User.objects.create_user(username='heyser', password='janjan12345')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Classic Tee')
        self.assertContains(response, 'Summer Shirt')

        # Navigation tests
    def test_navigation_home_to_about(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)
            about_page = self.client.get(reverse('about'))
            self.assertEqual(about_page.status_code, 200)

    def test_navigation_home_to_category(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code, 200)
            category_page = self.client.get(reverse('category', args=['T-Shirts']))
            self.assertEqual(category_page.status_code, 200)

    # Performance tests
    def test_home_view_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('home'))
        end_time = time.time()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(end_time - start_time < 0.5, "Home view took too long")

     # Security tests
    def test_unauthorized_access_to_protected_page(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))

    # Usability tests
    def test_error_message_on_invalid_login(self):
            response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'},
                                        follow=True)
            self.assertContains(response, 'Invalid username or password')

    def test_clear_product_descriptions(self):
            response = self.client.get(reverse('product', args=[self.product1.id]))
            self.assertContains(response, 'A comfortable t-shirt.')

