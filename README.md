# image-search
Using Google's Custom Search API to download image results. 

Get your API Key for Custom Search API here : https://developers.google.com/custom-search/v1/introduction

Get your Programmable Search Engine ID here : https://cse.google.com/all

Usage : 
1. Replace secretkey with your API Key
2. Replace secretcx with your programmable search engine ID.
3. Replace path with absolute/relative path of preferred download location.
4. Run the script with arguments:  query and number of results required(number of images to download)

  for example $ python imagerequest.py Cats 100
  
Custom Search JSON API provides 100 search queries per day for free. If you need more, you may sign up for billing in the API Console. Additional requests cost $5 per 1000 queries, up to 10k queries per day.
Every query contains 10 results so you can download upto 1000 images in a day for free.
