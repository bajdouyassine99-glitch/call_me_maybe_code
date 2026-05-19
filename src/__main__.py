from pydantic import ValidationError
from .m1_args_parse import parse_args
from .m2_jsons_parse import get_json_content, ParsePrompt, Parse_Func_Def
import sys


def main():

    # get 3 paths sous forme de Dict : (functions_definition, input, output)
    args_dict = parse_args()

    raw_prompts = get_json_content(args_dict["--input"])
    raw_func_defs = get_json_content(args_dict["--functions_definition"])

    prompts = [ParsePrompt(**i) for i in raw_prompts]
    func_defs = [Parse_Func_Def(**i) for i in raw_func_defs]


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
