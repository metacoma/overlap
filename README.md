```
find . -type f -iname "*.json" | xargs -I{} sh -c 'cat {} | python3 ./overlap.py'
```
