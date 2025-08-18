import json
import os
import hashlib
from datetime import datetime

class UserManagementSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.current_user = None
        self.users = self.load_users()
    
    def load_users(self):
        """Load existing users from JSON file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as file:
                    return json.load(file)
            except:
                return {}
        return {}
    
    def save_users(self):
        """Save users to JSON file"""
        with open(self.users_file, 'w') as file:
            json.dump(self.users, file, indent=4)
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, email, password, confirm_password):
        """Register a new user"""
        # Validation checks
        if not username or not email or not password:
            return False, "All fields are required"
        
        if username in self.users:
            return False, "Username already exists"
        
        if password != confirm_password:
            return False, "Passwords do not match"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters long"
        
        # Create new user
        user_id = str(len(self.users) + 1)
        hashed_password = self.hash_password(password)
        
        new_user = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "password": hashed_password,
            "created_at": datetime.now().isoformat(),
            "last_login": None
        }
        
        self.users[username] = new_user
        self.save_users()
        
        return True, f"User '{username}' registered successfully!"
    
    def login_user(self, username, password):
        """Login user with username and password"""
        if not username or not password:
            return False, "Username and password are required"
        
        if username not in self.users:
            return False, "Invalid username or password"
        
        user = self.users[username]
        hashed_password = self.hash_password(password)
        
        if user['password'] != hashed_password:
            return False, "Invalid username or password"
        
        # Update last login
        user['last_login'] = datetime.now().isoformat()
        self.save_users()
        
        # Set current user
        self.current_user = user
        
        return True, f"Welcome back, {username}!"
    
    def logout_user(self):
        """Logout current user"""
        if self.current_user:
            username = self.current_user['username']
            self.current_user = None
            return True, f"Logged out successfully, {username}!"
        return False, "No user is currently logged in"
    
    def get_user_profile(self):
        """Get current user's profile information"""
        if not self.current_user:
            return False, "No user is currently logged in"
        
        profile = self.current_user.copy()
        del profile['password']  # Don't show password
        return True, profile

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("           USER MANAGEMENT SYSTEM")
    print("="*50)
    
    if not user_system.current_user:
        print("1. Register User")
        print("2. Login User")
        print("3. Exit")
    else:
        print(f"Welcome, {user_system.current_user['username']}!")
        print("1. View Profile")
        print("2. Logout")
        print("3. Exit")
    
    print("="*50)

def register_menu():
    """Handle user registration"""
    print("\n--- USER REGISTRATION ---")
    
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()
    confirm_password = input("Confirm password: ").strip()
    
    success, message = user_system.register_user(username, email, password, confirm_password)
    print(f"\n{'✓' if success else '✗'} {message}")

def login_menu():
    """Handle user login"""
    print("\n--- USER LOGIN ---")
    
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    success, message = user_system.login_user(username, password)
    print(f"\n{'✓' if success else '✗'} {message}")

def main():
    """Main program loop"""
    global user_system
    user_system = UserManagementSystem()
    
    print("Welcome to User Management System!")
    
    while True:
        display_menu()
        
        if not user_system.current_user:
            # Not logged in
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                register_menu()
            elif choice == '2':
                login_menu()
            elif choice == '3':
                print("Thank you for using User Management System!")
                break
            else:
                print("Invalid choice! Please select 1-3.")
        
        else:
            # Logged in
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                success, result = user_system.get_user_profile()
                if success:
                    print("\n--- USER PROFILE ---")
                    for key, value in result.items():
                        print(f"{key.replace('_', ' ').title()}: {value}")
                else:
                    print(f"✗ {result}")
            
            elif choice == '2':
                success, message = user_system.logout_user()
                print(f"✓ {message}")
            
            elif choice == '3':
                print("Thank you for using User Management System!")
                break
            
            else:
                print("Invalid choice! Please select 1-3.")

if __name__ == "__main__":
    main()
