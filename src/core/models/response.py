from __future__ import annotations
from typing import Generic, TypeVar, List, Union
from pydantic import BaseModel
from src.core.enums.message_type import MESSAGE_TYPE
from src.core.enums.notification_type import NOTIFICATION_TYPE

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    message_type: MESSAGE_TYPE
    notification_type: NOTIFICATION_TYPE
    message: str
    response: Union[T, List[Union[T, None]], None] = None

    @classmethod
    def success(
        cls,
        response: Union[T, List[Union[T, None]], None] = None,
        message: str = "",
        message_type: MESSAGE_TYPE = MESSAGE_TYPE.NONE,
    ) -> Response[T]:
        return cls(
            response=response,
            message=message,
            message_type=message_type,
            notification_type=NOTIFICATION_TYPE.SUCCESS,
        )

    @classmethod
    def success_temporary_message(
        cls,
        response: Union[T, List[Union[T, None]], None] = None,
        message: str = "",
        message_type: MESSAGE_TYPE = MESSAGE_TYPE.TEMPORARY,
    ) -> Response[T]:
        return cls(
            response=response,
            message=message,
            message_type=message_type,
            notification_type=NOTIFICATION_TYPE.SUCCESS,
        )

    @classmethod
    def info(
        cls,
        response: Union[T, List[Union[T, None]], None] = None,
        message: str = "",
        message_type: MESSAGE_TYPE = MESSAGE_TYPE.STATIC,
    ) -> Response[T]:
        return cls(
            response=response,
            message=message,
            message_type=message_type,
            notification_type=NOTIFICATION_TYPE.INFO,
        )

    @classmethod
    def warning(
        cls,
        response: Union[T, List[Union[T, None]], None] = None,
        message: str = "",
        message_type: MESSAGE_TYPE = MESSAGE_TYPE.TEMPORARY,
    ) -> Response[T]:
        return cls(
            response=response,
            message=message,
            message_type=message_type,
            notification_type=NOTIFICATION_TYPE.WARNING,
        )

    @classmethod
    def error(
        cls,
        response: Union[T, List[Union[T, None]], None] = None,
        message: str = "",
        message_type: MESSAGE_TYPE = MESSAGE_TYPE.STATIC,
    ) -> Response[T]:
        return cls(
            response=response,
            message=message,
            message_type=message_type,
            notification_type=NOTIFICATION_TYPE.ERROR,
        )
