<h1 align="center">anime4k</h1> <p align="center">A simple library that provides anime and server episodes for watching, containing more than 5,000 thousand different anime</p>


<h2><a href='https://pytba.readthedocs.io/en/latest/index.html'>Official documentation</a></h2>


## Getting started
* Installation using pip (a Python package manager):

``` 
$ pip install anime4k

```

## GET Random anime list
```python 
from anime4k import list
# parameter:	
  # letter : Letter beginning of the name of the anime (a-z)
  # Numbar : The number of anime
	
listanime= list(letter="a",Number=1).data()
print(listanime)

```
## parameter (list)
### letter
It gives a list of beginning letters only, such as a. It gives anime beginning with the letter a 
 ,Only letters can be used `(a-z)`

### Number
The required number of anime

### save

Saves the score If it is `True` 
