import os
from logging import getLogger

from infrastructure.some_reposirory_impl import SomeRepositoryImpl
from usecase.some_usecase_impl import SomeUsecaseImpl

from presentation.config import Config

logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))

# Application-specific logics here.
# It is desirable to enumerate behaviors that people can understand.
#
# In addition, this layer sets up all reposirories and usecases.
# Environment variables and config files should be loaded here as well.


def handle_request(event, context):
    param_of_some_client = Config.param_of_some_client
    some_client = init_some_client(param_of_some_client)
    some_repository = SomeRepositoryImpl(some_client)
    some_usecase = SomeUsecaseImpl(repository=some_repository)

    some_usecase.run()

    return
