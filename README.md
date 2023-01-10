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

### result 
```json
{
    "Numbar_list_anime": 2,
    "data": [
        {
            "number_anime": 0,
            "img": "https://o.anime-slayer.com/wp-content/uploads/2023/01/132161-215x300.webp",
            "title": "Ars no Kyojuu",
            "story": "قصة انمي Ars no Kyojuu تدور في عصر السيوف والأبطال والأساطير. أنشأت الوحوش العملاقة الأرض، ولكن بعد ذلك سرق البشر تلك الأرض. أثار هذا غضب الوحوش التي بدأت بعد ذلك في أكل البشر. من أجل المقاومة، دعا البشر الآلهة. وبدأت وحوش “كيوجو” تنتشر في جميع أنحاء العالم، مما تسبب في أضرار جسيمة، لكن البشر قاوموا من خلال صيد “كيوجو“. بينما ازدهرت البشرية باستخدام الأجزاء المشرحة من الوحوش. “جيرو” هو «رجل نجا من الموت»، ويطارد “كيوجو” لكسب لقمة العيش. يلتقي بـ”كومي” التي يطاردها شخص ما. ثم يبدأ “جيرو” وأصدقاؤه في الكشف عن أسرار هذا العالم.\r\n\r\n",
            "type_tv": "\nArs no Kyojuu\n",
            "type_status": "يعرض الان",
            "id": "6172732D6E6F2D6B796F6A7575"
        }
    ]
}
```
