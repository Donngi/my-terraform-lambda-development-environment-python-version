import abc
import os
from logging import getLogger

from domain.some_repository import SomeRepository

from service.some_service import SomeService

# Behaviors that people can understand should be here.
# Services can use a combination of multiple repositories.
#
# In addition, all services have abstract class to realize DIP.


logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))


class SomeServiceImpl(SomeService):
    def __init__(self, repository) -> None:
        # Inject repository from outside of service to make this class testable.
        self.repository: SomeRepository = repository
        super().__init__()

    def some_behavior(self):
        # Do behaviors using some repositories.
        self.repository.some_crud_operation()
        return
