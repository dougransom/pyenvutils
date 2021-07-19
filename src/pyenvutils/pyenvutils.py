import sys
import sysconfig as sc

def stdlib():
    print(sc.get_path('stdlib'))

def platlib():
    print(sc.get_path('platlib'))

def purelib():
    print(sc.get_path('purelib'))

def include():
    print(sc.get_path('include'))

def platinclude():
    print(sc.get_path('platinclude'))

def scripts():
    print(sc.get_path('scripts'))

def data():
    print(sc.get_path('data'))

def prefix():
    print(sys.prefix)


def base_prefix():
    print(sys.base_prefix)


def exec_prefix():
    print(sys.base_prefix)


def executable():
    print(sys.executable)


def float_info():
    print(sys.float_info)


def hash_info():
    print(sys.hash_info)


def hexversion():
    print(sys.hexversion)


def int_info():
    print(sys.int_info)


def implementation():
    print(sys.implementation)


def path():
    print(sys.path)


def platform():
    print(sys.platform)


def platlibdir():
    """Python 3.9 or later."""
    print(sys.platlibdir)


def version_info():
    print(sys.version_info)


def winver():
    print(sys.winver)
