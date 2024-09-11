from collections.abc import Iterable
from typing import Any, TypeVar, overload, Mapping

_T = TypeVar("_T")


class FileHandler:
    @staticmethod
    def write_data_csv(file_name: str,
                       data: list,
                       field_names: list): ...

    @staticmethod
    def append_datas_csv(file_name: str,
                         data: Iterable[Mapping[_T, Any]],
                         field_names: list): ...

    @staticmethod
    def append_data_csv(file_name: str,
                        data: Mapping[_T, Any],
                        field_names: list): ...
