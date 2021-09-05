import abc

# Operations to external services here.
# All operations should be simple CRUD operation.
# If you want to do complex processing, it should be done in service layer.
#
# In addition, all repositories have abstract class to realize DIP.


class SomeRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def some_crud_operation(self):
        pass
