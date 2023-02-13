<h1 align="center">pyanime</h1> <p align="center">A simple library that provides anime and server episodes for watching, containing more than 5,000 thousand different anime</p>

[![Downloads](https://static.pepy.tech/badge/pyanime)](https://pepy.tech/project/pyanime)
[![YouTube](https://img.shields.io/static/v1?label=subscribe&logo=youtube&logoColor=ff0000&color=brightgreen&message=4.2k)](https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA)
[![Discord](https://img.shields.io/discord/566880874789076992?logo=telegram)](https://t.me/TBIBB)
<h2><a href='https://'>Official documentation</a></h2>

## Contents

  * [Getting started](#getting-started)
  * [GET Random anime list](#get-random-anime-list)
  * [Get anime episodes](#get-anime-episodes)
* [Show servers to watch the episode](#show-servers-to-watch-the-episode)
* [Search](#search-for-a-specific-anime)
* [anime categories](#anime-categories)
## Getting started
* Installation using pip (a Python package manager):

``` 
$ pip install pyanime

```

## GET Random anime list
```python 
from pyanime import list
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

from pyanime  import Episodes

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
* `id` : Episode ID
* `category` : Anime category `id category` Anime of the same category can be displayed through the category id


## Show servers to watch the episode

```python 


from pyanime  import watch


res=watch(id = "6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D34").data()

print(res)

```
### result 
```json
{
   "data":{
      "title":"Ars no Kyojuu الحلقة 4",
      "story-episode":"قصة انمي Ars no Kyojuu تدور في عصر السيوف والأبطال والأساطير. أنشأت الوحوش العملاقة الأرض، ولكن بعد ذلك سرق البشر تلك الأرض. أثار هذا غضب الوحوش التي بدأت بعد ذلك في أكل البشر. من أجل المقاومة، دعا البشر الآلهة. وبدأت وحوش “كيوجو” تنتشر في جميع أنحاء العالم، مما تسبب في أضرار جسيمة، لكن البشر قاوموا من خلال صيد “كيوجو“. بينما ازدهرت البشرية باستخدام الأجزاء المشرحة من الوحوش. “جيرو” هو «رجل نجا من الموت»، ويطارد “كيوجو” لكسب لقمة العيش. يلتقي بـ”كومي” التي يطاردها شخص ما. ثم يبدأ “جيرو” وأصدقاؤه في الكشف عن أسرار هذا العالم.\n",
      "img":"https://o.anime-slayer.com/wp-content/uploads/2023/01/132161.webp",
      "Type":"النوع: TV",
      "show-start":"بداية العرض: 2022",
      "anime-status":"حالة الأنمي: يعرض الان",
      "number-of-episodes":"\nعدد الحلقات:\n12 ",
      "episode-duration":"مدة الحلقة: 23 دقيقة",
      "season":"الموسم: شتاء 2023",
      "Source":"المصدر: اصلي"
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
         "name":"الحلقة 1",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D31"
      },
      {
         "number-anime":2,
         "name":"الحلقة 2",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D32"
      },
      {
         "number-anime":3,
         "name":"الحلقة 3",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D33"
      },
      {
         "number-anime":4,
         "name":"الحلقة 4",
         "id":"6172732D6E6F2D6B796F6A75752D2564382561372564392538342564382561642564392538342564392538322564382561392D34"
      }
   ],
   "servers":[
      "<class""pyanime.servers.servers"">",
      "<class""pyanime.servers.servers"">",
      "<class""pyanime.servers.servers"">",
      "<class""pyanime.servers.servers"">"
   ],
   "servers-HD":{
      "144P":"https://vd381.mycdn.me/?expires=1675014593501&srcIp=43.163.213.216&pr=10&srcAg=CHROME&ms=185.226.52.76&type=4&sig=KaWwSAlKr-s&ct=4&urls=45.136.22.18&clientType=0&id=3483106872026",
      "240P":"https://vd381.mycdn.me/?expires=1675014593501&srcIp=43.163.213.216&pr=10&srcAg=CHROME&ms=185.226.52.76&type=0&sig=X4unqb9kQd0&ct=4&urls=45.136.22.18&clientType=0&id=3483106872026",
      "360P":"https://vd381.mycdn.me/?expires=1675014593501&srcIp=43.163.213.216&pr=10&srcAg=CHROME&ms=185.226.52.76&type=1&sig=Kbqx87vET1g&ct=4&urls=45.136.22.18&clientType=0&id=3483106872026",
      "480P":"https://vd381.mycdn.me/?expires=1675014593501&srcIp=43.163.213.216&pr=10&srcAg=CHROME&ms=185.226.52.76&type=2&sig=lDj4HDlNF7g&ct=4&urls=45.136.22.18&clientType=0&id=3483106872026",
      "720P":"https://vd381.mycdn.me/?expires=1675014593501&srcIp=43.163.213.216&pr=10&srcAg=CHROME&ms=185.226.52.76&type=3&sig=5sP8LWEG9sw&ct=4&urls=45.136.22.18&clientType=0&id=3483106872026",
      "1080P":"https://vd381.mycdn.me/?expires=1675014593501&srcIp=43.163.213.216&pr=10&srcAg=CHROME&ms=185.226.52.76&type=5&sig=nSw5uA5wDCA&ct=4&urls=45.136.22.18&clientType=0&id=3483106872026"
   },
   "img":[
      
   ]
}

```

* `servers` : All quality is available `144p` , `240p` ,`360p` ,`480p` , `1080p`

## Search for a specific anime
```python 

from pyanime  import search


res = search.anime("Attack on Titan").data()

print(res)

```

## anime categories 
| ar                                                | en      | id|
|------------------------------------------------------|---------------|--------|
|أطفال|children|256438256133256438256237256439253831256438256137256439253834|
|أكشن|action|256438256133256439253833256438256234256439253836|
|ألات|Machines|256438256133256439253834256438256137256438256161|
|إيتشي|Ecchi|256438256135256439253861256438256161256438256234256439253861|
|اثارة|excitement|256438256137256438256162256438256137256438256231256438256139|
|العاب|games|256438256137256439253834256438256239256438256137256438256138|
|ايسيكاي|isekai|256438256137256439253861256438256233256439253861256439253833256438256137256439253861|
|بوليسي|Police|256438256138256439253838256439253834256439253861256438256233256439253861|
|تاريخي|Historical|256438256161256438256137256438256231256439253861256438256165256439253861|
|تشويق|suspense|256438256161256438256234256439253838256439253861256439253832|
|جنون|Mad|256438256163256439253836256439253838256439253836|
|جوسي|Josie|256438256163256439253838256438256233256439253861|
|حربي|military|256438256164256438256231256438256138256439253861|
|حريم|Seraglio|256438256164256438256231256439253861256439253835|
|خارق للعادة|supernatural|2564382561652564382561372564382562312564392538322D256439253834256439253834256438256239256438256137256438256166256438256139|
|خرف|senility|256438256165256438256231256439253831|
|خيال علمي|Fiction|2564382561652564392538612564382561372564392538342D256438256239256439253834256439253835256439253861|
|دراما|drama|256438256166256438256231256438256137256439253835256438256137|
|رعب|horror|256438256231256438256239256438256138|
|رومانسي|romantic|256438256231256439253838256439253835256438256137256439253836256438256233256439253861|
|رياضي|Athlete|256438256231256439253861256438256137256438256236256439253861|
|ساموراي|samurai|256438256233256438256137256439253835256439253838256438256231256438256137256439253861|
|سحر|Charm|256438256233256438256164256438256231|
|سيارات|cars|256438256233256439253861256438256137256438256231256438256137256438256161|
|سينين|seinen|256438256233256439253861256439253836256439253861256439253836|
|شريحة من الحياة|slice of life|2564382562342564382562312564392538612564382561642564382561392D2564392538352564392538362D256438256137256439253834256438256164256439253861256438256137256438256139|
|شوجو|Shoujo|256438256234256439253838256438256163256439253838|
|شوجو اَي|shoujo ai|2564382562342564392538382564382561632564392538382D256438256137256439253865256439253861|
|شونين|shounen|256438256234256439253838256439253836256439253861256439253836|
|شونين اي|shounen a|2564382562342564392538382564392538362564392538612564392538362D256438256137256439253861|
|شياطين|demons|256438256234256439253861256438256137256438256237256439253861256439253836|
|غموض|vagueness|256438256261256439253835256439253838256438256236|
|فضائي|alien|256439253831256438256236256438256137256438256136256439253861|
|فنتازيا|fantasy|256439253831256439253836256438256161256438256137256438256232256439253861256438256137|
|فنون قتالية|fighting arts|2564392538312564392538362564392538382564392538362D256439253832256438256161256438256137256439253834256439253861256438256139|
|قوى خارقة|super powers|2564392538322564392538382564392538392D256438256165256438256137256438256231256439253832256438256139|
|كوميدي|comic|256439253833256439253838256439253835256439253861256438256166256439253861|
|محاكاة ساخرة|Parody|2564392538352564382561642564382561372564392538332564382561372564382561392D256438256233256438256137256438256165256438256231256438256139|
|مدرسي|school|256439253835256438256166256438256231256438256233256439253861|
|مصاصي دماء|Vampires|2564392538352564382562352564382561372564382562352564392538612D256438256166256439253835256438256137256438256131|
|مغامرات|Adventures|256439253835256438256261256438256137256439253835256438256231256438256137256438256161|
|موسيقي|music|256439253835256439253838256438256233256439253861256439253832256439253861|
|ميكا|mica|256439253835256439253861256439253833256438256137|
|نفسي|myself|256439253836256439253831256438256233256439253861|
|لم يعرض بعد|Not shown yet|2564392538342564392538352D2564392538612564382562392564382562312564382562362D256438256138256438256239256438256166|

### status anime
| ar | en | id |
|--------------|-----------|-----------------|
|مكتمل|complete|256439253835256439253833256438256161256439253835256439253834|
|منتهي|Finished|2564382561372564392538362564392538372564382561372564382561312D2564382561372564392538342564382561372564392538362564392538352564392538612D256439253835256438256138256439253833256438256231256438256137256439253862|
|يعرض الان|Showing now|2564392538612564382562392564382562312564382562362D256438256137256439253834256438256137256439253836|

### type anime
| ar | en | id |
|--------------|-----------|-----------------|
|Movie|Movie||Movie|
|ONA|ONA|ONA|
|OVA|OVA|OVA|
|Special|Special|Special|
|TV|TV|TV|

### type anime
| ar | en | id |
|--------------|-----------|-----------------|
|Movie|Movie||Movie|
|ONA|ONA|ONA|
|OVA|OVA|OVA|
|Special|Special|Special|
|TV|TV|TV|




