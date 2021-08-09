
Practice Raising Errors
```python
raise ValueError('Value not found in the list')
```

```python
from collections import Counter
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt[1])
# OUTPUT: 3
```

```python
from collections import defaultdict
# default will be 0
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])
# OUTPUT: 0
```

```python
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
```


