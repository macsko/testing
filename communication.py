"""Module providing communication via APIs"""
import requests

import backup
from config_struct import EndPoint

class Communication:
    """Class for exchanging data with APIs"""

    def __init__(self, output_endpoint: EndPoint, backup_system: backup.Backup):
        self.output_endpoint = output_endpoint
        self.backup_system = backup_system

    def __send(self, payload):
        """Send specified JSON payload to output_endpoint url"""
        response = requests.post(
            self.output_endpoint.url,
            json=payload,
            headers={"token": self.output_endpoint.token},
            timeout=30,
        )
        response.raise_for_status()

    def send_data(self, payload: dict):
        """Send data to output_endpoint following DataHub interface definition"""
        try:
            self.__send(payload)
        except requests.RequestException as err:
            self.backup_system.create_file(payload)
            print(err)  # Tymczasowo

    def resend_data(self):
        """Resend data stored in backup_system"""
        for filename, payload in self.backup_system.get_files():
            try:
                self.__send(payload)
            except requests.RequestException:
                continue
            finally:
                self.backup_system.delete_file(filename)
