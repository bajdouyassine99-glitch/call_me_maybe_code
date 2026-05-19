from pydantic import BaseModel
from typing import Dict, Any
import json
import sys


def get_json_content(json_path) -> Any:
    # I used return: Any, because i need this function to read the vocab.json

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
        print("Error:", e)
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
