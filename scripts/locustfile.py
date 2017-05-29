from locust import Locust
from locust import TaskSet
from locust import task


class MyTaskSet(TaskSet):

    @task
    def my_task(self):
        print('Locust instance (%r) executing "my_task"'.format(self.locust))


class MyLocust(Locust):
    task_set = MyTaskSet
