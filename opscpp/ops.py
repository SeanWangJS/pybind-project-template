from .bindings import add as cpp_add

def add(a, b):
    return cpp_add(a, b)