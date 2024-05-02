from subprocess import run, PIPE
from rich.console import Console
import shutil

console = Console()

def tools_checker():
  tor = run(['brew', 'info', 'tor'], stdout=PIPE, text=True)
  proxychains = run(['brew', 'info', 'proxychains-ng'], stdout=PIPE, text=True)

  if 'Not installed' not in tor.stdout and 'Not installed' not in proxychains.stdout:
    return True
  
  elif 'Not installed' in tor.stdout or 'Not installed' in proxychains.stdout:
    tools = ['', '']

    if 'Not installed' in tor.stdout:
      tools.insert(0, 'tor')
    if 'Not installed' in proxychains.stdout:
      tools.insert(1, ' proxychains-ng')

    console.print(f'[[red]![/red]] The [blue]{tools[0]}{tools[1]}[/blue] tool is not installed on your system. Do you want to allow torii to install for you?(y/N) ', end='')
    response = input()

    if response.lower() == 'y':
      installer = run(['brew', 'install', 'tor', 'proxychains-ng'], capture_output=True)
      
      if installer.returncode == 0:
        console.print(f'[[green]+[/green]] Tools installed successfully!')
        console.print(f'[[blue]+[/blue]] Configuring proxychains.conf file...')

        config_file = "src/core/data/proxychains_config.txt"

        dest_files = [
            "/System/Volumes/Data/opt/homebrew/etc/proxychains.conf",
            "/System/Volumes/Data/opt/homebrew/Cellar/proxychains-ng/4.17/.bottle/etc/proxychains.conf"
        ]

        for dest_file in dest_files:
            shutil.copy(config_file, dest_file)

        console.print(f'[[green]+[/green]] proxychains-ng configured successfully!')

        return True
      
      elif installer.returncode == 1:
        console.print(f'[[red]![/red]] Error trying to install install.')
        return False
      
    elif response.lower() == 'n' or response.lower() == '':
      exit(0)