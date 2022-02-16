## ip2d-py

A CLI to convert IP addresses to integers and vice versa

### Install

`pip install ip2d-py`
### Usage

```bash
> ip2dpy ::3 --hex
3
```

```bash
> ip2dpy 8.8.8.8
134744072
```

```bash
> ip2dpy -i 51092 --hex -c
::c794
```

```bash
> ip2dpy ff:fe20::67 --hex -o oct
0o7777704000000000000000000000000000000147
```
