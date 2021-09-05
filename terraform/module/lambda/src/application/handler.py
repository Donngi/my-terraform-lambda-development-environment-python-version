import os
from logging import getLogger

from domain.some_reposirory_impl import SomeRepositoryImpl
from service.some_service_impl import SomeServiceImpl

logger = getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "WARNING"))


def handler_request(event, context):
    # Application-specific logics here.
    # It is desirable to enumerate behaviors that people can understand.
    #
    # In addition, this layer sets up all reposirories and services.
    # Environment variables and config files should be loaded here as well.
    some_client = init_some_client()
    some_repository = SomeRepositoryImpl(some_client)
    some_service = SomeServiceImpl(repository=some_repository)

    some_service.some_behavior()

    return
