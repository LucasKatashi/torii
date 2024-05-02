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
             T                   torii v0.2
             |                   by katashi
             ! 
             :         . : 
             .       *"""
  console.print(f"[purple]{art}[/purple]")
