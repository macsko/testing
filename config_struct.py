"""module containing classes for handling configuration of device"""

import json


class ConfError(Exception):
    def __init__(self, message: str = ""):
        self.message = message


class DeviceConfig:
    """structure holding device configuration data"""

    def __init__(self, name: str = "", file: str = "", cls: str = "", arg: dict = None):
        self.device_name: str = name
        self.src_file_name: str = file
        self.class_name: str = cls
        self.args: dict = arg

    def get_from_dict(self, s: dict):
        """read data from dict and set object attributes"""
        for key, value in s.items():
            self.__setattr__(key, value)
        return self


class EndPoint:
    """structure holding endpoint data"""

    def __init__(self, url: str = "", token: str = ""):
        self.url = url
        self.token = token

    def get_from_dict(self, s: dict):
        """read data from dict and set object attributes"""
        for key, value in s.items():
            self.__setattr__(key, value)
        return self


class Configuration:
    """structure holding all configuration data"""

    def __init__(self):
        self.stationName: str = ""
        self.id: str = ""
        self.location: dict = dict()
        self.networkIf: str = ""
        self.verbosity: int = 0
        self.measureDevices: list[DeviceConfig] = []
        self.measureFrequency: int = 0
        self.endpointData: EndPoint = None
        self.endpointCom: EndPoint = None

    def get_station_data(self) -> dict:
        d = dict()
        for name in ["stationName", "id", "location", "networkIf", "verbosity"]:
            d[name] = self.__getattribute__(name)
        return d

    def get_from_json(self, json_name: str):
        """method reading configuration from json file"""
        f = open("config_files/" + json_name)
        conf_data: str = f.read()
        f.close()
        r = json.loads(conf_data)
        for key, value in r.items():
            self.__setattr__(key, value)

        tmp = EndPoint()
        self.endpointData = tmp.get_from_dict(self.endpointData)
        tmp = EndPoint()
        self.endpointCom = tmp.get_from_dict(self.endpointCom)

        for i in range(len(self.measureDevices)):
            tmp = DeviceConfig()
            self.measureDevices[i] = tmp.get_from_dict(self.measureDevices[i])
