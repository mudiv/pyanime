import requests,bs4,base64
from .servers import servers 

class watch:
  def __init__(self,id):
    self.id =id
    self.data_anime_json={"data":{},"category":[],"episodes":[],"servers":[],"servers-HD":{},"img":[]}
  def data(self):
    Base=base64.b16decode(self.id).decode('utf-8')
    response = requests.get("https://o.anime-slayer.com/episode/"+Base).text
    html = bs4.BeautifulSoup(response,'html.parser')
    
    title= html.findAll("meta",{"name":"description"})[0]["content"]
    img=html.findAll("img",{"class":"thumbnail img-responsive"})[0]["src"]
    story_episode =html.findAll("p",{"class":"anime-story"})[0].text
    Type = html.findAll("div",{"class":"anime-info"})[0].text
    show_start=html.findAll("div",{"class":"anime-info"})[1].text
    anime_status=html.findAll("div",{"class":"anime-info"})[2].text
    number_of_episodes=html.findAll("div",{"class":"anime-info"})[3].text
    Episode_duration=html.findAll("div",{"class":"anime-info"})[4].text
    season=html.findAll("div",{"class":"anime-info"})[5].text
    Source=html.findAll("div",{"class":"anime-info"})[6].text
    data_json ={
      "title":title,
      "story-episode":story_episode,
      "img":img,
      "Type":Type,
      "show-start":show_start,
      "anime-status":anime_status,
      "number-of-episodes":number_of_episodes,
      "episode-duration":Episode_duration,
      "season":season,
      "Source":Source
      
    }
    self.data_anime_json["data"] = data_json
    category =html.findAll("ul",{"class":"anime-genres"})[0]
    len_dataCat =category.findAll("li")
    for numbers in range(len(len_dataCat)):
      name_category = len_dataCat[int(numbers)].text
      href_anime =len_dataCat[int(numbers)].findAll("a")[0]["href"]
      idu =href_anime.split("/")[4]
      id=base64.b16encode(idu.encode("ascii")).decode('utf-8')  
      data ={
        "category":name_category,
        "id":id
      }
      list=self.data_anime_json["category"]
      list.append(data)
    Category = html.findAll("ul",{"class":"all-episodes-list scroll-episodes-list"})[0]
    len_Category =Category.findAll("li")
    for number in range(len(len_Category)):
        #print(Category) # 2022/5/11 (: by ruks 
      data = Category.findAll("li")[number]
      name = data.text
      href_anime = data.findAll("a")[0]["href"]
      idu =href_anime.split("/")[4]
      id=base64.b16encode(idu.encode("ascii")).decode('utf-8') 
      data ={
          "number-anime":number +1,      
          "name":name,
          "id":id
        }
      list=self.data_anime_json["episodes"]
      list.append(data)
      serverurl = html.findAll("ul",{"class":"nav nav-tabs"})[0]
      for number in range(len(serverurl)-2):
       # print(serverurl)
        url = serverurl.findAll("li")[number].findAll("a")[0]["data-ep-url"]
        server,img,HD=servers(url).get()
        
        if HD !={}:
          
          list=self.data_anime_json["servers-HD"] = HD
        if img !=[]:
          list=self.data_anime_json["img"]
          for i in img:
            
            list.append(i)
        
        if server !=[]:
          list=self.data_anime_json["servers"]
          
          list.append(servers)
          
        
        
    return self.data_anime_json
    
    
    
    
    
    
    
    
    
