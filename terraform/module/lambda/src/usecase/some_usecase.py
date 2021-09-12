import abc

# Behaviors that people can understand should be here.
# Usecases can use a combination of multiple repositories.
#
# In addition, all usecases have abstract class to realize DIP.


class SomeUseCase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass
