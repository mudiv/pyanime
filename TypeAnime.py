import requests,bs4,base64

class sort:
  def __init__(self,numbar=None):
    self.Numbar =numbar
    self.json ={"Numbar_list_anime":0,"data":[]}
  def category(self,idu):
    """
    idu:
      مترجم :(2564382561372564392538342564382561372564392538362564392538352564392538612D256438256137256439253834256439253835256438256161256438256231256438256163256439253835)
      مدبلج :(2564382561372564392538342564382561372564392538362564392538352564392538612D256438256137256439253834256439253835256438256166256438256138256439253834256438256163)
    """
    id=base64.b16decode(idu).decode('utf-8')
    response =requests.get(f"https://o.anime-slayer.com/anime-category/{id}").text
    html = bs4.BeautifulSoup(response,'html.parser')
    len_list_anime = html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    
    for numbar in range(len(len_list_anime)):
      
      self.json["Numbar_list_anime"]+=1
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
      list = self.json["data"]
      list.append(json_add)
    return self.json        
  def status(self,idu):
    """ 
    idu:
    لم يعرض بعد :(2564392538342564392538352D2564392538612564382562392564382562312564382562362D256438256138256438256239256438256166)
    مكتمل :(256439253835256439253833256438256161256439253835256439253834)
    منتهي :(2564382561372564392538362564392538372564382561372564382561312D2564382561372564392538342564382561372564392538362564392538352564392538612D256439253835256438256138256439253833256438256231256438256137256439253862)
    يعرض الآن:(2564392538612564382562392564382562312564382562362D256438256137256439253834256438256137256439253836)
    """
    id=base64.b16decode(idu).decode('utf-8')
    response =requests.get(f"https://o.anime-slayer.com/anime-status/{id}").text
    html = bs4.BeautifulSoup(response,'html.parser')
    len_list_anime = html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    
    for numbar in range(len(len_list_anime)):
      
      self.json["Numbar_list_anime"]+=1
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
      list = self.json["data"]
      list.append(json_add)
    return self.json        
  def type(self,id):
    """ 
      id:
        movie,
        ova,
        ona,
        tv,
        special
    """
    
    response =requests.get(f"https://o.anime-slayer.com/anime-type/{id}").text
    html = bs4.BeautifulSoup(response,'html.parser')
    len_list_anime = html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    
    for numbar in range(len(len_list_anime)):
      
      self.json["Numbar_list_anime"]+=1
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
      list = self.json["data"]
      list.append(json_add)
    return self.json      
  def genre(self,idu):
    id=base64.b16decode(idu).decode('utf-8')
    response =requests.get(f"https://o.anime-slayer.com/anime-genre/{id}").text
    html = bs4.BeautifulSoup(response,'html.parser')
    len_list_anime = html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    
    for numbar in range(len(len_list_anime)):
      
      self.json["Numbar_list_anime"]+=1
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
      list = self.json["data"]
      list.append(json_add)
    return self.json    