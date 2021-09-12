import abc
import os
from logging import getLogger

from domain.some_repository import SomeRepository

from usecase.some_usecase import SomeUseCase

# Behaviors that people can understand should be here.
# Usecases can use a combination of multiple repositories.
#
# In addition, all usecases have abstract class to realize DIP.


logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))


class SomeUseCaseImpl(SomeUseCase):
    def __init__(self, repository) -> None:
        # Inject repository from outside of usecase to make this class testable.
        self.repository: SomeRepository = repository
        super().__init__()

    def run(self):
        # Do behaviors using some repositories.
        self.repository.some_crud_operation()
        return
