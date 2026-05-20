from pydantic import ValidationError
from .m1_parsing import parse_args, get_json_content, ParsePrompt
from .m1_parsing import Parse_Func_Def
import sys
from llm_sdk import Small_LLM_Model
from .m2_sys_prompt import sys_prompt, lst_of_funcs
from .m3_const_decod import Llm_Get_Right_Function


def main():

    # get 3 paths sous forme de NameSpace object :
    # (functions_definition, input, output)
    args = parse_args()

    prompts = get_json_content(args.input)
    func_defs = get_json_content(args.functions_definition)

    prompts = [ParsePrompt(**i) for i in prompts]

    func_defs = [Parse_Func_Def(**i) for i in func_defs]

    llm = Small_LLM_Model(args.model)


    lst_functs = lst_of_funcs(func_defs)

    for pr in prompts:
        ai_prompt = sys_prompt(func_defs, pr.prompt)
        right_function = Llm_Get_Right_Function(llm, lst_functs, ai_prompt)
        print(right_function.print())


if __name__ == "__main__":

    try:

        main()

    except ModuleNotFoundError as e:
        # If we dont have the module
        print("Error", e)
        sys.exit(1)

    except ImportError as e:
        # The module exist but the import faild (no method, class, circ import)
        print("Error", e)
        sys.exit(1)

    except ValidationError as e:
        # for pydantic
        print("❌ Data Validation Error!")
        print(e)
        sys.exit(1)

    except Exception as e:
        # any other exceptions (very important. dont miss Exception)
        print(e)
        sys.exit(1)
