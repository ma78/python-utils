# python-utils

This repo is dumping ground of useful things I've collected while learning python. It contains a set of python scripts that perform common, useful functions.


## Contents


### make

A convenient wrapper for running tests, formatting checks, linting checks and type checks.

```bash
% make help

Usage:
  make <target>

Targets:
  venv                 Create/activate python virtualenv
  fmt                  Format python code using black
  check-fmt            Perform code format using black
  check-lint           Perform pylint check
  check-type           Perform mypy check
  check                Perform fmt, lint and type checks
  test                 Perform unit tests
Help
  help                 Show help
````


### openai/chat.py

Requires an OpenAI API key. Get one from here: https://platform.openai.com/api-keys

Using a virtualenv, or otherwise, do the following to run the script:

```bash
# Install openai 
. .venv/bin/activate  # if you have a virtualenv
pip3 install openai
pip3 install dotenv

# Run script
Place OPENAI_API_KEY=<my long API key> into a .env file in the package home directory.
python3 chat.py
```

Example interaction:

```bash
% python3 chat.py
 * GPT: Ask me stuff. Enter 'done' when finished ...

 * You: Will you remember this conversation when we are finished?

( thinking .. )

 * GPT: I don't have the ability to remember past conversations once they are 
 finished. Each new conversation is treated as separate and not connected to 
 previous ones. How can I help you further with your current question?

 * You: done

 * GPT: Get outta here.

```


### datetimeutils/age.py

Takes a timestamp string with the format `%Y-%m-%d %H:%M:%S %Z` and renders a short string representing elapsed time (age).

```bash
% ./datetimeutils/age.py -h
usage: age.py [-h] -t TIMESTAMP

example: ./datetimeutils/age.py -t '2023-09-14 14:23:00 AEST'

optional arguments:
  -h, --help    show this help message and exit
  -t TIMESTAMP  timestamp, format: %Y-%m-%d %H:%M:%S %Z

# Examples
% ./datetimeutils/age.py -t '2023-09-14 18:30:00 AEST'
1h49m

% ./datetimeutils/age.py -t '2023-09-14 18:30:00 AEST'
1d1h
```


### datetimeutils/sleep_until.py

Takes a timestamp string with the format `%Y-%m-%d %H:%M:%S %Z` and sleep the number of seconds required to reach the timestamp.

```bash
% ./datetimeutils/sleep_until.py -h
usage: sleep_until.py [-h] -t TIMESTAMP

example: ./sleep_until.py -t '2023-09-14 14:23:00'

optional arguments:
  -h, --help    show this help message and exit
  -t TIMESTAMP  timestamp, format: %Y-%m-%d %H:%M:%S

# Examples
% ./sleep_until.py -t '2023-09-25 10:16:10'
 -> sleeping (14s) ..............
 -> Done.
 -> Current time: 2023-09-25 10:16:10
```