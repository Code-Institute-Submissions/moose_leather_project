from django.test import TestCase
from django.core.management import call_command
from .models import Order, LineItem
from django.conf import settings


class TestOrderModels(TestCase):
    # this method of installing fixtures does not work for me!!
    # fixtures = ['/accounts/fixtures/auth.yaml', '/accounts/fixtures/accounts.yaml']

    @classmethod
    def setUpClass(cls):
        # Be sure to add the call to super!
        super(TestOrderModels, cls).setUpClass()
        settings.USE_TZ = True
        call_command('loaddata', 'auth.yaml', verbosity=0)
        call_command('loaddata', 'accounts.yaml', verbosity=0)


    def test_order_creation(self):
        # You MUST call XXX.objects.create within the test otherwise it tries to use non-test tables
        order = Order.objects.create(name="name", order_info="more stuff", total=50, address1="1234 Main St",
                                     city="San Diego", state="CA", postal_code="11111")
        self.assertTrue(isinstance(order, Order))
        self.assertEqual(order.__str__(), order.name)

    def test_order_string_representation(self):
        order = Order(name='Create an Order')
        self.assertEqual('Create an Order', str(order))

    def test_line_item_string_representation(self):
        order = Order(name='John Doe')
        line_item = LineItem(order=order)
        self.assertEqual(str(line_item), 'John Doe')
