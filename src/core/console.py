import cmd
from subprocess import run
from rich.console import Console
console = Console()

class MyShell(cmd.Cmd):
    prompt = '(torii-env) ➜ '

    def default(self, line):
        return line

def start_console():
    shell = MyShell()
    while True:
        command = input(shell.prompt)

        tor_env = f'ALL_PROXY=socks5://localhost:9050 proxychains4 {command}'
        if command is None or command == 'exit':
            break
        process = run(tor_env, shell=True, capture_output=True, text=True)
        print(process.stdout, end='')