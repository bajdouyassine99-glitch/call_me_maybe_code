import argparse
from pydantic import BaseModel
from typing import Dict, Any
import json
import sys


def parse_args():
    """ Parsing Terminal Arguments. """

    args_parser = argparse.ArgumentParser(description="---- Args helper ----")
    # args_parser now is a object de type ArgumentParser

    args_parser.add_argument(
                                "--functions_definition",
                                type=str,
                                default="data/input/functions_definition.json",
                            )
    # add_argument(): Add a argument in the ArgumentParser (args_parser)

    args_parser.add_argument(
                                "--input",
                                type=str,
                                default="data/input/function_calling_tests."
                                "json",
                            )

    args_parser.add_argument(
                                "--output",
                                type=str,
                                default="data/output/function_calls.json",
                            )

    args_parser.add_argument(
                                "--model",
                                type=str,
                                default="Qwen/Qwen3-0.6B",
                            )

    args = args_parser.parse_args()
    # args is Namespace

    return args


def get_json_content(json_path) -> Any:
    """ Read JSON content (inputs JSON) """

    # I used return: Any, because i need this function to read also vocab.json

    try:

        with open(json_path, "r") as f:
            content = json.load(f)

        return content

    except FileNotFoundError:
        print(f"❌ Error: File not found -> {json_path}")
        sys.exit(1)

    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON format in -> {json_path}")
        sys.exit(1)

    except PermissionError:
        print(f"❌ Error: Permission denied -> {json_path}")
        sys.exit(1)

    except IsADirectoryError:
        print(f"❌ Error: is a directory -> {json_path}")
        sys.exit(1)

    except Exception as e:
        print("Error In One Of JSON Files:", e)
        sys.exit(1)


class ParsePrompt(BaseModel):
    prompt: str


# This class for internal dict
class Nested_Dict(BaseModel):
    type: str


class Parse_Func_Def(BaseModel):
    name: str
    description: str
    parameters: Dict[str, Nested_Dict]
    returns: Nested_Dict


if __name__ == "__main__":

    print(parse_args())
    # We dont need de catch args errors. argparse module handel it itself
    # using try-except and sys.exit
