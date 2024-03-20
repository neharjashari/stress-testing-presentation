from locust import HttpUser, SequentialTaskSet, task, between
import json
import random
import string

class UserBehavior(SequentialTaskSet):
    def generate_random_string(self, length=10):
        """Generate a random string of fixed length."""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))

    def on_start(self):
        """Generate random credentials for the user."""
        self.email = f"{self.generate_random_string()}@example.com"
        self.password = self.generate_random_string()

    @task
    def register(self):
        """Register a new user."""
        response = self.client.post("/api/register", json={
            "name": self.generate_random_string(),
            "email": self.email,
            "password": self.password,
        })
        print("Registered with:", self.email, self.password)

    @task
    def login(self):
        """Log in as the newly registered user."""
        response = self.client.post("/api/login", json={
            "email": self.email,
            "password": self.password
        })
        result = response.json()
        self.token = result["authorization"]["access_token"]
        print("Logged in with:", self.email)

    @task
    def get_user_info(self):
        """Get the current user's information."""
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/api/me", headers=headers)
        print("Fetched user info for:", self.email)

    @task
    def logout(self):
        """Log out the current user."""
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.post("/api/logout", headers=headers)
        print("Logged out:", self.email)

    def on_stop(self):
        """Any cleanup actions if necessary."""
        pass

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
