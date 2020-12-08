import locust


class MyTaskSet(locust.TaskSet):
    @locust.task
    def my_task(self):
        print('Locust instance ({}) executing "my_task"'.format(self.user))


class MyUser(locust.User):
    tasks = [MyTaskSet]
