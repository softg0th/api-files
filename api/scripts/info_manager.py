import subprocess
import os
from abc import ABC, abstractmethod


class InfoManagerTemplate(ABC):
    @abstractmethod
    def current_left_space(self) -> int:
        pass

    @abstractmethod
    def is_vm(self) -> bool:
        pass


class InfoManager(InfoManagerTemplate):
    def current_left_space(self) -> int:
        space = subprocess.call('df -m /home', shell=True)
        return space

    def is_vm(self) -> bool:
        detector = subprocess.call('systemd-detect-virt', shell=True)
        if detector in ('vbox', 'vmware'):
            return True
        return False
