from .drone import Drone
from .http import create_session
from .users import Drone as Users


class Client:
    def __init__(self, user, repo):
        self.owner = user
        self.repository = repo
        self._session = create_session()

    @property
    def user(self):
        return Users.User()

    @property
    def users(self):
        return Users.Users()

    @property
    def secrets(self):
        return Users.Secrets(self.owner, self.repository)

    @property
    def build(self):
        return Drone.Build(self.owner, self.repository, session=self._session)

    @property
    def cron(self):
        return Drone.Cron(self.owner, self.repository, session=self._session)

    @property
    def repos(self):
        return Drone.Repo(self.owner, self.repository, session=self._session)


def drone(user, repo):
    return Client(user, repo)
