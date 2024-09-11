import csv
import os
from typing import TypeVar, overload

_T = TypeVar("_T")


class FileHandler:
    @staticmethod
    def write_data_csv(file_name,
                       data,
                       field_names):
        file_name = f"{file_name}.csv"
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def append_datas_csv(file_name,
                         data,
                         field_names):
        file_name = f"{file_name}.csv"
        file_exists = os.path.exists(file_name)

        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            if not file_exists or os.path.getsize(file_name) == 0:
                writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def append_data_csv(file_name,
                        data,
                        field_names):
        file_name = f"{file_name}.csv"
        file_exists = os.path.exists(file_name)

        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            if not file_exists or os.path.getsize(file_name) == 0:
                writer.writeheader()
            writer.writerow(data)
