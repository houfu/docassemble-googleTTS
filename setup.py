import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.googleTTS',
      version='0.0.1',
      description=('A docassemble interview that performs text to speech with Google Cloud'),
      long_description='# docassemble-googleTTS\r\n\r\nA docassemble interview that performs text to speech with Google Cloud\r\n\r\n## What you need\r\n\r\n1. Install this interview \r\n2. Go to the Configuration and set the `tts account credentials` subdirective under the `google` directive. Set it to a service account. ([See here for details](https://docassemble.org/docs/functions.html#google%20sheets%20example) how to do it, but note the different subdirective.)\r\n3. Run interview. Make your text talk!\r\n\r\n## Limitations\r\n\r\n* Only Wavenet US voices can be selected.',
      long_description_content_type='text/markdown',
      author='Houfu Ang',
      author_email='houfu@outlook.sg',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['google-cloud-texttospeech>=2.11.0'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/googleTTS/', package='docassemble.googleTTS'),
     )

