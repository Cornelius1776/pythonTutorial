# The zip functon takes elements from two different iterables and aggregate them, pair them in a zip
# object stored in a tuple for each element

banks = ["Stanbic", "Gt", "Union", "Wema"]
atm_pin = (1234, 6534, 9668, 8589)

accounts = zip(banks, atm_pin)  # The iterables can be more than 2
for account in accounts:
    print(account)

print(type(accounts))
# prints the elements in a tuple as zip by default, but the can be typecast into other iterables

# Typecast to list
list_accounts = list(zip(banks, atm_pin))
for account in list_accounts:
    print(account)

print(type(list_accounts))


# Typecast to set
set_accounts = set(zip(banks, atm_pin))
for account in set_accounts:
    print(account)

print(type(set_accounts))


# Typecast to dictionary
dict_accounts = dict(zip(banks, atm_pin))
for key, value in dict_accounts.items():
    print(f"{key} : {value}")

print(type(dict_accounts))
