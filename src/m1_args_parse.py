from typing import Dict
import argparse


def parse_args() -> Dict[str, str]:

    args_parser = argparse.ArgumentParser(description="---- Args helper ----")
    # args_parser now is a object de type ArgumentParser

    args_parser.add_argument(
                                "--functions_definition",
                                type=str,
                                default="data/input/functions_definition.json",
                                help="Enter Your Function Definition File Path"
                            )
    # add_argument(): Add a argument in the ArgumentParser (args_parser)

    args_parser.add_argument(
                                "--input",
                                default="data/input/function_calling_tests."
                                "json",
                                type=str,
                                help="Enter Your input file path"
                            )

    args_parser.add_argument(
                                "--output",
                                default="data/output/function_calls.json",
                                type=str,
                                help="Enter Your output file path"
                            )

    args = args_parser.parse_args()
    # args is Namespace

    return (
                {
                    "--functions_definition": args.functions_definition,
                    "--input": args.input,
                    "--output": args.output
                }
           )


if __name__ == "__main__":

    print(parse_args())
    # We dont need de catch args errors. argparse module handel it itself
    # using try-except and sys.exit
