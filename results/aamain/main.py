import requests
import time
from colorama import init, Fore
import os

init(autoreset=True)

SOCIAL = {
    "Instagram": "https://instagram.com/{}",
    "Facebook": "https://facebook.com/{}",
    "Twitter/X": "https://x.com/{}",
    "TikTok": "https://tiktok.com/@{}",
    "LinkedIn": "https://linkedin.com/in/{}",
    "Pinterest": "https://pinterest.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "Tumblr": "https://{}.tumblr.com",
    "VK": "https://vk.com/{}",
    "Weibo": "https://weibo.com/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Dev.to": "https://dev.to/{}",
    "CodePen": "https://codepen.io/{}",
    "HackerRank": "https://hackerrank.com/{}",
    "LeetCode": "https://leetcode.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Epic Games": "https://epicgames.com/id/{}",
    "Xbox": "https://xboxgamertag.com/search/{}",
    "PlayStation": "https://psnprofiles.com/{}",
    "Twitch": "https://twitch.tv/{}",
    "Discord": "https://discord.com/users/{}",
    "Roblox": "https://roblox.com/users/{}",
    "YouTube": "https://youtube.com/@{}",
    "Vimeo": "https://vimeo.com/{}",
    "Dailymotion": "https://dailymotion.com/{}",
    "Imgur": "https://imgur.com/user/{}",
    "Flickr": "https://flickr.com/people/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "Last.fm": "https://last.fm/user/{}",
    "Quora": "https://quora.com/profile/{}",
    "Medium": "https://medium.com/@{}",
    "Wikipedia": "https://en.wikipedia.org/wiki/User:{}",
    "Fiverr": "https://fiverr.com/{}",
    "Upwork": "https://upwork.com/freelancers/{}",
    "Etsy": "https://etsy.com/people/{}",
    "Kickstarter": "https://kickstarter.com/profile/{}",
    "Patreon": "https://patreon.com/{}",
    "DeviantArt": "https://{}.deviantart.com",
    "Behance": "https://behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Slack": "https://{}.slack.com",
    "Telegram": "https://t.me/{}",
    "Signal": "https://signal.me/#p/{}",
    "Keybase": "https://keybase.io/{}",
    "ReverbNation": "https://reverbnation.com/{}",
    "Mixcloud": "https://mixcloud.com/{}",
    "Goodreads": "https://goodreads.com/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Trakt": "https://trakt.tv/users/{}",
    "Tinder": "https://tinder.com/@{}",
    "Bumble": "https://bumble.com/@{}",
    "OkCupid": "https://okcupid.com/profile/{}",
    "Meetup": "https://meetup.com/members/{}",
    "Nextdoor": "https://nextdoor.com/{}",
    "Venmo": "https://venmo.com/{}",
    "CashApp": "https://cash.app/${}",
    "PayPal": "https://paypal.me/{}",
    "OnlyFans": "https://onlyfans.com/{}",
    "Fansly": "https://fansly.com/{}",
    "Slideshare": "https://slideshare.net/{}",
    "SpeakerDeck": "https://speakerdeck.com/{}",
    "HubPages": "https://hubpages.com/@{}",
    "Blogger": "https://{}.blogspot.com",
    "WordPress": "https://{}.wordpress.com",
    "Substack": "https://{}.substack.com",
    "Ghost": "https://{}.ghost.io",
    "Gumroad": "https://gumroad.com/{}",
    "ProductHunt": "https://producthunt.com/@{}",
    "AngelList": "https://angel.co/u/{}",
    "Crunchbase": "https://crunchbase.com/person/{}",
    "About.me": "https://about.me/{}",
    "Linktree": "https://linktr.ee/{}",
    "Carrd": "https://{}.carrd.co",
    "Notion": "https://notion.so/{}",
    "Scribd": "https://scribd.com/{}",
    "Issuu": "https://issuu.com/{}",
    "Blurb": "https://blurb.com/user/{}",
    "Kofi": "https://ko-fi.com/{}",
    "BuyMeACoffee": "https://buymeacoffee.com/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Replit": "https://replit.com/@{}",
    "Glitch": "https://glitch.com/@{}",
    "Codrops": "https://tympanus.net/codrops/author/{}",
    "Codier": "https://codier.io/{}",
    "CodeSandbox": "https://codesandbox.io/u/{}",
    "Gravatar": "https://gravatar.com/{}",
    "HackerOne": "https://hackerone.com/{}",
    "Bugcrowd": "https://bugcrowd.com/{}",
    "TryHackMe": "https://tryhackme.com/p/{}",
    "HackTheBox": "https://app.hackthebox.com/profile/{}",
    "Riot Games": "https://playvalorant.com/{}",
    "Fortnite": "https://fortnitetracker.com/profile/all/{}",
    "Minecraft": "https://namemc.com/profile/{}",
    "Wattpad": "https://wattpad.com/user/{}",
    "Fanfiction": "https://fanfiction.net/u/{}",
    "ArchiveOfOurOwn": "https://archiveofourown.org/users/{}",
    "Instructables": "https://instructables.com/member/{}",
    "Duolingo": "https://duolingo.com/profile/{}",
    "Khan Academy": "https://khanacademy.org/profile/{}",
    "Coursera": "https://coursera.org/user/{}",
    "Udemy": "https://udemy.com/user/{}",
    "Chess.com": "https://chess.com/member/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Strava": "https://strava.com/athletes/{}",
    "MyFitnessPal": "https://myfitnesspal.com/profile/{}",
    "Untappd": "https://untappd.com/user/{}",
    "RateBeer": "https://ratebeer.com/user/{}",
    "BeReal": "https://bere.al/{}",
    "VSCO": "https://vsco.co/{}",
    "Picsart": "https://picsart.com/u/{}",
    "500px": "https://500px.com/p/{}",
    "Smule": "https://smule.com/{}",
    "Resso": "https://resso.com/profile/{}",
    "Gaana": "https://gaana.com/user/{}",
    "JioSaavn": "https://jiosaavn.com/user/{}",
    "Anilist": "https://anilist.co/user/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "Kitsu": "https://kitsu.io/users/{}",
    "IMDb": "https://imdb.com/user/{}",
    "RottenTomatoes": "https://rottentomatoes.com/user/{}",
    "Trakt": "https://trakt.tv/users/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Goodreads": "https://goodreads.com/{}"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(f"\n{Fore.CYAN}┌─────────────────────────────────────────┐")
    print(f"{Fore.CYAN}│          {Fore.WHITE}S O C I A L   L E A K          {Fore.CYAN}│")
    print(f"{Fore.CYAN}└─────────────────────────────────────────┘\n")

def username_exists(username, url):
    try:
        response = requests.get(url.format(username), timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def print_progress_bar(current, total, bar_length=32):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = f"{Fore.CYAN}{'▰' * filled_length}{Fore.WHITE}{'▱' * (bar_length - filled_length)}"
    percent_display = f"{int(percent * 100)}%"
    print(f"{Fore.CYAN}[{bar}{Fore.CYAN}]{Fore.WHITE} ({percent_display})", end='\r')

def scan_platforms(username):
    found = []
    total = len(SOCIAL)
    print(f"\n{Fore.WHITE}Searching for {Fore.YELLOW}@{username}\n")
    start = time.time()
    for idx, (name, url) in enumerate(SOCIAL.items(), 1):
        exists = username_exists(username, url)
        if exists:
            found.append((name, url.format(username)))
        print_progress_bar(idx, total)
        time.sleep(0.1)
    print()
    duration = time.time() - start
    return found, duration

def print_results(found, duration, username):
    print(f"\n{Fore.CYAN}╭─ SCAN RESULTS {'─'*33}")
    if found:
        print(f"{Fore.WHITE}  Accounts found for {Fore.YELLOW}@{username}{Fore.WHITE}:\n")
        max_len = max(len(name) for name, _ in found)
        for i, (name, url) in enumerate(found, 1):
            print(f"  {Fore.GREEN}[{i}]{Fore.CYAN} {name.ljust(max_len)}{Fore.WHITE}: {url}")
    else:
        print(f"\n{Fore.RED}  No accounts found for @{username}")
    print(f"{Fore.CYAN}╰{'─'*45}")
    print()

def save_results(username, found):
    if not found:
        print(f"{Fore.YELLOW}No results to save.")
        return
    choice = input(f"{Fore.WHITE}Do you want to save the results to a file? {Fore.YELLOW}(y/n): {Fore.WHITE}").strip().lower()
    if choice == "y":
        os.makedirs("results", exist_ok=True)
        filename = f"results/{username}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for name, url in found:
                f.write(f"{name}: {url}\n")
        print()
        print(f"{Fore.GREEN}Results saved in {filename}")
    else:
        print(f"{Fore.RED}Results not saved.")

def main():
    while True:
        clear_screen()
        show_banner()
        username = input(f"{Fore.CYAN}┌─({Fore.YELLOW}Username{Fore.CYAN})\n└─▶{Fore.WHITE} ").strip()
        if not username:
            choice = input(
                f"{Fore.WHITE}Do you want to exit? {Fore.YELLOW}(y/n){Fore.YELLOW}){Fore.WHITE} to quit: "
            ).strip().lower()
            if choice in ["exit", "n", "no", ""]:
                print(f"{Fore.YELLOW}Exiting the program. Goodbye!")
                break
            else:
                continue
        found, duration = scan_platforms(username)
        print_results(found, duration, username)
        save_results(username, found)
        print()
        choice = input(
            f"{Fore.WHITE}Do you want to search again? {Fore.YELLOW}(y/n){Fore.WHITE}: "
        ).strip().lower()
        if choice in ["n", "no", "exit", ""]:
            print(f"{Fore.YELLOW}Exiting the program.")
            break

if __name__ == "__main__":
    main()
