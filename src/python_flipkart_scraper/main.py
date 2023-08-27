import requests, re
from bs4 import BeautifulSoup as bs

headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

class ExtractFlipkart:
    def __init__(self, url):
        url = url
        page = requests.get(url, headers=headers)
        soup = bs(page.content, "lxml")
        self.soup = soup

    # Function to extract Product Title
    def get_title(self):
        try:
            title = self.soup.select_one("h1").find('span').text
            title_string = re.sub("   +", " ", title)

        except AttributeError:
            title_string = ""	
        return title_string

    # Function to extract Product Price
    def get_price(self):
        
        try:
            price = self.soup.select_one('#container>div>div:nth-child(3)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(3)>div:nth-child(1)>div>div:nth-child(1)').text.strip()
        except AttributeError:  
            try:
                price = self.soup.select_one('#container>div>div:nth-child(3)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(4)>div>div>div:nth-child(1)').text.strip()
            except AttributeError:
                price = ''
        return price.replace('₹', '').replace(',', '')

    # Function to extract Product Rating
    def get_rating(self):
        try:
            rating = self.soup.select_one("#container>div>div:nth-child(3)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div>div:nth-child(2)>div>div>span>div")
            rating = rating.contents[0]
        except AttributeError:
            rating = ""	

        return rating

    # Function to extract Availability Status
    def is_available(self):
        try:
            sold_out = self.soup.select_one('#container>div>div:nth-child(3)>div:nth-child(1)>div:nth-child(2)>div:nth-child(3)>div:nth-child(1)')
            sold_out = sold_out.text.strip()
            return sold_out != 'Sold Out'
        except AttributeError as e:
            print(e)
            return True	
    

    # Function to extract images [ul>li>div>div>img]
    def get_images(self, width=500, height=500, quality=100):
        try:
            images = self.soup.select('ul>li>div>div>img')
            images_list = []
            for image in images:
                image_src = image['src']
                image_src = image_src.replace('?q=70', f'?q={quality}')
                image_src = image_src.replace('image/128/128', f'image/{width}/{height}')
                images_list.append(image_src)
            return images_list
        
        except AttributeError:
            return False
    
    

