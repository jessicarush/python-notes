# pyenv

See first: [pyenv docs](https://github.com/pyenv/pyenv)

These instructions come from this [intro to pyenv article](https://realpython.com/intro-to-pyenv/), but [this blog post](https://switowski.com/blog/pyenv) also looks good.

## Table of Contents

<!-- toc -->

- [Install pyenv](#install-pyenv)
- [Install python versions](#install-python-versions)
- [Remove a version](#remove-a-version)
- [Using your versions](#using-your-versions)
- [Other commands](#other-commands)

<!-- tocstop -->

## Install pyenv

Install dependencies:

```bash
brew install openssl readline sqlite3 xz zlib
```

Install pyenv:

```bash
curl https://pyenv.run | bash
```

Note: the most recent instructon in the pyenv docs say  you can just do this: 

```bash
brew update
brew install pyenv
```

There will be a message in the console saying that you need to update your PATH. Be sure to read because the instructions seem to change as they update pyenv. 

Basically, I have to add to my `.bash_profile`:

```bash
export PATH="$HOME/.pyenv/shims:$PATH"
```

However, they have a longer, roundabout way of doing this:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

The reasons are explained in the [pyenv docs](https://github.com/pyenv/pyenv#advanced-configuration).

Be sure to restart `.bash_profile`:

```bash
source ~/.bash_profile
```

## Install python versions

List all versions (warning: there's a lot):

```bash
pyenv install --list
```

List specific versions:

```bash
pyenv install --list | grep " 3\.[678]"
```

Install a version:

```bash
pyenv install -v 3.7.8
```

Each version installed with pyenv is located in your pyenv root directory:

```bash
ls ~/.pyenv/versions/
```

## Remove a version

Check the versions you have first:

```bash
ls ~/.pyenv/versions/
```

Then remove one like this:

```bash
rm -rf ~/.pyenv/versions/2.7.15
```

or like this:

```bash
pyenv uninstall 2.7.15
```

## Using your versions

First check what you have:

```bash
pyenv versions
* system (set by /Users/jessicarush/.pyenv/version)
  3.5.9
  3.6.11
  3.7.8
  3.8.5
```

The asterisk indicates which version is currently running. In the above output it's the system os version (2.7.16).

To switch you can use the `global` command:

```bash
pyenv global 3.7.8
```

now check:

```bash
pyenv versions
system
3.5.9
3.6.11
* 3.7.8 (set by /Users/jessicarush/.pyenv/version)
3.8.5
```

A great way to get peace of mind that the version of Python you just installed is working properly is to run the built-in test suite:

```bash
python -m test
```

If you ever want to go back to the system version:

```bash
pyenv global system
```

## Other commands

Note, you will need to update pyenv to see new python versions to install with `pyenv install --list`. To update pyenv:

```bash
pyenv update
```

Note that if you want to see `which python`, there will be a pyenv shim in place:

```bash
which python
/Users/jessicarush/.pyenv/shims/python
```

To see the actual path, you can run the following:

```bash
pyenv which python
/usr/bin/python
```

To see a complete list of pyenv commands:

```bash
pyenv commands
```

Each command has a `--help` flag that will give you more detailed information.

See also: [pyenv commands reference](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md#pyenv-global)
