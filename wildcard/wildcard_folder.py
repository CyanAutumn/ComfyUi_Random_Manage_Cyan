import os
import random
from custom_nodes.ComfyUi_Random_Manage_Cyan import random_prompt_cyan
from custom_nodes.ComfyUi_Random_Manage_Cyan.wildcard.base import Base

class WildcardFolder(Base):
    folder_path:str

    def __init__(self,tag,folder_path):
        self.folder_path=folder_path
        pass

    def __str__(self):
        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        random_file = random.choice(files)
        file_path = os.path.join(self.folder_path, random_file)
        with open(file_path, 'r') as file:
            content = file.read()
        return content