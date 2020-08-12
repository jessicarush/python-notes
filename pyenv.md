# pyenv

These instruction come from [this Real Python article](https://realpython.com/intro-to-pyenv/).

## Table of Contents

<!-- toc -->

## Install pyenv

Install dependencies:
```
brew install openssl readline sqlite3 xz zlib
```

Install pyenv
```
curl https://pyenv.run | bash
```
Add to your `.bash_profile` the output provided in the console. It will look like the following but with your info:
```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Restart `.bash_profile`:
```
source /.bash_profile
```

## Install python versions

List all versions (warning: there's a lot)
```
pyenv install --list
```

List specific versions
```
pyenv install --list | grep " 3\.[678]"
```

Install a version
```
pyenv install -v 3.7.8
```

Each version installed with pyenv is located in your pyenv root directory:
```
$ ls ~/.pyenv/versions/
```

## Remove a version

Check the versions you have first:
```
$ ls ~/.pyenv/versions/
```

Then remove one like this:
```
rm -rf ~/.pyenv/versions/2.7.15
```

or like this:
```
pyenv uninstall 2.7.15
```

## Using your versions

First check what you have:
```
pyenv versions
* system (set by /Users/jessicarush/.pyenv/version)
  3.5.9
  3.6.11
  3.7.8
  3.8.5
```

The start indicates which version is currently running. In the above output it's the system os version (2.7.16).

To switch you can use the `global` command:
```
pyenv global 3.7.8
```

now check:
```
pyenv versions
system
3.5.9
3.6.11
* 3.7.8 (set by /Users/jessicarush/.pyenv/version)
3.8.5
```

A great way to get peace of mind that the version of Python you just installed is working properly is to run the built-in test suite:
```
python -m test
```

If you ever want to go back to th esystem version:
```
pyenv global system
```

## Other commands

Update pyenv:
```
pyenv update
```

Note that if you want to see `which python`, there will be a pyenv shim in place:
```
which python
/Users/jessicarush/.pyenv/shims/python
```

To see the actual path, you can run the following:
```
pyenv which python
/usr/bin/python
```

To see a complete list of pyenv commands:
```
pyenv commands
```

Each command has a `--help` flag that will give you more detailed information
