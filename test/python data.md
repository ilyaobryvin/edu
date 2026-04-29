```python
# list with list as rows
header = ["id", "product", "price"] # index = [0, 1, 2]
[
    [0, 1, 2],
    ["Чай", "Кофе", "Печенье"],
    [100, 200, 150] 
]

# list with dict as rows
[
    {"id": 0, "product": "Чай", "price": 100},
    {"id": 1, "product": "Кофе", "id": "Напитки", "price": 200},
    {"id": 2, "product": "Печенье", "id": "Сладости", "price": 150}
]

# dict with lists as rows
{
    'id': [0, 1, 2],
    'product': ["Чай", "Кофе", "Печенье"],
    'price': [100, 200, 150] 
}

# dict with dicts
{
    'id': {0: 0, 1: 1, 2: 2},
    'product': {0: 'tea', 1: 'coffee', 2: 'cookies'},
    'price': {0: 100, 1: 200, 2: 300}
}
```