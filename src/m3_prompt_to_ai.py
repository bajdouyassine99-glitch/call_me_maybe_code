from m2_jsons_parse import get_json_content
import json


def prompt_to_ai(user_prompt: str, func_defs_path: str) -> str:

    func_defs = get_json_content(func_defs_path)

    func_defs = json.dumps(func_defs, separators=(",", ":"))
    # A revoir (Mafhemtch 3lach "," 3ad ":" o machi ":" 3ad ",")

    system = (
                "You are a helpful function calling agent.\n"
                f"You have access to the following functions: {func_defs}\n"
                "You must strictly output a valid JSON object containing "
                "exactly 'name' and 'parameters' keys."
             )

    user = user_prompt

    assistant = "{"
    # zdna hadi bach llm i fhem bli khassi ikmel 3liha
    # ila madrnahach, ghadi i ibda matalan b : sure. here the answer ...

    return (
            f"<|im_start|>system\n{system}<|im_end|>\n"
            f"<|im_start|>user\n{user}<|im_end|>\n"
            f"<|im_start|>assistant\n{assistant}"
           )
