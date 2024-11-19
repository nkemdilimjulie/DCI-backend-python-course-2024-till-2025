python -3.2 # __init__.py was required
python +3.3 # __init__.py is not required

# unittest
from ns import db, func


## Exercise
- Create two namespace packages called
    - `calculator_old`
    - `calculator_new`

- Unify the two namespace packages such that we can do the following

```python
# add -> calculator_old
# sub -> calculator_new
from calc import add, sub

print(add.addition(2,3)) # 5
print(sub.subtract(5,4)) # 1
```
