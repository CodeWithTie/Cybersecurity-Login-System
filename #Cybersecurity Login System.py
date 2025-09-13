"""
Cybersecurity Login System
--------------------------
This project demonstrates a secure login system with:
- Password hashing using bcrypt
- Role-based access control (admin vs user)
- Admin dashboard with ability to view, add, and delete users
- Session handling (tracking logged-in user)
This project highlights core cybersecurity principles in authentication and access control.
"""

import bcrypt # - bcrypt libary handles password hashing
import getpass # - lets you enter a password without it showing on screen

#Store users in memory
users = {}

"""
This function - register() -registers a new user in the system. It asks for the
username, role and hidden password. It hashes the password to ensure security.
"""
def register():
    #Ask user to enter username
    user_name = input("Choose a username: ")

    #Ask user to input their role (if their are either an admin or an user)
    role = input("Role (user/admin): ").strip().lower()

    #if not user ot admin, print error message
    if role not in ["user", "admin"]:
        print ("Invalid choice. Please choose user or admin.")
        return

    #Allow user to enter a hidden password
    password = getpass.getpass("Choose a password: ").encode('utf-8')

    #Hash the password securely
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    #Store the new user in memory
    users[user_name] = {"hash": hashed, "role": role}

    #Print sucess message
    print (f"User '{user_name}' registered successfully as {role}. ")

"""
This function - login() - log in a new user in the system by asking for their
username and password. It authenticates to ensure the user the indeed in the system.
If the user is an admin it directs them to the admin menu.
"""
def login():
        
        #Allow user to input username
        user_name = input("Username: ")

        #Check if user exists, and print error message if user is not found
        if user_name not in users:
            print("User not found!")
            return None
        
        #allow user to enter password(hidden) and encode it for bcrypt
        attempt = getpass.getpass("Enter your password: ").encode('utf-8')

        #Check if hashed password entered matches hashed password that is stored
        if bcrypt.checkpw(attempt, users[user_name]["hash"]):
            role = users[user_name]['role']

            #print success confirmation message
            print(f"Login successful! Welcome, {user_name}.")

            #If user's role is an admin, log them into admin dashboard
            if role == "admin":
                 print(f"You now have access to the ADMIN dashboard.")
                 #Return session for admin
                 return (user_name, role)

           #else log user into regular dashboard
            else:
                 print(f"You are logged in as a regular USER.")
                 #Return session for user
                 return (user_name. role)

        else:
            #else, print failure message
            print("Login failed.")
            #Return none due to failed session
            return None

"""
This function - delete_user() - allows the admin to delete a regular user in the system. 
It also has the following security measures:
-Checks if user to be deleted is found in the system
-Prevents admin from deleting themselves
-Prevents admin from deleting another admin
-Confirms if a user is to be deleted
"""
def delete_user(current_admin):

    #Allow admin to input the username they want to delete
    user_name = input("Enter the username to delete: ").strip()

    #Check if user exists
    if user_name not in users:
         print(f"User '{user_name}' not found.")
         return
    
    #Prevent the admin from deleting themselves
    if user_name == current_admin:
         print("Error: You cannot delete your own account.")
         return
    
    #Prevent admin from deleting another admin
    if users[user_name]['role'] == "admin":
         print("You cannot delete another admin account.")
         return
    
    #Delete user confirmation to ensure the correct people is being deleted
    user_confirmation = input(f"Are you sure you want to delete '{user_name}'? yes or no?:  ").lower().strip()

    #if confirmed, delete user and print confirmation message
    if user_confirmation == "yes":
         del users[user_name]
         print(f"User '{user_name}' deleted successfully.")

    #Else, print cancellation message
    else:
         print("This has been cancelled.")



"""
This function - admin_menu(current_admin) - accepts the variable - current_admin as a paramter.
This parameter stores the current admin user currently logged in the program.
This function displays the admin menu with options specifically for the admin to choose from.
"""
def admin_menu(current_admin):
     while True:
          print("--- ADMIN MENU ---")
          print("1. View all users")
          print("2. Add a new user")
          print("3. Delete a user")
          print("4. Logout")

        #Allow user to input their menu choice
          choice = input("Enter your menu choice: ").strip()
          #Ensure user enters a number
          if not choice.isdigit():
               print("Please enter a number.")
               continue

        #if user choice is 1
          if choice == "1":
               #print resgisterd users (usernames & roles)
               print("--- Registered Users ---")
               for u, info in users.items():
                    print(f"-{u} (Role: {info['role'].upper()})")
                    print("="*30)

          elif choice == "2":
                #call the register function
                register() 
          
          elif choice == "3":
                #call the delete user function
                delete_user(current_admin)

          elif choice == "4":
               print("Exiting from ADMIN dashboard...")
               break
          
          else:
               print("Invalid choice. Try again")

          
"""
This function - main_menu - displays the main menu options for users for greater usualbility.
"""
def main_menu():
    #While true, print menu options
    while True:
        print("-----Cybersecurity Login System-----")
        print("1. Register")
        print("2. Login")
        print("3.Exit")

        #Allow user to input their menu choice
        choice = input("Choose your menu choice (1-3): ").strip()

        #Ensure user enters a number
        if not choice.isdigit():
            print("Please enter a number.")
            continue

        # if menu choice - 1 is selected, execute register() method
        if choice == "1":
             register()

        # if menu choice - 2 is selected, execute login() method
        elif choice == "2":
             #execute login function and stores it in session if successful
             session = login()

             #if session is sucessful , store username and role
             if session:
                  user_name, role = session

                  #if role is admin, run admin menu with current admin as a parameter
                  if role == "admin":
                       admin_menu(current_admin = user_name)

                  #else, welcome regular user
                  else:
                       print (f"Welcome, {user_name}! You are now logged in. ")

        # if menu choice - 3 is selected, exit menu
        elif choice == "3":
             print ("Exiting menu ...")
             break
        
        #else, print error message
        else:
             print("Invalid menu choice. Enter 1, 2 or 3")
             
#Run program
main_menu()
