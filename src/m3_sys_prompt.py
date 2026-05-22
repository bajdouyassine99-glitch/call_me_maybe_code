from typing import List, Dict, Any


def sys_prompt(func_defs: List[Dict[str, Any]], prompt: str):

    lst_funcs_def = [f"- {i['name']}\n" for i in func_defs]

    ai_prompt = (
                    "System: You are a function calling assistant. "
                    "Based on the user request, select the appropriate "
                    "function and extract its parameters.\n"
                    f"Available Functions:\n{''.join(lst_funcs_def)}\n"
                    f"User Request: {prompt}\n"
                    "Output JSON:\n"
                )

    return ai_prompt
