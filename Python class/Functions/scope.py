# Scope is simply where a variable is visible. Inner scopes have access to variables in the global
# scope, however global scope can't use local scope variables

# global scope variable
name = "mark"


def greet():
    # Local scope variable
    name = "John"
    print(f"Hello {name}")


print(f"Hi {name}")
greet()
