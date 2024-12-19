import random
from custom_nodes.ComfyUi_Random_Prompt_Cyan import random_prompt_cyan
from custom_nodes.ComfyUi_Random_Prompt_Cyan.wildcard.base import Base

class WildcardFile(Base):
    buf_text:str
    file_name:str
    file_path:str

    def __init__(self,tag,file_path):
        _=tag.split(":")
        self.file_name=_[0]
        self.file_path=file_path

    def __str__(self):
        file_path = f"{self.file_path}\{self.file_name}.txt"
        with open(file_path, 'r') as file:
            lines = file.readlines()
        random_line = random.choice(lines)
        return random_line