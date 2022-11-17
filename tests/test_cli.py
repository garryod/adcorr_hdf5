import subprocess
import sys

from adcorr_hdf5 import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "adcorr_hdf5", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
