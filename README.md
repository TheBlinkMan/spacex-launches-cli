# SpaceX Launches CLI

Simple cli to read the launches endpoint of the SpaceX REST API v3

## USAGE

```
git clone https://github.com/TheBlinkMan/spacex-launches-cli.git
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python cli.py
```

## Requirements

Internet connection

GIT

Python 3.7+

## TODO

- [ ] Add a wrapper to the requests api
- [ ] Create a class to represent a launch
- [ ] Create unit tests

## Common issues

[The menu options are are shuffled](https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6/39980744)

[Python3 UnicodeEncodeError](https://medium.com/@diewland/python3-unicodeencodeerror-ascii-codec-can-t-encode-characters-in-position-0-9-ordinal-not-in-70ce922c552)
