import requests
import time
from colorama import init, Fore
import os

init(autoreset=True)

SOCIAL = {
    "Instagram": "https://instagram.com/{}",
    "Facebook": "https://facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "LinkedIn": "https://linkedin.com/in/{}",
    "TikTok": "https://tiktok.com/@{}",
    "YouTube": "https://youtube.com/@{}",
    "Reddit": "https://reddit.com/user/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Xbox": "https://account.xbox.com/en-us/profile?gamertag={}",
    "PlayStation": "https://my.playstation.com/profile/{}",
    "Twitch": "https://twitch.tv/{}",
    "Epic Games": "https://www.epicgames.com/id/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Deezer": "https://www.deezer.com/profile/{}",
    "Bandcamp": "https://bandcamp.com/{}"
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