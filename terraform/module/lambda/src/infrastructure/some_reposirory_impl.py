import abc
import os
from logging import getLogger

from domain.some_repository import SomeObject, SomeRepository

# Operations to domain object is here.
#
# - All operations must change not only one object but also all objects in aggregates at once.
# - All operations should be simple CRUD operation.
#   If you want to do complex processing, it should be done in specialized other class in domain layer.
#
# In addition, all repositories have abstract class to realize DIP.

logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))


class SomeRepositoryImpl(SomeRepository):
    def __init__(self, some_client: SomeClient) -> None:
        # Inject client from outside of repository to make this class testable.
        # You should specify type of client like
        #   self.dynamodb_client: DynamoDBClient = dynamodb_client
        self.some_client: SomeClient = some_client
        super().__init__()

    def some_crud_operation(self):
        new_object = SomeObject()
        # An operation to domain objects is here
        return
