from locust import HttpLocust, TaskSet, task, between
import json

base_url = "http://localhost:8000"

class UserActions(TaskSet):
    cookies = {}

    def on_start(self):
        self.login()

    def login(self):
        # login to the application
        resp = self.client.post(base_url+'/api/users/login/',
                         {'email': 'user1@example.com', 'password': 'Test@123'})
        self.cookies['x-access-token'] = json.loads(resp.content)["data"]["token"]
    
    @task(1)
    def index(self):
        self.client.get(base_url+'/api/users/details/', cookies=self.cookies)
    
    for i in range(1):
        @task(2)
        def index1(self):
            self.client.get(base_url+'/api/feeds/', cookies=self.cookies)
    
    for i in range(1):
        @task(3)
        def index2(self):
            self.client.get(base_url+'/api/feeds/1', cookies=self.cookies)

class ApplicationUser(HttpLocust):
    task_set = UserActions
    wait_time = between(1, 4)
    min_wait = 0
    max_wait = 0