'''Question: 
Write a Python program to list the special variables used within the language.
'''

# Python code: 

s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print()
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
print()


'''Output sample: 
ArithmeticError AssertionError AttributeError BaseException BlockingIOError BrokenPipeError BufferError BytesW
arning                                                                                                        
ChildProcessError ConnectionAbortedError ConnectionError ConnectionRefusedError ConnectionResetError Deprecati
onWarning EOFError Ellipsis                                                                                   
EnvironmentError Exception False FileExistsError FileNotFoundError FloatingPointError FutureWarning GeneratorE
xit                                                                                                           
IOError ImportError ImportWarning IndentationError IndexError InterruptedError IsADirectoryError KeyError     
KeyboardInterrupt LookupError MemoryError NameError None NotADirectoryError NotImplemented NotImplementedError
OSError OverflowError PendingDeprecationWarning PermissionError ProcessLookupError RecursionError ReferenceErr
or ResourceWarning 
----------
 filter float format frozenset getattr globals hasattr hash                                                    
help hex id input int isinstance issubclass iter                                                              
len license list locals map max memoryview min                                                                
next object oct open ord pow print property                                                                   
quit range repr reversed round set setattr slice                                                              
sorted staticmethod str sum super tuple type vars                                                             
zip   
'''