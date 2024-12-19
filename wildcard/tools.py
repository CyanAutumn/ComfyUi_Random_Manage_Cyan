import re
from typing import List
from custom_nodes.ComfyUi_Random_Prompt_Cyan.wildcard.base import Base
from custom_nodes.ComfyUi_Random_Prompt_Cyan.wildcard.wildcard_file import WildcardFile
from custom_nodes.ComfyUi_Random_Prompt_Cyan.wildcard.wildcard_folder import WildcardFolder

def parse_prompt_to_wildcards(prompt:str,folder_path:str,file_path:str):
    tags: List[str] = [tag.strip() for tag in prompt.split(',')]
    wildcards:List[Base]=[str(parse_tag_to_wildcarad(tag,folder_path,file_path)) for tag in tags]
    return str.join(" , ",wildcards)
    
def parse_tag_to_wildcarad(tag:str,folder_path:str,file_path:str)->Base:
    match = re.match(r"<.*?>", tag)
    if match:
        _=tag[1:-1]
        if _.startswith("随机提示词"):
            return WildcardFolder(_,folder_path)
        else:
            return WildcardFile(_,file_path)
    else:
        return Base(tag)
