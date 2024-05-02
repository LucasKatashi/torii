<p align="center">
<h1 align="center"><b>Torii</b></h1>

<div align="center">
    <img src="./banner.png">
</div>

### Summary

The torii project is a tool that aims to enable the execution of tools through the macOS terminal by making all TCP traffic pass through the Tor network. Tools that use UDP connection are blocked (ideally).

While the tool can function in Linux environments, it may not offer the optimal experience. For Linux distributions, I highly recommend using [nipe](https://github.com/htrgouvea/nipe). Torii, on the other hand, serves as a convenient alternative tailored specifically for macOS.

---

### Instalation

- `git clone https://github.com/LucasKatashi/torii && brew install tor`
- `cd torii`
- `python3 -m pip install -r requirements.txt && chmod +x torii.py`
- `./torii.py`

[![asciicast](https://asciinema.org/a/FWgSxWsbByv2AhbJULJR0qnmz.svg)](https://asciinema.org/a/FWgSxWsbByv2AhbJULJR0qnmz)

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

### Contribution

Feel free to contribute to the project, especially for any aspect that you notice that breaks the privacy logic of the tool. For example, the possibility of running tools that cannot be passed through the Tor network.

---

### Acknowledgements

Thanks [nipe](https://github.com/htrgouvea/nipe). The project served as motivation to this project.

---

### License

This work is licensed under [MIT License.](/LICENSE.md)
