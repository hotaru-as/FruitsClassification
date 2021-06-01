from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報
key = sys.argv[1]
secret = sys.argv[2]
wait_time = 1

flickr = FlickrAPI(key, secret, format='parsed-json')

fruits = ['apple', 'cherry', 'grape']

for fruit in fruits:
  savedir = "./" + fruit
  if os.path.exists(savedir):
    os.makedirs(savedir)
  
  result = flickr.photos.search(
    text = fruit,
    per_page = 600,
    media = 'photos',
    sort = 'relevance',  # 関連順に並べる
    safe_search = 1,
    extras = 'url_q, licence'
  )

  photos = result['photos']
  # pprint(photos)

  for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):
      continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)

