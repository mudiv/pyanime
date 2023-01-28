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

* `id` : An anime identifier with which to fetch anime episodes

## Get anime episodes
```python 

from anime4k  import Episodes

# We use a specific anime ID to get the episodes
d=Episodes(id="6172732D6E6F2D6B796F6A7575").anime()

print(d)
```
### result 
```json
{
   "data":{
      "title":"Ars no Kyojuu",
      "story-episode":"قصة انمي Ars no Kyojuu تدور في عصر السيوف والأبطال والأساطير. أنشأت الوحوش العملاقة الأرض، ولكن بعد ذلك سرق البشر تلك الأرض. أثار هذا غضب الوحوش التي بدأت بعد ذلك في أكل البشر. من أجل المقاومة، دعا البشر الآلهة. وبدأت وحوش “كيوجو” تنتشر في جميع أنحاء العالم، مما تسبب في أضرار جسيمة، لكن البشر قاوموا من خلال صيد “كيوجو“. بينما ازدهرت البشرية باستخدام الأجزاء المشرحة من الوحوش. “جيرو” هو «رجل نجا من الموت»، ويطارد “كيوجو” لكسب لقمة العيش. يلتقي بـ”كومي” التي يطاردها شخص ما. ثم يبدأ “جيرو” وأصدقاؤه في الكشف عن أسرار هذا العالم.\n",
      "img":"https://o.anime-slayer.com/wp-content/uploads/2023/01/132161.webp",
      "Type":"النوع: TV",
      "show-start":"بداية العرض: 2022",
      "anime-status":"حالة الأنمي: يعرض الان",
      "number-of-episodes":"\nعدد الحلقات:\n12 ",
      "episode-duration":"مدة الحلقة: 23 دقيقة",
      "season":"الموسم: شتاء 2023",
      "Source":"المصدر: اصلي",
      "teaser":"https://youtu.be/ukE3G4b_K0w",
      "MAL":"https://myanimelist.net/anime/53179"
   },
   "category":[
      {
         "category":"أكشن",
         "id":"256438256133256439253833256438256234256439253836"
      },
      {
         "category":"فنتازيا",
         "id":"256439253831256439253836256438256161256438256137256438256232256439253861256438256137"
      },
      {
         "category":"مغامرات",
         "id":"256439253835256438256261256438256137256439253835256438256231256438256137256438256161"
      }
   ],
   "episodes":[
      {
         "number-anime":1,
         "img":"https://o.anime-slayer.com/wp-content/uploads/2023/01/132161-225x220.webp",
         "name":"Ars no Kyojuu الحلقة 1",
         "numbar-episode":"الحلقة 1",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D31"
      },
      {
         "number-anime":2,
         "img":"https://o.anime-slayer.com/wp-content/uploads/2023/01/132161-225x220.webp",
         "name":"Ars no Kyojuu الحلقة 2",
         "numbar-episode":"الحلقة 2",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D32"
      },
      {
         "number-anime":3,
         "img":"https://o.anime-slayer.com/wp-content/uploads/2023/01/132161-225x220.webp",
         "name":"Ars no Kyojuu الحلقة 3",
         "numbar-episode":"الحلقة 3",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D33"
      },
      {
         "number-anime":4,
         "img":"https://o.anime-slayer.com/wp-content/uploads/2023/01/132161-225x220.webp",
         "name":"Ars no Kyojuu الحلقة 4",
         "numbar-episode":"الحلقة 4",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D34"
      }
   ]
}
         

```
* `category` : Anime category `id category` Anime of the same category can be displayed through the category id
