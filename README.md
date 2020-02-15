# network sniffer

This is a little freetime project in Python.\
This script pings all IP's in the range the user provides or in the range from 1 to 254 and reports all back that appear to be alive.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements:

```bash
pip install -r requirements.txt
```

## Usage

For CLI version run `app.py` with python3:

```bash
python3 app.py
```

If you prefer a GUI run `app_gui.py` with python3:

```bash
python3 app_gui.py
```

**Full IP range**

- CLI-option 1
- scans all IP's from x.x.x.1 to x.x.x.254)

**Custom IP range**

- CLI-option 2
- scans IP's in provided range)

**Keep in mind:**\
Between each ping there is a random sleep-time of up to 5 seconds to not flood the network.\
Therefore a full scan or a custom scan with a large range can potentially take a **long** time!s

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
