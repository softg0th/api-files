import os
from abc import ABC, abstractmethod
import shutil
from typing import List

from dotenv import load_dotenv

load_dotenv()


class FileManagerTemplate(ABC):
    @abstractmethod
    def __init__(self, pwd):
        self.pwd = pwd

    @abstractmethod
    def get_all_user_files(self, user):
        pass

    @abstractmethod
    def upload_user_file(self, user, file):
        pass

    @abstractmethod
    def delete_user_file(self, user, file):
        pass

    @abstractmethod
    def rename_user_file(self, user, file, new_file):
        pass


class FileManager(FileManagerTemplate):
    def __init__(self, pwd):
        FileManagerTemplate.__init__(self, pwd)

    def get_all_user_files(self, user) -> List:
        user_files = os.listdir(f'{self.pwd}/{user}')
        return user_files

    def upload_user_file(self, user, file) -> bool:
        try:
            shutil.move(file, f'{self.pwd}/{user}')
        except Exception:
            return False
        return True

    def delete_user_file(self, user, file) -> bool:
        try:
            os.remove(f'{self.pwd}/{user}/{file}')
        except Exception:
            return False
        return True

    def rename_user_file(self, user, file, new_file) -> bool:
        try:
            extension = os.path.splitext(file)[1]
            os.rename(file, f'{new_file}{extension}')
        except Exception:
            return False
        return True

