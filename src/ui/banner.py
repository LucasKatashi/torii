from rich.console import Console
console = Console()

def banner():
  art = """                *          .
                      *       '
                  *                *
             .                      .
             .                      ;                 *
             :                  - --+- -  
             !           .          !                       *
             |        .             . 
             |_         +
          ,  | `.
    --- --+-<#>-+- ---  --  -
          `._|_,'
             T                   torii v0.1
             |                   by katashi
             ! 
             :         . : 
             .       *"""
  console.print(f"[purple]{art}[/purple]")