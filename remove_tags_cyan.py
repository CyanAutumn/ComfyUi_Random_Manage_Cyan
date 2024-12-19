from comfy.comfy_types import IO, ComfyNodeABC, InputTypeDict
from custom_nodes.ComfyUi_Random_Prompt_Cyan.wildcard import tools, wildcard_file


class RemoveTagsCyan:
    @classmethod
    def INPUT_TYPES(s) -> InputTypeDict:
        return {
            "required": {
                "black_text": (
                    IO.STRING,
                    {
                        "multiline": True,
                        "dynamicPrompts": True,
                        "tooltip": "The text to be encoded.",
                    },
                ),
                "input_prompt": (
                    IO.STRING,
                    {
                        "tooltip": "字符串类型的输入",
                        "default": "",
                    },
                ),
            }
        }

    RETURN_TYPES = (IO.STRING,)
    OUTPUT_TOOLTIPS = (
        "A conditioning containing the embedded text used to guide the diffusion model.",
    )
    FUNCTION = "encode"

    CATEGORY = "conditioning"
    DESCRIPTION = "黑名单tag删除用"

    def encode(self, input_prompt, black_text):
        input_tags = [tag.strip() for tag in input_prompt.split(",")]
        black_tags = [tag.strip() for tag in black_text.split(",")]
        black_tags.extend(
            [tag.strip().replace(" ", "_") for tag in black_text.split(",")]
        )
        _ = [tag for tag in input_tags if tag not in black_tags]
        _ = str.join(" , ", _)
        return (_,)
