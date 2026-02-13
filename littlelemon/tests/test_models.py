from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=12.60, inventory=34)
        self.assertEqual(str(item), "Ice Cream : 12.6")