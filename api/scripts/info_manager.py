import subprocess
import os
from abc import ABC, abstractmethod


class InfoManagerTemplate(ABC):
    @abstractmethod
    async def current_left_space(self) -> int:
        pass

    @abstractmethod
    async def is_vm(self) -> bool:
        pass


class InfoManager(InfoManagerTemplate):
    async def current_left_space(self) -> int:
        space = subprocess.call('df -m /home', shell=True)
        return space

    async def is_vm(self) -> bool:
        detector = subprocess.call('systemd-detect-virt', shell=True)
        if detector in ('vbox', 'vmware'):
            return True
        return False
