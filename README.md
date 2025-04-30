# hello_poetry_project
Hello World Project using poetry (without using requirements.txt and setup.py)

# How to setup

## poetry Install and setup
```shell
➜ cd /<your_dir>/repos/
➜  curl -sSL https://install.python-poetry.org | python3 -
```

output:
```shell

Retrieving Poetry metadata

# Welcome to Poetry!

This will download and install the latest version of Poetry,
a dependency and package manager for Python.

It will add the `poetry` command to Poetry's bin directory, located at:

/<your_user_home>/.local/bin



You can uninstall at any time by executing this script with the --uninstall option,
and these changes will be reverted.

Installing Poetry (2.1.2): Done

Poetry (2.1.2) is installed now. Great!

To get started you need Poetry's bin directory (/<your_dir>/.local/bin) in your `PATH`
environment variable.

Add `export PATH="/<your_home_dir>/.local/bin:$PATH"` to your shell configuration file.

Alternatively, you can call Poetry explicitly with `/<your_dir>/.local/bin/poetry`.

You can test that everything is set up by executing:

`poetry --version`
```

Test poetry CLI:
```shell
(.venv_3_12) ➜  etl-testing poetry --version 
zsh: command not found: poetry
(.venv_3_12) ➜  etl-testing                 

```

## Next >>
```shell

➜  ~ vi .bash_profile 
...
#Added poetry to path
export PATH="/<your_dir>/.local/bin:$PATH"

➜  ~ source .bash_profile                                                                        

➜  ~ poetry --version
Poetry (version 2.1.2)
➜  ~ 
```

## Create a Virtual Environment
```shell
➜  hello_poetry_project git:(main) ✗ python3.12 -m venv .venv_3_12                                                                                                                             
➜  hello_poetry_project git:(main) ✗ pwd                          
/<your_dir>/repos/OSS_REPOS/hello_poetry_project
➜  hello_poetry_project git:(main) ✗ source .venv_3_12/bin/activate           
(.venv_3_12) ➜  hello_poetry_project git:(main) ✗ 

```

## Error:
```
➜  LLMEvaluation source .venv_3_12/bin/activate
(.venv_3_12) ➜  LLMEvaluation cd ../hello_poetry_project 

(.venv_3_12) ➜  hello_poetry_project poetry install
Installing dependencies from lock file

Installing the current project: hello-poetry-project (0.1.0)
Error: The current project could not be installed: No file/folder found for package hello-poetry-project
If you do not want to install the current project use --no-root.
If you want to use Poetry only for dependency management but not for packaging, you can disable package mode by setting package-mode = false in your pyproject.toml file.
If you did intend to install the current project, you may need to set `packages` in your pyproject.toml file.

(.venv_3_12) ➜  hello_poetry_project 
```

## Fix:
```shell

packages = [
    { include = "hello" }
]

added to "pyproject.toml"

Sample:
=======
[tool.poetry]
name = "hello-poetry-project"
version = "0.1.0"
description = "A simple Hello World project using Poetry."
authors = ["Your Name <you@example.com>"]
packages = [
    { include = "hello" }
]

[tool.poetry.dependencies]
python = "^3.12"

[tool.poetry.scripts]
hello = "hello.main:say_hello"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## Run (SUCCESS):
```shell

(.venv_3_12) ➜  hello_poetry_project poetry install
Installing dependencies from lock file

Installing the current project: hello-poetry-project (0.1.0)
(.venv_3_12) ➜  hello_poetry_project poetry run hello
Hello, Poetry world!

(.venv_3_12) ➜  hello_poetry_project 
```

## Unit Test
In PyCharm the Unit test "Run" (Play) button was not activated(not visible)

### Fix:
```shell

(.venv_3_12) ➜  hello_poetry_project git:(poetry_hello) ✗ poetry install
Installing dependencies from lock file

Package operations: 4 installs, 0 updates, 0 removals

  - Installing iniconfig (2.1.0)
  - Installing packaging (25.0)
  - Installing pluggy (1.5.0)
  - Installing pytest (7.4.4)

Installing the current project: hello-poetry-project (0.1.0)
(.venv_3_12) ➜  hello_poetry_project git:(poetry_hello) ✗
```

Now got activated
