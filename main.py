import requests

def connect(page: int) -> dict:
	payload = {
		"limit" : 100,
		"page" : page
	}
	response = requests.get("https://eztv.ag/api/get-torrents", params= payload)
	return response.json()

def get_data(response: dict)-> dict:
	torrents = list()
	for torrent in response["torrents"]:
		torrent_info = {
			"magnet" : torrent["magnet_url"],
			"title" : torrent["title"],
			"file_name" : torrent["filename"],
		}
		torrents.append(torrent_info)
	return torrents
if __name__ == "__main__":
	torrents = list()

	for page in range(1,698):
		response = connect(page= page)
		new_torrents = get_data(response=response)
		torrents.extend(new_torrents)
		print(str(len(new_torrents)) + " torrents added")
		print("Next page: " + str(page + 1))
	import json
	with open("magnets.json", "w+") as file:
		json.dump(torrents,file)
