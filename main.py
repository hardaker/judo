from tinyCompiler import PythonParser, Compiler

# parser = PythonParser('interpreter.py')

compiler = Compiler(parser_filename='/home/adam/GitHub/bashlex/bashlex/parser.py', interpreter_filename='interpreter.py', output_filename='judo/parser.py')
compiler.build()

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/home/adam/GitHub/judo/judo/')

import parser as bashlex

nodes = bashlex.parse("echo this | echo that")
# echo something else | echo this ; echo even more

for node in nodes:
    node.command()
    # print(node.dump())
    # print(hasattr(node, 'command'))

# for node in nodes:
#     print(node.dump())
# print(parser.dump())
