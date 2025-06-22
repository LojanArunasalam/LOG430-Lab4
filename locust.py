import time
from locust import HttpUser, task, between
import random as rand

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def index(self):
        # Simulate a user visiting the home page
        self.client.get("/")

    @task
    def products(self):
        # Simulate a user checking the products api
        self.client.get("/api/v1/products")

    @task
    def stocks(self):
        # Simulate a user checking the stocks api
        store = rand.choice([1, 2, 3, 4, 5])
        self.client.get(f"/api/v1/stocks/store/{store}")

    @task
    def report(self):
        # Simulate a user checking the stocks api
        store = rand.choice([1, 2, 3, 4, 5])
        self.client.get(f"/api/v1/report/{store}")

    @task
    def performances(self):
        # Simulate a user checking the performances api
        self.client.get("/api/v1/performances")

