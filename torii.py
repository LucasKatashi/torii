#!/usr/bin/env python3
from argparse import ArgumentParser
from rich.console import Console
from src.core.check_port import check_port
from src.core.start_tor import start_tor
from src.core.console import start_console
from src.ui.banner import banner

console = Console()

def main():
  port = check_port(args.proxy)

  if port == False:
    console.print(f'[[red]![/red]] Tor proxy port {args.proxy} is closed.\n[[yellow]?[/yellow]] Do you want to initialize the Tor service?(y/N): ', end='')
    response = input()

    if response.lower() == 'y':
      return_code = start_tor()
      if return_code == 0:
        console.print(f'[[green]+[/green]] Tor proxy started on port {args.proxy}.')
        start_console()
      else:
        console.print(f'[[red]![/red]] Failed to open tor proxy.')
        exit(1)
    elif response.lower() == 'n' or response.lower() == '':
      exit(0)

  elif port == True:
    console.print(f'[[green]+[/green]] Tor proxy port 9050 is open.')
    start_console()

if __name__ == '__main__':
  parser = ArgumentParser(description='Torii uses proxy port from Tor as default gateway.')
  parser.add_argument('-p', '--proxy', type=int, default=9050, help='Specify the value of the port on which the Tor proxy service is running.')

  args = parser.parse_args()
  
  try:
    banner()
    main()
  except EOFError:
    exit(1)
  except KeyboardInterrupt:
    exit(1)