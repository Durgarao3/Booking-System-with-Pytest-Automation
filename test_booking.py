# test_booking.py

import pytest
from booking import BookingSystem

@pytest.fixture
def booking_system():
    return BookingSystem()

def test_successful_booking(booking_system):
    assert booking_system.book("Alice", "10AM") is True
    assert ("Alice", "10AM") in booking_system.list_bookings()

def test_duplicate_booking(booking_system):
    booking_system.book("Alice", "10AM")
    with pytest.raises(ValueError, match="Slot already booked"):
        booking_system.book("Bob", "10AM")

def test_cancel_booking(booking_system):
    booking_system.book("Alice", "10AM")
    assert booking_system.cancel("Alice", "10AM") is True
    assert ("Alice", "10AM") not in booking_system.list_bookings()

def test_cancel_nonexistent_booking(booking_system):
    with pytest.raises(ValueError, match="No such booking found"):
        booking_system.cancel("Bob", "9AM")

def test_slot_availability(booking_system):
    assert booking_system.is_slot_available("10AM") is True
    booking_system.book("Alice", "10AM")
    assert booking_system.is_slot_available("10AM") is False
