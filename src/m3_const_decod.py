from typing import List, Any, Dict
from llm_sdk import Small_LLM_Model


class Llm_Get_Right_Function:
    def __init__(self, llm: Small_LLM_Model, lst_functs: List[str],  prompt: str) -> None:
        self.llm = llm
        self.lst_functs = lst_functs
        self.prompt = prompt

    def get_ids_of_functions(self):
        return {i: self.llm.encode(i).tolist()[0] for i in self.lst_functs}
   










if __name__ == "__main__":
    pass