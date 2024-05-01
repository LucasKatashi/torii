from subprocess import run

def start_tor():
  process = run(['brew', 'services', 'start', 'tor'], capture_output=True)

  return process.returncode