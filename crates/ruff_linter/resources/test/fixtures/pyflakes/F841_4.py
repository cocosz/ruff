# The `except` binding shadows an existing binding in the same scope, so removing it is unsafe:
# Python deletes the name at the end of the `except` block.
def f():
    e = None
    try:
        1 / 0
    except ZeroDivisionError as e:
        pass
    print(e)


e = None
try:
    1 / 0
except ZeroDivisionError as e:
    pass
print(e)


# No shadowed binding: the fix remains safe.
def g():
    try:
        1 / 0
    except ZeroDivisionError as e:
        pass
