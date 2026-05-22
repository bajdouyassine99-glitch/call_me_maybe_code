from pydantic import BaseModel
import json
from typing import Any, Dict


def get_json_content(json_path: str) -> Any:
    """ Read JSON content (inputs JSON) """

    # I used return: Any, because i need this function to read also vocab.json

    try:

        with open(json_path, "r") as f:
            content = json.load(f)

        return content

    except FileNotFoundError:
        raise Exception(f"❌ Error: File not found -> {json_path}")

    except json.JSONDecodeError:
        raise Exception(f"❌ Error: Invalid JSON format in -> {json_path}")

    except PermissionError:
        raise Exception(f"❌ Error: Permission denied -> {json_path}")

    except IsADirectoryError:
        raise Exception(f"❌ Error: is a directory -> {json_path}")

    except Exception as e:
        raise Exception("Error In One Of JSON Files:", e)


class ParsePrompt(BaseModel):
    prompt: str


# This class for internal dict
class NestedDict(BaseModel):
    type: str


class ParseFuncDef(BaseModel):
    name: str
    description: str
    parameters: Dict[str, NestedDict]
    returns: NestedDict


if __name__ == "__main__":
    # We dont need de catch args errors. argparse module handel it itself
    # using try-except and sys.exit
    pass
