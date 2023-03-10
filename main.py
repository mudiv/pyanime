from requests import get 
import bs4,json,base64,requests

class Episodes:
  def __init__(self,id =None):
    self.id =id
    self.data_anime_json={"data":{},"category":[],"episodes":[]}
  def anime(self):
    code =base64.b16decode(self.id).decode('utf-8')
    respons=requests.get("https://o.anime-slayer.com/anime/"+code).text
    html = bs4.BeautifulSoup(respons,'html.parser')
    
    data = html.findAll("div",{"class":"row display-flex"})[0]
    len_list_anime = data.findAll("div",{"class":"col-lg-3 col-md-3 col-sm-12 col-xs-12 col-no-padding col-mobile-no-padding DivEpisodeContainer"})
    title =html.findAll("h1",{"class":"anime-details-title"})[0].text	
    story_episode =html.findAll("p",{"class":"anime-story"})[0].text	
    img =html.findAll("img",{"class":"thumbnail img-responsive"})[0]["src"]	
    Type = html.findAll("div",{"class":"anime-info"})[0].text
    show_start=html.findAll("div",{"class":"anime-info"})[1].text
    anime_status=html.findAll("div",{"class":"anime-info"})[2].text
    number_of_episodes=html.findAll("div",{"class":"anime-info"})[3].text
    Episode_duration=html.findAll("div",{"class":"anime-info"})[4].text
    season=html.findAll("div",{"class":"anime-info"})[5].text
    Source=html.findAll("div",{"class":"anime-info"})[6].text
    teaser=html.findAll("a",{"class":"anime-trailer"})[0]["href"]
    MAL =html.findAll("a",{"class":"anime-mal"})[0]["href"]
    category =html.findAll("ul",{"class":"anime-genres"})[0]
    
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
      "Source":Source,
      
      "teaser":teaser,
      "MAL":MAL
      
    }

    self.data_anime_json["data"] = data_json
    len_dataCat =category.findAll("li")
    
    for numbers in range(len(len_dataCat)):
      
      name_category = len_dataCat[int(numbers)].text
      href_anime =len_dataCat[int(numbers)].findAll("a")[0]["href"]
      idu =href_anime.split("/")[4]
      id=base64.b16encode(idu.encode("ascii")).decode('utf-8')  
      
      data ={
        "category":name_category,
        "id": id
      }
        

      list=self.data_anime_json["category"] 
      list.append(data)
    for Numbar in range(len(len_list_anime)):
      html_code = len_list_anime[Numbar]
      img_episode = html_code.findAll("img",{"class":"img-responsive"})[0]["src"]
      numbar_episode= html_code.findAll("h3")[0].text
      name_episode = html_code.findAll("img",{"class":"img-responsive"})[0]["alt"]
      href_anime = html_code.find("a",{"class":"overlay"})["href"]
      idu =href_anime.split("/")[4]
      id=base64.b16encode(idu.encode("ascii")).decode('utf-8') 
      data ={
        "number-anime":Numbar+1,      
        "img":img_episode,
        "name":name_episode,
        "numbar-episode":numbar_episode,
        "id":id
      }
      list=self.data_anime_json["episodes"]
      list.append(data)
    return self.data_anime_json      



class list:
  def __init__(self,letter=None,Number=None,save=None):
    self.search = letter 
    self.Numbar = Number
    
    self.save = save
    self.Json ={"Numbar_list_anime":0,"data":[]}
    self.JsonPage ={"Numbar_list_anime":0,"data":[]}
    
  def page(self,Page=0):
    response = get(f"https://o.anime-slayer.com/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a7%d9%86%d9%85%d9%8a/page/{Page}").text
    
    html = bs4.BeautifulSoup(response,'html.parser')		
    len_list_anime = html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    
    for numbar in range(len(len_list_anime)):
      
      self.JsonPage["Numbar_list_anime"]+=1
      if numbar == self.Numbar :
        break
      
      # data anime 
      html_code = len_list_anime[numbar]
      img_anime = html_code.find("img",{"class":"img-responsive"})["src"]
      href_anime = html_code.find("a",{"class":"overlay"})["href"]
      status_anime = html_code.find("div",{"class":"anime-card-status"}).text
      anime_card_title =html_code.find("div",{"class":"anime-card-title"})
      anime_card_type = anime_card_title.text			
      story_anime =anime_card_title["data-content"]
      title_anime = anime_card_title["title"]
      idu =href_anime.split("/")[4]
      id=base64.b16encode(idu.encode("ascii")).decode('utf-8')  
      
			#add data anime 
      json_add={
        "number_anime":numbar,
        "img": img_anime,
        "title": title_anime,
        "story": story_anime,
        "type_tv": anime_card_type,
        "type_status": status_anime,
        "id":id
        }
      list = self.JsonPage["data"]
      
      list.append(json_add)
    if self.save:
      with open("data_anime.json","w")as f:
        json.dump(self.Json, f, indent=4)
    return self.JsonPage 
  def data(self):
    response= get(f"https://ar.anime-slayer.com/en-anime-letter/{self.search}").text
    
    html = bs4.BeautifulSoup(response,'html.parser')		
    len_list_anime = html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    for numbar in range(len(len_list_anime)):
      self.Json["Numbar_list_anime"]+=1
      if numbar == self.Numbar or self.search == None:
        break
      
      # data anime 
      html_code = len_list_anime[numbar]
      img_anime = html_code.find("img",{"class":"img-responsive"})["src"]
      href_anime = html_code.find("a",{"class":"overlay"})["href"]
      status_anime = html_code.find("div",{"class":"anime-card-status"}).text
      anime_card_title =html_code.find("div",{"class":"anime-card-title"})
      anime_card_type = anime_card_title.text			
      story_anime =anime_card_title["data-content"]
      title_anime = anime_card_title["title"]
      idu =href_anime.split("/")[4]
      id=base64.b16encode(idu.encode("ascii")).decode('utf-8')  
      
			#add data anime 
      json_add={
        "number_anime":numbar,
        "img": img_anime,
        "title": title_anime,
        "story": story_anime,
        "type_tv": anime_card_type,
        "type_status": status_anime,
        "id":id
        }
      list = self.Json["data"]
      list.append(json_add)
    if self.save:
      with open("data_anime.json","w")as f:
        json.dump(self.Json, f, indent=4)
    return self.Json







