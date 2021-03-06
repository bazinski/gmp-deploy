import pytest
import os
import publish_ci2 as p
try:
    import mock
except ImportError:
    from unittest import mock


@mock.patch.dict(os.environ, {'TARBALL': '', 'ZENODO_API_KEY': ''})
def test_setup_empty_env():
    with pytest.raises(Exception) as empty_vars:
        token, data = p.setup()
        print empty_vars


@mock.patch.dict(os.environ, {'TARBALL': 'tarball.tar.gz', 'ZENODO_API_KEY': '101010101'})
def test_setup_fake_env():
    assert p.setup()


@mock.patch.dict(os.environ, {'SHELL': '/bin/bash',
                              'PWD': '/home/becker/SAGrid-2.0/gmp-deploy'})
def test_setup_no_env():
    with pytest.raises(KeyError) as no_vars:
        print os.environ['TARBALL']
        p.setup()
