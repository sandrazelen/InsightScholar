import requests 
import bs4 
  
text= "graph theory with metro networks"
url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C33&q=' + text

request_result=requests.get( url ) 
  
main_search = bs4.BeautifulSoup(request_result.text, "html.parser") 
#print(main_search)
heading_object=main_search.find_all( 'h3' ) 

for info in heading_object: 
    title = info.getText()
    link = info.find('a')['href']
    print(title)
    print(link)
    
    paper = requests.get(link) 

    paper_content_page = bs4.BeautifulSoup(paper.text, "html.parser") 
    print(paper_content_page)
