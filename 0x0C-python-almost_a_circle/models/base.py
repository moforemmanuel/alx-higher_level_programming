#!/usr/bin/python3
"""models"""
# pylint: disable=invalid-name, redefined-builtin, too-few-public-methods

import json
import csv


class Base:
    """base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        fname = cls.__name__ + ".json"

        data = []
        if list_objs:
            for obj in list_objs:
                data.append(obj.to_dictionary())
        data_str = Base.to_json_string(data)

        with open(fname, 'w', encoding='UTF-8') as json_file:
            return json_file.write(data_str)

    @staticmethod
    def from_json_string(json_string):
        dict_obj = []
        if json_string:
            dict_obj = json.loads(json_string)
        return dict_obj

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 4)
        elif cls.__name__ == 'Square':
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, 'r', encoding='UTF-8') as json_file:
                json_string = json_file.read().replace('\n', '')
                # print(type(json_string)) #str
                dict_objs = cls.from_json_string(json_string)
                # print(type(dict_objs)) #list
                for obj in dict_objs:
                    instances.append(cls.create(**obj))

                # print(instances)

        except FileNotFoundError:
            pass

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        # data = []
        # content = ""
        if list_objs:
            header_key = list(list_objs[0].to_dictionary().keys())
            # print(header_key)
            # print(list_objs)
            dict_objs = list(map(lambda obj: obj.to_dictionary(), list_objs))
            # print(dict_objs)
            with open(filename, 'w', encoding='UTF-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=header_key)
                writer.writeheader()
                return writer.writerows(dict_objs)

                # or
                # for obj in list_objs:
                #     dict_obj = obj.to_dictionary()
                #     csv_row = dict(zip(header_key, dict_obj.values()))
                #     # print(csv_row)
                #     writer.writerow(csv_row)
        return []

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r', encoding='UTF-8') as csv_file:
                reader = csv.DictReader(csv_file)
                # dict_objs = [line for line in reader] better syntax below
                dict_objs = list(reader)
                # print(dict_objs)
            # format the data
            # print(dict_objs)
            # no - dict_objs = list(map(lambda obj: (int(val) for val in obj.keys()), dict_objs))
            # no - print([dict_obj.values() for dict_obj in dict_objs])

            # map values to in, as csv writer rewrote the types
            for obj in dict_objs:
                for key, value in obj.items():
                    try:
                        obj[key] = int(value)
                    except ValueError:
                        obj[key] = float(value)
                    except TypeError:
                        pass
            # print(dict_objs)
            instances = list(map(lambda ob: cls.create(**ob), dict_objs))
            # print(instances)
        except FileNotFoundError:
            pass

        return instances
