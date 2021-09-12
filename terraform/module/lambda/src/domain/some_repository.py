import abc
import dataclasses

# Operations to domain object is here.
#
# - All operations must change not only one object but also all objects in aggregates at once.
# - All operations should be simple CRUD operation.
#   If you want to do complex processing, it should be done in specialized other class in domain layer.
#
# In addition, all repositories have abstract class to realize DIP.


class SomeRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def some_crud_operation(self):
        pass


# Objects to be operated by repositories are easier to understand
# if they are in the same file.
@dataclasses.dataclass
class SomeObject:
    id: str
    name: str
    value: str
