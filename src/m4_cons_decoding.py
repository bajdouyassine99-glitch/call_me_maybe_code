from llm_sdk import Small_LLM_Model
from typing import List, Any, Dict, Set
import numpy as np


def func_name_const_decod(
                            llm: Small_LLM_Model,
                            funcs_def: List[Dict[str, Any]],
                            one_prompt: str,
                         ):

    lst_funcs_def = [i["name"] for i in funcs_def]

    lst_ids_funcs_def = [llm.encode(i).tolist()[0] for i in lst_funcs_def]

    ids_prompt = llm.encode(one_prompt).tolist()[0]

    res_ids = []

    while True:

        logits = llm.get_logits_from_input_ids(ids_prompt + res_ids)

        temp_ids: Set[int] = set()
        # saraha mazal mafhemtch 3lach drna set()

        length = len(res_ids)

        for i in lst_ids_funcs_def:
            try:
                temp_ids.add(i[length])
            except Exception:
                pass

        masked_logits = [float("-inf")] * len(logits)

        for i in temp_ids:
            masked_logits[i] = logits[i]

        max_id = int(np.argmax(masked_logits))
        # npp.argmax() return a numpy.int64. so good practice to cast it

        res_ids.append(max_id)

        res_str = llm.decode(res_ids)

        if res_str in lst_funcs_def:
            break

    return res_str


def full_constr_decod(
                        llm: Small_LLM_Model,
                        funcs_def: List[Dict[str, Any]],
                        ai_function: str,
                        one_prompt: str,
                        ai_prompt: str
                     ):

    json_start = (
                    f'{ai_prompt}' + '{\n  "prompt": "' + f'{one_prompt}' +
                    '",\n' + '  "parameters": {"'
                 )

    print(json_start)