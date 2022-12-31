# Judo: Bash, but safely!

## Starting the CLI

To start the CLI run: python3 run.py

main.py shows a simple example of using the interpreter without the need for the CLI

<br/>

## Command Format

Judo commands take a very similar format to bash commands, but with a significant reduction in complexity. They can only take the format: 

    COMMAND -FLAGS SPACE SEPARATED ARGUMENTS

<br/>
<br/>

# Commands

## LOAD

Takes a single argument of a bash file you wish to step through. Loading the file allows the user to step through it on the CLI using the next command or to undo a step with the undo command. This does not run any commands by default. 

<br/>

## NEXT

Runs the next line of the bash file which you previously loaded. Using the -e flag WILL RUN THE COMMAND ON THE HOST SYSTEM WITHOUT PROTECTION (it will replace it as much as possble). Using the -i flag will allow the user call 'inch' (see below) to step through the command in detail.

<br/>

## UNDO

Reversts the interpreter to the last saved state (either user defined to at the end of the most recent run or next command). This destroys the current environment state so you must re-run the commands to get back to that point.

<br/>

## SKIP

This allows the user to skip a command in the bash file without running it

<br/>

## SAVE

This allows users to create their own named save points in the history. The name is specified in the args and can be space separated.

<br/>


## BUILD

This allows users to create the action stack (ie what actions the bashparse interpreter should take) without actually executing them. Calling inch until the action stack is empty will yeild the same results as running the command using 'run'

<br/>

## INCH

This executes a single entry off the action stack. It allows the user a fine grained control over the execution of a bash script and allows for detailed modification of the runtime environment.

<br/>

## RUN

This allows the user to run bash commands directly from the CLI. The entire command should be specified in the arguments. Using the -e flag WILL RUN THE COMMAND ON THE HOST SYSTEM WITHOUT PROTECTION (it will replace it as much as possble). The -i flag will alias to the 'build' command.

<br/>

## STACK

This prints the current action of the bash interpreter

<br/>

## PARSE

This will print the bash AST for whatever command is specified in the arguments.

<br/>

## HISTORY

This allows the user to print the history and modify if its collected or not. Using the -p flag will print the full history to the screen. Passing 'on', 'off', or 'toggle' as an argument will change whether you save history or not.

<br/>

## STATE

This allows the user to print or modify the current state. Passing the -p flag (or no flags) will print the current state (last entry in the history list). The -s flag allows the user to change various attributes depending on what arguments you pass in. 

To change / define a variable:

    state -s var name:value name:value

<br/>

To change / add a file to the file system:

    state -s fs name:file contents:permissions 

Permissions are rw-rw-rw- by default.

To change the current working directory:

    state -s dir /new/location

To set STDIN:

    state -s stdin Some Values

To set STDOUT:

    state -s stdout Some Values

<br/>

## ALIAS

This allows the user to create their own commands. The last argument passed in is the new command name and the arguments before that are the command you wish to create. The created command does NOT need to be a complete command, partial aliasing is allowed. Two examples are shown below:

    alias "run echo hello world; state" t

This alias will echo hello world and then print the state afterwards

    alias run echo e

This alias allows the user a shorter way to echo things in the environment as shown below:

    e Hello World

<br/>

## PASS

This command does nothing. Shouldn't ever need to use it but it does exist

<br/>

## VOID 

An alias of PASS


<br/>

## EXIT

Simply exits the terminal

<br/>

<br/>

<br/>

# Adding New Commands to the Bash Interpreter

To add new commands to use in the bash interpreter simply add a function of the following form to the Interpreter class in byInterpreter.py

    def f_<Command Name>(self, command, args):
        <Whatever implementation you desire>
    
This function can affect the state however you'd like, you can create new state in outside variables, etc. 

You should overload the showState function if you add new elements to the state, so they can be displayed in the CLI. But other than that, all updates automatically propogate so you don't need to do anything more than define the function! 

All the current state is held in the InterpreterBase class, along with all the facilities necessary to run the bash scripts. This shouldn't require any intervention but please create an issue if something isn't working as expected.
