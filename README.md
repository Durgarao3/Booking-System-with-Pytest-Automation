# Booking-System-with-Pytest-Automation

# 🧪 Booking System - Automation Testing with Pytest

This project demonstrates a simple **Booking System** built in Python, with a complete suite of **automated tests** written using **Pytest**.

📍 GitHub Repo: [Booking-System-with-Pytest-Automation](https://github.com/Durgarao3/Booking-System-with-Pytest-Automation)

---

## 🚀 Features

- Book slots with a name and time
- Prevent duplicate slot bookings
- Cancel existing bookings
- Raise appropriate errors for invalid actions
- Fully tested using Pytest

---

## 🛠️ Tech Stack

- Python 3.x
- Pytest
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

booking_system/
│
├── booking.py # Main BookingSystem class
├── test_booking.py # Pytest test cases
├── README.md # Project documentation


---

## 🧪 Sample Test Cases

```python
def test_duplicate_booking(booking_system):
    booking_system.book("Alice", "10AM")
    with pytest.raises(ValueError, match="Slot already booked"):
        booking_system.book("Bob", "10AM")

## 🚀 How to Run

1.Clone Resporitory
git clone https://github.com/Durgarao3/Booking-System-with-Pytest-Automation.git
cd Booking-System-with-Pytest-Automation


2.Install dependencies:
pip install pytest

3.Run the tests:
pytest test_filename.py
