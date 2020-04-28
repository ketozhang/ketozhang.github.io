---
title: Ubuntu
---

Instructions taken primarily from [Python 3's official docs](https://docs.python.org/3/using/unix.html).

## Ubuntu/Debian

::: Note :::
In summary,

```sh
sudo apt install python3 python3-dev
```

:::

Ubuntu and Debian can use APT to get python very easily however it will rarely be the latest stable release.

```sh
sudo apt install python3
```

If you plan to develop (including using virtual environments), make sure to get the development package as well.

```sh
sudo apt install python3-dev
```

## Build From Source

::: Warning
Highly not recommended due to difficulty of upgrading and uninstalling
:::

To get the latest stable release, the primary way is to build from [source code](https://www.python.org/downloads/source/).

::: Note
In the extracted `Python-3.x.x` directory,

```sh
sudo apt install zlib
./configure --prefix=/path/to/install/destination
make
make install
```

You may need `sudo` depends on where you're installing.

:::

## Version Manager

To get the best of both worlds (up to date and easy upgrade/downgrade), the best solution is to use a version manager.

### Pyenv

Pyenv is a dedicated version manager that not only support official Python distributions but also various other distributions.

```sh
curl https://pyenv.run | bash
```

In your profile config (e.g., `.bashrc`, `.zshrc`) add this,

```sh
...
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

```sh
exec $SHELL
pyenv update
pyenv install 3.x.x
```

### Anaconda

Anaconda is a distribuition --- a curated suite of software (including Python) and package used in data science.
