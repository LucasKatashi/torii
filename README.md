<p align="center">
<h1 align="center"><b>Torii</b></h1>

### Summary

The torii project is a tool that aims to enable the execution of tools through the macOS terminal by making all TCP traffic pass through the Tor network.

Tools that use UDP connection are blocked (ideally).

### Instalation

- `git clone https://github.com/LucasKatashi/torii && brew install tor`
- `cd torii`
- `python3 -m pip install -r requirements.txt && chmod +x torii.py`
- `./torii.py`

---

### Usage

```
usage: ./torii.py [OPTIONAL] --proxy <PORT>

torii uses proxy port from Tor as default gateway.

options:
  -h, --help            show this help message and exit
  -p, --proxy           Specify the value of the port on which the Tor proxy
                        service is running.
```

---

### License

This work is licensed under [MIT License.](/LICENSE.md)
