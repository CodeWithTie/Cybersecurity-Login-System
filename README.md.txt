# Cybersecurity Login System

A Python-based login and user management system that demonstrates **secure password handling**, **role-based access control**, and **basic cybersecurity principles**.  

This project uses:
- `bcrypt` for password hashing (never storing plain-text passwords)
- `getpass` for hidden password entry
- In-memory user storage with role restrictions (`admin` vs. `user`)

---
## DEMO
![Cybersecurity Login Screenshot](cybersecurity_demo_screenshot.png)

---

## Features
- **User Registration**: Create accounts with secure password hashing  
- **Login System**: Verifies credentials using bcrypt  
- **Role-Based Access**: Admins have their own dashboard with extended functionality  
- **Admin Features**:  
  - View all users  
  - Add a new user  
  - Delete a user (with safety checks: can’t delete self or other admins)  
- **Security Considerations**:  
  - Prevents admins from accidentally removing themselves  
  - Uses hashing instead of storing raw passwords  

---

## Tech Stack
- **Language**: Python  
- **Libraries**: `bcrypt`, `getpass`  

---

## Purpose
This project was built to demonstrate:  
- Secure coding practices (hashing, role-based access control)  
- Awareness of cybersecurity risks in simple applications  
- A foundation for future work in cybersecurity and FinTech  

---

## Future Improvements
Planned enhancements include:  
- Storing users in a database instead of in-memory storage  
- Adding session timeouts & stronger authentication  
- Implementing activity logs for admin oversight  
- Expanding role types beyond just "admin" and "user"  

---

## How to Run
1. Clone the repository:
   ```bash  
   git clone https://github.com/yourusername/cybersecurity-login-system.git
   cd cybersecurity-login-system
2. Install dependencies:
   pip install bcrypt 
3. Run the program

##ABOUT ME
Developed by Tiesha — Business Information Systems student exploring cybersecurity, FinTech, and secure system design.

