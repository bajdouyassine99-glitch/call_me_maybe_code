import argparse
from typing import Dict


def parse_args() -> Dict[str, str]:
    """ Parsing Terminal flags. """

    args_parser = argparse.ArgumentParser()
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

    return {
                "functions_definition": args.functions_definition,
                "input": args.input,
                "output": args.output,
                "model": args.model
           }
