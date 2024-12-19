from comfy.comfy_types import IO, ComfyNodeABC, InputTypeDict
from custom_nodes.ComfyUi_Random_Prompt_Cyan.wildcard import tools, wildcard_file


class RandomPromptCyan:
    @classmethod
    def INPUT_TYPES(s) -> InputTypeDict:
        return {
            "required": {
                "input_prompt_1": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "dynamicPrompts": True,
                        "tooltip": "The text to be encoded.",
                    },
                ),
                "input_prompt_2": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "dynamicPrompts": True,
                        "tooltip": "The text to be encoded.",
                    },
                ),
                "folder_path": (
                    IO.STRING,
                    {
                        "multiline": False,
                        "default": "Wildcard按文件抽取路径",
                        "tooltip": "wildcard folder",
                    },
                ),
                "file_path": (
                    IO.STRING,
                    {
                        "multiline": False,
                        "default": "Wildcard按行抽取路径",
                        "tooltip": "wildcard file",
                    },
                ),
            },
        }

    RETURN_TYPES = (IO.STRING,)
    OUTPUT_TOOLTIPS = (
        "A conditioning containing the embedded text used to guide the diffusion model.",
    )
    FUNCTION = "encode"

    CATEGORY = "conditioning"
    DESCRIPTION = "Encodes a text prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images."

    def encode(self, input_prompt_1, input_prompt_2, folder_path, file_path):
        prompt = input_prompt_1
        if input_prompt_2 and input_prompt_2 != "":
            prompt += "," + input_prompt_2

        _ = tools.parse_prompt_to_wildcards(prompt, folder_path, file_path)
        return (_,)

    def IS_CHANGED(id):
        return True
