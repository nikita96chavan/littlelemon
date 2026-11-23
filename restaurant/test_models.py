from django.test import TestCase
from .models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_booking(self):
        booking = Booking.objects.create(Name="Test", No_of_guests=2, BookingDate="2024-01-01")
        self.assertEqual(str(booking), "Test")
