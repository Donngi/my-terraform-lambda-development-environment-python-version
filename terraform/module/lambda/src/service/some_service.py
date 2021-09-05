import abc

# Behaviors that people can understand should be here.
# Services can use a combination of multiple repositories.
#
# In addition, all services have abstract class to realize DIP.


class SomeService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def some_behavior(self):
        pass
