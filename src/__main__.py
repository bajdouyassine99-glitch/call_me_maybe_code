from .m1_args_parser import parse_args
from .m2_json_parser import get_json_content, ParsePrompt, ParseFuncDef
from .m3_sys_prompt import sys_prompt
from pydantic import ValidationError
from llm_sdk import Small_LLM_Model
from .m4_cons_decoding import func_name_const_decod, full_constr_decod


def main():

    # get 4 paths sous forme de Dict object :
    # (functions_definition, input, output, model)
    args = parse_args()

    prompts = get_json_content(args["input"])
    prompts_parse = [ParsePrompt(**i) for i in prompts]

    funcs_def = get_json_content(args["functions_definition"])
    funcs_def_parse = [ParseFuncDef(**i) for i in funcs_def]

    ai_prompt = sys_prompt(funcs_def, prompts[0]['prompt'])

    llm = Small_LLM_Model()

    vocab = get_json_content(llm.get_path_to_vocab_file())

    ai_func = func_name_const_decod(llm, funcs_def, ai_prompt)

    res = full_constr_decod(llm, funcs_def, ai_func, prompts[0]['prompt'], ai_prompt)

    print(res)












if __name__ == "__main__":

    try:

        main()

    except ModuleNotFoundError as e:
        # If we dont have the module
        print("Error", e)

    except ImportError as e:
        # The module exist but the import faild (no method, class, circ import)
        print("Error", e)

    except ValidationError as e:
        # for pydantic
        print("❌ Data Validation Error!")
        print(e)

    # except Exception as e:
    #     # any other exceptions (very important. dont miss Exception)
    #     print(e)
