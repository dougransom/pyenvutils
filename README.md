# Python Environment Utils

Python Environment Utils is a set of command line
tools to provide information about the Python folder layout.

You might find these useful just to quickly check where the 
python executable or scripts directory is, or maybe 
you would like the information for use in a shell script.

These command line tools are simply wrappers around functions
from [sys](https://docs.python.org/3/library/sys.html) and
[sysconfig](https://docs.python.org/3/library/sysconfig.html).  The command line tools
will be installed in the `Scripts` directory for your environment if you install Python Environment Utils
with pip.

Look for functions in [sys](https://docs.python.org/3/library/sys.html) and
[sysconfig](https://docs.python.org/3/library/sysconfig.html) that match the name of the command
after removing the `pye_` prefix (i.e. the command `pye_prefix` corresponds to the `prefix` function in [sys](https://docs.python.org/3/library/sys.html]).

## Installation
Install the Python Environment Utils  in each Python environment or virtual
environment you wish to have the utils available in.

```
pip install pyenvutils
```

## Implementation and List of Commands

A one line function for each command is in `pyenvutils.py`.
`pyproject.toml` specifies the command and the Python function to execute
when the command is issued from the command line.

Here is an excerpt from `pyproject.toml` showing how `py_sysconfig` and `pye_scripts` are implemented:

```[tool.flit.scripts]
pye_sysconfig="sysconfig:_main"
pye_scripts ="pyenvutils.pyenvutils:scripts"
```

A tool called [flit](https://flit.readthedocs.io/en/latest/) builds the
python install package. When  the package is installed with pip the command
line programs will be installed in the scripts directory.  After you install 
Python Environment Utils, you can run `pye_scripts` to locate the scripts directory.

In Windows PowerShell or in Bash run:

```
ls $(pye_scripts)
```

to see all the commands available in your Python installation.

## Sample Output of Each Command
Each command is shown below, and sample output for a Python installed at `C:\python38-32`:

### System configuration

#### `pye_sysconfig`

Output:
```    
Platform: "win32"
Python version: "3.8"
Current installation scheme: "nt"

Paths: 
    data = "c:\python38-32"
    include = "c:\python38-32\Include"
    platinclude = "c:\python38-32\Include"
    platlib = "c:\python38-32\Lib\site-packages"
    platstdlib = "c:\python38-32\Lib"
    purelib = "c:\python38-32\Lib\site-packages"
    scripts = "c:\python38-32\Scripts"
    stdlib = "c:\python38-32\Lib"

Variables: 
    BINDIR = "C:\Python38-32"
    BINLIBDEST = "c:\python38-32\Lib"
    EXE = ".exe"
    EXT_SUFFIX = ".cp38-win32.pyd"
    INCLUDEPY = "c:\python38-32\Include"
    LIBDEST = "c:\python38-32\Lib"
    SO = ".cp38-win32.pyd"
    VERSION = "38"
    abiflags = ""
    base = "c:\python38-32"
    exec_prefix = "c:\python38-32"
    installed_base = "c:\python38-32"
    installed_platbase = "c:\python38-32"
    platbase = "c:\python38-32"
    prefix = "c:\python38-32"
    projectbase = "C:\Python38-32"
    py_version = "3.8.10"
    py_version_nodot = "38"
    py_version_short = "3.8"
    srcdir = "C:\Python38-32"
    userbase = "C:\Users\dougr\AppData\Roaming\Python" 
``` 

### Path information

#### `pye_scripts`

```c:\python38-32\Scripts```

#### `pye_data`

```c:\python38-32```

#### `pye_platinclude`

```c:\python38-32```

#### `pye_include`

```c:\python38-32\Include```

#### `pye_purelib`

 ```c:\python38-32\Lib\site-packages```

#### `pye_platlib`

```c:\python38-32\Lib\site-packages```

#### `pye_stdlib`

```c:\python38-32\Lib```

#### `pye_path`

``` ['C:\\Python38-32\\Scripts\\pye_path.exe', 'C:\\Users\\dougr\\OneDrive\\doug\\codingprojects\\pydir\\%PYTHONPATH%', 'C:\\Users\\dougr\\Doug Ransom Financial Services\\operations - Documents\\scripts\\bulk mutual funds', 'c:\\python38-32\\python38.zip', 'c:\\python38-32\\DLLs', 'c:\\python38-32\\lib', 'c:\\python38-32', 'c:\\python38-32\\lib\\site-packages', 'c:\\python38-32\\lib\\site-packages\\win32', 'c:\\python38-32\\lib\\site-packages\\win32\\lib', 'c:\\python38-32\\lib\\site-packages\\Pythonwin']```

### Prefix information

#### `pye_prefix`

```c:\python38-32```

#### `pye_base_prefix`

```c:\python38-32```

#### `pye_exec_prefix`

```c:\python38-32```

### Executable, versions, and information

#### `pye_executable`  

```c:\python38-32\python.exe```

#### `pye_implementation`

```namespace(cache_tag='cpython-38', hexversion=50858736, name='cpython', version=sys.version_info(major=3, minor=8, micro=10, releaselevel='final', serial=0))```

#### `pye_float_info`

```sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)```

### `pye_int_info`
```sys.int_info(bits_per_digit=15, sizeof_digit=2)```

#### `pye_hash_info`

```sys.hash_info(width=32, modulus=2147483647, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)```

#### `pye_hex_version`

```50858736```

#### `pye_platform`

```win32 ```

#### `pye_version_info`

```sys.version_info(major=3, minor=8, micro=10, releaselevel='final', serial=0)```

#### `pye_winver`

```3.8-32```
