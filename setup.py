from distutils.core import setup, Extension

module1 = Extension('led', sources = ['capslock_light.c'], extra_link_args=['-framework', 'CoreFoundation', '-framework',  'IOKit'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1],)

