import requests,bs4,base64


class anime:
	def __init__(self,value=False,save=False):
		self.save=save
		if value:			
			self.url =requests.get(f"https://ar.anime-slayer.com/?search_param=animes&s={value}").text	
			
	def data(self):
		self.html = bs4.BeautifulSoup(self.url,'html.parser')				
		self.len_list_anime = self.html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
		self.number_list_anime = len(self.len_list_anime)
		self.data_json = [{"Numbar_list_anime":self.number_list_anime,"listAnime": []}]
		for numbar in range(self.number_list_anime):
			
			self.html_code = self.html.findAll("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})[numbar]
			self.img_anime = self.html_code.find("img",{"class":"img-responsive"})["src"]		
			self.href_anime = self.html_code.find("a",{"class":"overlay"})["href"]
			self.status_anime = self.html_code.find("div",{"class":"anime-card-status"}).text
			self.anime_card_type = self.html_code.find("div",{"class":"anime-card-type"}).text				
			self.anime_card_title =self.html_code.find("div",{"class":"anime-card-title"})			
			self.story_anime =self.anime_card_title["data-content"]
			self.title_anime = self.anime_card_title["title"]
			idu =self.href_anime.split("/")[4]
			id=base64.b16encode(idu.encode("ascii")).decode('utf-8')  
      
			
			self.json_add={
                "img": self.img_anime,
                "title": self.title_anime,
                "story": self.story_anime,
                "type_tv": self.anime_card_type,
                "type_status": self.status_anime,
                "id":id
            	}
			self.data_anime=self.data_json[0]["listAnime"]
			self.data_anime.append(self.json_add)
		if self.save:
			self.save_file()
		return self.data_json
	def save_file(self):	
		with open("data_anime.json", "w") as f:
			json.dump(self.data_json, f, indent=4)
		
    