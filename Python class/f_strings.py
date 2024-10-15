from datetime import datetime

time = datetime.now()
print(time)

# 1
n = 200000
print(f'{n:,}')

# 2
name = 'Ironman'
print(name)
print(f'{name:<20}|')
print(f'{name:>20}/')
print(f'{name:^20}$')
print(f'{name:$^20}|')

# 3
a = 8765.3958
print(a)
print(round(a))
print(f'{a:.2f}')
print(f'{a:.0f}')
print(f'{a:,.1f}')

# 4
x = 2
y = 3
print(x + y)
print(f'x + y = {x + y}')
print(f'{x + y = }')
print(f'{name = }')