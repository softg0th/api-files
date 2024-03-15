import base64
import logging
import os
import subprocess
from abc import ABC, abstractmethod
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List

from dotenv import load_dotenv

load_dotenv()


class FileManagerTemplate(ABC):
    @abstractmethod
    def __init__(self, pwd):
        self.pwd = pwd

    @abstractmethod
    async def get_all_user_files(self, user):
        pass

    @abstractmethod
    async def upload_user_file(self, user, file):
        pass

    @abstractmethod
    async def delete_user_file(self, user, file):
        pass

    @abstractmethod
    async def rename_user_file(self, user, file, new_file):
        pass

    @abstractmethod
    async def load_user_file(self, user_id, file_name):
        pass


class FileManager(FileManagerTemplate):
    def __init__(self, pwd):
        FileManagerTemplate.__init__(self, pwd)

    async def get_all_user_files(self, user_id) -> List:
        try:
            user_files = os.listdir(f'{self.pwd}/{user_id}')
        except FileNotFoundError:
            return []
        return user_files

    async def upload_user_file(self, user_id, file) -> bool:
        def get_content_after_last_slash(input_string):
            last_slash_index = input_string.rfind('/')
            if last_slash_index != -1:
                content_after_last_slash = input_string[last_slash_index + 1:]
                return content_after_last_slash

        try:
            users = os.listdir(self.pwd)
            user_in_dir = False
            for user in users:
                if user == str(user_id):
                    user_in_dir = True
                    break
            if not user_in_dir:
                subprocess.run(['mkdir', f'{self.pwd}\\{str(user_id)}'], shell=True)
            file.filename = get_content_after_last_slash(file.filename)
            with open(f'{self.pwd}\\{str(user_id)}\\{file.filename}', 'wb') as f:
                f.write(file.file.read())
        except Exception as ex:
            logging.info(f"An error occurred: {ex}")
            return False
        return True

    async def delete_user_file(self, user_id, file) -> bool:
        try:
            os.remove(f'{self.pwd}/{user_id}/{file}')
        except FileNotFoundError:
            return False
        return True

    async def rename_user_file(self, user_id, file_name, new_file_name) -> bool:
        try:
            os.rename(f'{self.pwd}/{user_id}/{file_name}', f'{self.pwd}/{user_id}/{new_file_name}')
        except FileNotFoundError:
            return False
        return True

    async def load_user_file(self, user_id, file_name):
        position = 0
        file_data = None
        for position in range(3):
            try:
                with open(f'{self.pwd}\\{user_id}\\{file_name}.{position}', 'rb') as f:
                    file_data = f.read()
                    file_data = base64.b64encode(file_data).decode('utf-8')
                    break
            except FileNotFoundError:
                pass
        return file_data, position
