def sample_function():
    # Accessing __globals__ dictionary
    globals_dict = sample_function.__globals__

    # Accessing __builtins__ from the globals_dict
    builtins_module = globals_dict['__builtins__']

    # Print available built-ins
    for key in dir(builtins_module):
        print(key)

sample_function()

