# Working with Files
## Exception handling
### File permissions

##### Example of errors/exception
-  `value error`
- `syntax error`
- `out of bounds `
- `key error`
- `attribute error`
- `ZeroDivisionError: division by zero`

##### File permissions

- `r` This is the default mode. It opens file for reading
- `w` This mode opens file for writing. If file doesn't exist, it creates a new file for us
- `x` Creates a new file, if already exists, the operation fails
- `a` Opens file in Append Mode, if file doesn't exist, it creates a new one
- `t` This the default mode to open in text mode
- `b` This for binary mode
- `+` This will open a file for reading and writing (updating) 

**we have `try` `except` and `finally`**
- `try` works as `if condition`
- `except` works as `elif`
- `finally` works as else, finally will execute regardless of `try` and `except` conditions  

#### Items in a list task

main.py
```python
from pack import p_exceptions
pex = p_exceptions.PExceptions()
pex.exce(input("Please enter what items you would like to add: ")) #seperate items by commas
```

p_exceptions.py
```python
class PExceptions:
    def exce(self, item):
        try: #check if file exists
            file = open("order.txt", "r+") #read and write
            print("File found, the contents are:")
            print(file.read()) #position of writing is now pushed to the end
            for x in item.split(","):
                file.write(x.lstrip() + "\n")
            file.close()
        except FileNotFoundError as errmsg: #create file if it doesn't exist
            print("File not found: {}".format(errmsg))
            print("Creating the file...")
            file2 = open("order.txt", "w")
            for x in item.split(","):
                file2.write(x.lstrip() + "\n")
            file2.close()
        finally:
            print('Goodbye')
```