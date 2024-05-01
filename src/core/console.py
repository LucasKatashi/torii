import cmd
from subprocess import run
from rich.console import Console
console = Console()

class MyShell(cmd.Cmd):
    prompt = '(torii-env) ➜ '

    def default(self, line):
        return line

def start_console():
    not_supported = ['ping', 'nmap']

    shell = MyShell()
    while True:
        command = input(shell.prompt)

        if any(substring in command for substring in not_supported):
            console.print(f'[[red]![/red]] Command {command} not supported.')
            continue

        tor_env = f'ALL_PROXY=socks5://localhost:9050 {command}'
        if command is None or command == 'exit':
            break
        process = run(tor_env, shell=True, capture_output=True, text=True)
        print(process.stdout, end='')