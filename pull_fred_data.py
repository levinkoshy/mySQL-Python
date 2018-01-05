import requests

gdpc_url = "https://api.stlouisfed.org/fred/series/observations?series_id=GDPC1&api_key=05bcb4f13945e4bfc8bde23012cb666b&file_type=txt"
umcsent_url = "https://api.stlouisfed.org/fred/series/observations?series_id=UMCSENT&api_key=05bcb4f13945e4bfc8bde23012cb666b&file_type=txt"
umrate_url = "https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key=05bcb4f13945e4bfc8bde23012cb666b&file_type=txt"

# pull gdpc data
gdpc_request = requests.get("https://api.stlouisfed.org/fred/series/observations?series_id=GDPC1&api_key=05bcb4f13945e4bfc8bde23012cb666b&file_type=txt")
gdpc_filer = open("gdpc1.txt.zip","wb")
gdpc_filer.write(gdpc_request.content)
gdpc_filer.close()

# pul umcsent data
umcsent_request = requests.get("https://api.stlouisfed.org/fred/series/observations?series_id=UMCSENT&api_key=05bcb4f13945e4bfc8bde23012cb666b&file_type=txt")
umcsent_filer = open("umcsent.txt.zip","wb")
umcsent_filer.write(umcsent_request.content)
umcsent_filer.close()

# pull umrate data
umrate_request = requests.get("https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key=05bcb4f13945e4bfc8bde23012cb666b&file_type=txt")
umrate_filer = open("umrate.txt.zip","wb")
umrate_filer.write(umrate_request.content)
umrate_filer.close()

