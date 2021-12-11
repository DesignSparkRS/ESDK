# Python examples for testing peripherals

The simple examples in this directory are for use in testing peripherals and to
aid development.

## Installation

Execute the following series of commands:

```
$ sudo apt update && sudo apt dist-upgrade

$ sudo apt install git python3-venv

$ git clone git@github.com:DesignSparkrs/ESDK.git

$ cd ESDK/software/test

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt

```

Note that whenever the command prompt is prefixed with "(venv)" this means that
the Python virtual environment is activated and scripts can be run. However, if
you log out and back in again or reboot, it will be neccessary to activate the
environment again. This is simply done with:

```
$ cd ESDK/software/test

$ source venv/bin/activate
```

### Running the examples

Each Python script includes two optional arguments:

* `-i <seconds>` (sampling interval - default = 5s)
* `-f <filename>`

E.g.:

```
$ ./SHT31.py -i 10 -f temphum.csv 
```

### Updating

To get the latest versions run the following commands:

```
$ git pull

$ pip install -r requirements.txt
```

The first command fetches any updates from GitHub.

The second command checks the Python dependencies and if these have been
updated, gets them from PyPy.

Note: this assumes that you are in still in the `test` directory and the Python
virtual environment is active (the command prompt has the "(venv)" prefix.
