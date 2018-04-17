'''Question: 
Write a Python program to find the available built-in modules.
'''

# Python code: 

import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))


'''Output sample: 
_ast, _bisect, _codecs, _collections, _datetime, _elementtree,                                                
_functools, _heapq, _imp, _io, _locale, _md5, _operator, _pickle,                                             
_posixsubprocess, _random, _sha1, _sha256, _sha512, _signal, _socket,                                         
_sre, _stat, _string, _struct, _symtable, _thread, _tracemalloc,                                              
_warnings, _weakref, array, atexit, binascii, builtins, errno,                                                
faulthandler, fcntl, gc, grp, itertools, marshal, math, posix, pwd,                                           
pyexpat, select, spwd, sys, syslog, time, unicodedata, xxsubtype,                                             
zipimport, zlib 
'''