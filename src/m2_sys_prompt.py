from typing import List, Dict, Any
from .m1_parsing import Parse_Func_Def

def sys_prompt(func_defs: List[Dict[str, Any]], prompt: str):

    ai_prompt = [
                "STRICT SYSTEM RULES: use ONLY a matching function from the "
                "list bellow.\nIf NO function maches the users intent (even if "
                "type not mactch), set name: \"None\"\n"
                "NEVER use an undeclared function for a different task.\n\n"
                "Available functions:\n"
             ]

    funcs_descrpt = []

    for i in func_defs:

        name = f"-{i.name}"

        params = [
                    f"{key}:{value.type}"
                    for key, value in i.parameters.items()
                 ]
        params = f"{','.join(params)}"

        description = f"{i.description}"

        funcs_descrpt += name + f"({params}): " + description + "\n"

    output_type = [f"\nUser Request:{prompt}\nOutput: "]

    return ("".join(ai_prompt + funcs_descrpt + output_type))


def lst_of_funcs(func_def: List[Dict[str, Any]]) -> List[str]:
    return [i.name for i in func_def] + ['None']
