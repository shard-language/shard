import argparse
from parser import parser
from environment import Environment
import os

def main():
    version = "0.0.3"

    argparser = argparse.ArgumentParser(description="The Shard programming language compiler")

    argparser.add_argument('-v', '--version', action="store_true", help="Displays the used version of the Shard compiler")
    argparser.add_argument('-c', '--compile', type=str, help="Compiles the provided Shard file")

    arguments = argparser.parse_args()

    if arguments.version:
        print(f"Shard compiler version {version} released under MIT license")
    elif arguments.compile:
        if os.path.isfile(arguments.compile):
            with open(arguments.compile, 'r') as file:
                content = file.read()

                env = Environment()
                ast = parser.parse(content)

                if ast is not None:
                    for node in ast:
                        if node is not None:
                            env.c_code.append(env.evaluate(node))

                env.write_c(arguments.compile.replace('.shd', '.c') if arguments.compile.endswith('.shd') else f"{arguments.compile}.c")

if __name__ == "__main__":
    main()