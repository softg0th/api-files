from abc import ABC, abstractmethod


class FileManagerTemplate(ABC):
    @abstractmethod
    def get_all_user_files(self, user):
        pass

    @abstractmethod
    def upload_user_file(self, user, file):
        pass

    @abstractmethod
    def delete_user_file(self, user, file):
        pass


class FileManager(FileManagerTemplate):
    def get_all_user_files(self, user):
        pass

    def upload_user_file(self, user, file):
        pass

    def delete_user_file(self, user, file):
        pass

