import requests,bs4



class servers:
  def __init__(self,id):
    self.id =id
  def get(self):
    list = []
    img = []
    HD ={}
    if "4shared" in self.id:
      
      try:
        respons = requests.get(self.id)
        html = bs4.BeautifulSoup(respons,'html.parser')	
        mp4 = html.find("source")["src"]
        list.append(mp4)
      except:
        pass
    if "ok.ru" in self.id:
      
      idok =self.id.split("/")[4]
      respons = requests.get(f"https://www.videofk.com/ok.ru-video-download/search?url=http://ok.ru/video/{idok}&select=ok.ru").text
      html = bs4.BeautifulSoup(respons,'html.parser')
      mp4= html.findAll("div",{"class":"video_files"})[0]
      len_a =mp4.findAll("a")
      for i in range(len(len_a)):
        url=len_a[i]["download"].replace(";","&")
        Pt=len_a[i].text.split(" ")[1]
        HD[str(Pt)] = url
      
        
    
    if "vadbam" in self.id:
      
      try:
        respons = requests.get(self.id).text
        html = bs4.BeautifulSoup(respons,'html.parser')	
        url =html.findAll("script")[7].text[52:142]
        if "https:" in url:
          list.append(url)
      except:
        pass
    if "vidshar" in self.id:
      
      respons = requests.get(self.id)
      html= bs4.BeautifulSoup(respons,'html.parser')
      sp = html.findAll("script").text[52:170]
      url = sp.split('"')[0]
      list.append(url)
      img =html.findAll("script")[7].text[181:250].split('"')[0]
      img.append(img)
    return list,img,HD
      
      
      




      