import requests
from rich.progress import track
from colorama import Fore, init

init(autoreset=True)

# === SITES TO SCAN ===
SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Medium": "https://medium.com/@{}",
    "YouTube": "https://www.youtube.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Keybase": "https://keybase.io/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "About.me": "https://about.me/{}",
    "Codepen": "https://codepen.io/{}",
    "Repl.it": "https://replit.com/@{}",
    "HackerOne": "https://hackerone.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Blogger": "https://{}.blogspot.com",
    "500px": "https://500px.com/{}",
    "OK.ru": "https://ok.ru/{}",
    "VK": "https://vk.com/{}",
    "AskFM": "https://ask.fm/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def check(username, url_template):
    try:
        url = url_template.format(username)
        res = requests.get(url, headers=HEADERS, timeout=5)
        if res.status_code == 200:
            return True, url
        else:
            return False, url
    except:
        return False, url_template.format(username)

def scan_username(username):
    print(Fore.CYAN + f"\n[~] Scanning username: {username}\n")
    for site, url_template in track(SITES.items(), description="[yellow]Checking sites..."):
        found, url = check(username, url_template)
        if found:
            print(f"{Fore.GREEN}[+] {site}: {url}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}[-] {site}: Not found")

if __name__ == "__main__":
    user = input(Fore.CYAN + " 🦈 Enter username to scan: ").strip()
    if user:
        scan_username(user)
    else:
        print(Fore.RED + "Username can't be empty.")
