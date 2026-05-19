from llm_sdk import Small_LLM_Model
from m3_prompt_to_ai import prompt_to_ai
import numpy as np


def constrained_decoding(user_prompt: str, func_defs_path: str) -> str:

    llm = Small_LLM_Model()

    ai_prompt = prompt_to_ai(user_prompt, func_defs_path)

    ids = llm.encode(ai_prompt).tolist()[0]

    generated_ids = []

    for _ in range(100):

        logits = llm.get_logits_from_input_ids(ids)

        max_id = np.argmax(logits)

        ids.append(max_id)

        generated_ids.append(max_id)

    res = llm.decode(generated_ids)

    print(res)
