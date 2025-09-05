from custom_nodes.ComfyUi_Random_Manage_Cyan.random_prompt_cyan import RandomPromptCyan
from custom_nodes.ComfyUi_Random_Manage_Cyan.remove_tags_cyan import RemoveTagsCyan

NODE_CLASS_MAPPINGS = {
    "Random Prompt Cyan": RandomPromptCyan,
    "Remove Prompt Cyan": RemoveTagsCyan
}

__all__ = ["NODE_CLASS_MAPPINGS"]
