from distutils.core import setup, Extension

luala_hash_module = Extension('luala_hash',
                                 sources = ['lualamodule.c',
                                            'luala.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
                                            'sha3/shavite.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'luala_hash',
       version = '1.3.1',
       description = 'Binding for Luala X11 proof of work hashing.',
       ext_modules = [luala_hash_module])
