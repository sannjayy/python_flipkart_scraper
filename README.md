## Scrap Data from Flipkart
Extract Product information from Flipkart. 

GitHub Repo: [https://github.com/sannjayy/python_flipkart_scraper](https://github.com/sannjayy/python_flipkart_scraper)
### Installaion
Do the following in your virtualenv:

`pip install python_flipkart_scraper`

**Import:**
```
from python_flipkart_scraper import ExtractFlipkart
```
---
**Minimal Code Example:**
```
from python_flipkart_scraper import ExtractFlipkart
url = 'FLIPKART PRODUCT URL'
product = ExtractFlipkart(url)

print("Product Title = ", product.get_title())
print("Product Price = ", product.get_price())
print("Availability = ", product.is_available())

print("Product Images = ", product.get_images())
```

---

**DEMO OUTPUT:**


```
Product Title = APPLE iPhone 7 (Rose Gold, 128 GB)
Product Price = 34900
Availability = False

Product Images = ['https://rukminim2.flixcart.com/image/500/500/k12go7k0/mobile/e/y/z/apple-iphone-7-mn952hn-a-original-imafkqe8ptsnpd6m.jpeg?q=100', 'https://rukminim2.flixcart.com/image/500/500/k12go7k0/mobile/e/y/z/apple-iphone-7-mn952hn-a-original-imafkqe8f9ghcfsh.jpeg?q=100', 'https://rukminim2.flixcart.com/image/500/500/k12go7k0/mobile/e/y/z/apple-iphone-7-mn952hn-a-original-imafkqe8ywuhzqyc.jpeg?q=100', 'https://rukminim2.flixcart.com/image/500/500/k12go7k0/mobile/e/y/z/apple-iphone-7-mn952hn-a-original-imafkqe8ujhbszhf.jpeg?q=100']
```

---

[![](https://img.shields.io/github/followers/sannjayy?style=social)](https://github.com/sannjayy)  
Developed by *Sanjay Sikdar*.   
- 📫 me@sanjaysikdar.dev



