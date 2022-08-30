import os, requests, random, json, threading
from colorama import Fore

email = [
	"fbi.gov",
	"supremecourt.gov",
	"gmail.com",
	"yahoo.com",
	"discord.com",
	"spotify.com",
	"mail.com",
]

url = "https://spclient.wg.spotify.com/signup/public/v2/account/create"


os.system("cls && title Spotify AIO")


def center(var: str, space: int = None):  # From Pycenter
	if not space:
		space = (
			os.get_terminal_size().columns
			- len(var.splitlines()[int(len(var.splitlines()) / 2)])
		) / 2

	return "\n".join((" " * int(space)) + var for var in var.splitlines())


class AIO:
	def GetEmail():
		semail = str(random.randint(11111111, 99999999)) + "@" + random.choice(email)
		return semail

	def GetGender():
		genders = ["Female", "Male"]
		return random.choice(genders)

	def CreateAccount():
		with open("proxies.txt", encoding="utf-8") as f:
			proxies = [i.strip() for i in f]
		working = 0
		notworking = 0
		while True:
			proxy = random.choice(proxies)
			os.system(f"title [+] Created Accounts: {working}")
			napkin = AIO.GetEmail()
			password = str(random.randint(11111111, 99999999))
			payload = json.dumps(
				{
					"account_details": {
						"birthdate": "1999-09-02",
						"consent_flags": {
							"eula_agreed": True,
							"send_email": True,
							"third_party_email": False,
						},
						"display_name": "AIO",
						"email_and_password_identifier": {
							"email": napkin,
							"password": password,
						},
						"gender": 1,
					},
					"callback_uri": "https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=uk",
					"client_info": {
						"api_key": "a1e486e2729f46d6bb368d6b2bcda326",  # Stay
						"app_version": "v2",
						"capabilities": [1],
						"installation_id": "",
						"platform": "www",
					},
					"tracking": {
						"creation_flow": "",
						"creation_point": "https://www.spotify.com/uk/",
						"referrer": "",
					},
				}
			)
			xxx = requests.post(
				url, data=payload, proxies={"http": "http" + "://" + proxy}
			)
			if xxx.status_code == 200:
				print(
					center(
						f"{Fore.GREEN} [Created] {napkin}:{password} {Fore.YELLOW}Gender: {AIO.GetGender()} {Fore.RED}PROXY: {proxy} {Fore.RESET}"
					)
				)
				working += 1
			else:
				print(center(f" {Fore.RED} [-] {napkin} {Fore.RESET}"))
				notworking += 1


if __name__ == "__main__":
	print(
		center(
			f"""\n\n
		{Fore.LIGHTGREEN_EX}    
  ██████  ██▓███   ▒█████  ▄▄▄█████▓ ██▓  █████▒▓██   ██▓
▒██    ▒ ▓██░  ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██▒▓██   ▒  ▒██  ██▒
░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒ ▓██░ ▒░▒██▒▒████ ░   ▒██ ██░
  ▒   ██▒▒██▄█▓▒ ▒▒██   ██░░ ▓██▓ ░ ░██░░▓█▒  ░   ░ ▐██▓░
▒██████▒▒▒██▒ ░  ░░ ████▓▒░  ▒██▒ ░ ░██░░▒█░      ░ ██▒▓░
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░   ▒ ░░   ░▓   ▒ ░       ██▒▒▒ 
░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░     ░     ▒ ░ ░       ▓██ ░▒░ 
░  ░  ░  ░░       ░ ░ ░ ▒    ░       ▒ ░ ░ ░     ▒ ▒ ░░  
      ░               ░ ░            ░           ░ ░     
                                                 ░ ░     
		{Fore.RESET}  
															
              Spotify Account Generator
			  © Working 2022
		
		"""
		))

	try: 
		x = input(" Threads ~ ")
		t = []
		for x in range(int(x) + 1):
			thread = threading.Thread(target=AIO.CreateAccount(),daemon=False)
			t.append(thread)
			thread.start()
		for thread in t:
			thread.join()

	except (KeyboardInterrupt,ValueError):
		print("~ Stopped")
