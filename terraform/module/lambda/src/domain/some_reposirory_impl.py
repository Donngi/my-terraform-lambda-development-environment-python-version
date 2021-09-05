import abc
import os
from logging import getLogger

from domain.some_repository import SomeRepository

# Operations to external services here.
# All operations should be simple CRUD operation.
# If you want to do complex processing, it should be done in service layer.
#
# In addition, all repository have abstract class to realize DIP.

logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))


class SomeRepositoryImpl(SomeRepository):
    def __init__(self, some_client) -> None:
        # Inject client from outside of repository to make this class testable.
        # You should specify type of client like
        #   self.dynamodb_client: DynamoDBClient = dynamodb_client
        self.some_client = some_client
        super().__init__()

    def some_crud_operation(self):
        # Operations to external services here
        return
