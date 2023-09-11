#!/usr/bin/env python
from setuptools import setup

setup(
    name='libagent',
    version='0.14.8',
    description='Using hardware wallets as SSH/GPG/age agent',
    author='Roman Zeyde',
    author_email='dev@romanzey.de',
    url='http://github.com/romanz/trezor-agent',
    packages=[
        'libagent',
        'libagent.age',
        'libagent.device',
        'libagent.gpg',
        'libagent.signify',
        'libagent.ssh',
    ],
    install_requires=[
        'bech32>=1.2.0',
        'cryptography>=3.4.6',
        'docutils>=0.14',
        'python-daemon>=2.3.0',
        'wheel>=0.32.3',
        'backports.shutil_which>=3.5.1',
        'ConfigArgParse>=0.12.1',
        'python-daemon>=2.1.2',
        'ecdsa>=0.13',
        'pynacl>=1.4.0',
        'mnemonic>=0.18',
        'pymsgbox>=1.0.6',
        'semver>=2.2',
        'unidecode>=0.4.20',
        'pywin32>=300;sys_platform=="win32"'
    ],
    platforms=['POSIX', 'win32'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: Communications',
        'Topic :: Security',
        'Topic :: Utilities',
    ],
)
