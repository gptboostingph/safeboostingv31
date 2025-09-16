import os
import random
import string
import uuid
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import requests
import json
import sys
import os
import platform
import re
import threading
import requests as rq
import requests as rq
import threading
from concurrent.futures import ThreadPoolExecutor
import time, random

# Softer ANSI colors
blue = "\033[34m"     # dark blue
red = "\033[31m"      # dark red
yellow = "\033[33m"   # dark yellow
green = "\033[32m"    # green
reset = "\033[0m"
orange = "\033[38;5;208m"  # candy-orange-like
file_lock = threading.Lock()
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
SKYBLUE = "\033[1;36m"
BLUE = "\033[1;34m"
LIGHTBLUE = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
WHITE = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
DARKBLUE = "\033[34m"
GREEN = "\033[1;32m"
white = "\033[1;37m"
# Define colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def clear_screen():
    # Works on Windows and Unix, and clears scrollback buffer
    if os.name == 'nt':
        os.system('cls')
        print("\033[3J", end='')  # clears scrollback buffer in Windows terminal
    else:
        os.system('clear')
        print("\033[3J", end='')  # clears scrollback buffer in Unix terminal
def logo():
    clear_screen()
    logo = [
        "       ███████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗       ",
        "       ██╔════╝ ██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║       ",
        "       █████╗   ██████╔╝       ██║   ██║   ██║██║   ██║██║       ",
        "       ██╔══╝   ██╔══██╗       ██║   ██║   ██║██║   ██║██║       ",
        "       ██║      ██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗   ",
        "       ╚═╝      ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝   "
    ]

    contact = "Contact: @SafeBoosting | Telegram: t.me/SafeBoosting"

    # compute box width based on longest line
    box_width = max(len(line) for line in logo + [contact]) + 4  # some padding

    print("╔" + "═" * box_width + "╗")
    print("║" + " " * box_width + "║")

    for line in logo:
        # center each line inside the box
        print("║" + line.center(box_width) + "║")

    print("║" + " " * box_width + "║")
    print("║" + contact.center(box_width) + "║")
    print("╚" + "═" * box_width + "╝")

def show_account():
    """
    Ensure account/page files exist, count their entries, 
    and display an overview with the logo.
    """
    # Paths of the files
    paths = {
        "FRA_ACCOUNT": '/sdcard/boostphere/FRAACCOUNT.txt',
        "FRA_PAGES": '/sdcard/boostphere/FRAPAGES.txt',
        "RPW_ACCOUNT": '/sdcard/boostphere/RPWACCOUNT.txt',
        "RPW_PAGES": '/sdcard/boostphere/RPWPAGES.txt'
    }

    # Ensure files exist
    for path in paths.values():
        open(path, 'a').close()

    # Count accounts/pages
    total_accounts, total_pages = count_tokens(paths["FRA_ACCOUNT"], paths["FRA_PAGES"])
    total_account_rpw, total_pages_rpw = count_tokens(paths["RPW_ACCOUNT"], paths["RPW_PAGES"])

    # Display
    print_overview()
    print(f"""
                 OVERVIEW OF STORED ACCOUNT & PAGES💫
          
                            FRA ACCOUNT : {total_accounts}
                            FRA PAGES   : {total_pages}
                            RPW ACCOUNT : {total_account_rpw}
                            RPW PAGES   : {total_pages_rpw}
      ───────────────────────────────────────────────────────────────
    """)

    # Return counts in case needed
    return total_accounts, total_pages, total_account_rpw, total_pages_rpw

def count_tokens(accounts_file, pages_file):
    """Count the number of accounts and pages stored in the respective files."""
    total_accounts = 0
    total_pages = 0

    try:
        with open(accounts_file, 'r') as af:
            total_accounts = sum(1 for line in af if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Account file not found: {accounts_file}")

    try:
        with open(pages_file, 'r') as pf:
            total_pages = sum(1 for line in pf if line.strip())  # Count non-empty lines
    except FileNotFoundError:
        print(f"Page file not found: {pages_file}")

    return total_accounts, total_pages

def generate_user_agent():
    ua_dict = {
        "Huawei": [
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/CHA-AL80;FBSV/11;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=441,width=1200,height=2640};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ELS-NX9;FBSV/Android 10;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=422,width=1080,height=2340};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/ELE-L29;FBSV/Android 10;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=395,width=1084,height=2412};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/BLK-LX9;FBSV/HarmonyOS 4.2;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=412,width=1080,height=2340};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/YAL-L61;FBSV/Android 10;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=264,width=720,height=1604};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/MGA-LX3;FBSV/Android 12;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=538,width=1440,height=3120};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/LYA-L29;FBSV/Android 9;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=450,width=1228,height=2700};FBLC/tl_PH;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/JAD-LX9;FBSV/HarmonyOS 2.0;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=408,width=1080,height=2240};FBLC/en_US;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/CLT-L29;FBSV/Android 10;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=409,width=1080,height=2340};FBLC/en_US;FBRV/0;FBCR/Huawei;FBMF/Huawei;FBBD/Huawei;FBPN/com.facebook.katana;FBDV/INE-LX1;FBSV/Android 9;FBOP/1;FBCA/arm64-v8a]"
        ],
        "Vivo": [
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=3.0,width=1080,height=2376};FBLC/tl_PH;FBRV/0;FBCR/Smart;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/V2158;FBSV/12;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=2.5,width=720,height=1608};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/V2420;FBSV/14;FBOP/1;FBCA/arm64-v8a]"
        ],
        "Samsung": [
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=4.0,width=1440,height=3120};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-S938B;FBSV/15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=4.0,width=1440,height=3120};FBLC/tl_PH;FBRV/0;FBCR/Smart;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-S938B;FBSV/15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=3.5,width=1080,height=2340};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-S721B;FBSV/14;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=3.5,width=1080,height=2340};FBLC/tl_PH;FBRV/0;FBCR/Smart;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A566;FBSV/15;FBOP/1;FBCA/arm64-v8a]"
        ],
        "Xiaomi": [
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/POCOM7_4G;FBSV/15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/527.0.0.47.99;FBBV/777654321;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/0;FBCR/Smart;FBMF/Xiaomi;FBBD/Poco;FBPN/com.facebook.katana;FBDV/Poco M7 Plus;FBSV/15;FBOP/1;FBCA/arm64-v8a:;]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 15 4G;FBSV/15;FBOP/2;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=2.0,width=720,height=1600};FBLC/en_PH;FBRV/0;FBCR/Smart;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/25078RA3EA;FBSV/15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=396,width=1080,height=2460};FBLC/en_PH;FBRV/0;FBCR/Xiaomi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/24049RN28L;FBSV/Android 14;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=260,width=720,height=1640};FBLC/tl_PH;FBRV/0;FBCR/Xiaomi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/RedmiA5;FBSV/Android 15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=522,width=1440,height=3200};FBLC/tl_PH;FBRV/0;FBCR/Xiaomi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi15Ultra;FBSV/Android 15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=395,width=1080,height=2400};FBLC/tl_PH;FBRV/0;FBCR/Xiaomi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/RedmiNote14S;FBSV/Android 15;FBOP/1;FBCA/arm64-v8a]",
            "[FBAN/FB4A;FBAV/526.1.0.66.75;FBBV/464219463;FBDM/{density=206,width=1200,height=1920};FBLC/tl_PH;FBRV/0;FBCR/Xiaomi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/BlackSharkPad6;FBSV/Android 14;FBOP/1;FBCA/arm64-v8a]"
        ]
    }

    # Pick a random brand first
    all_uas = [ua for ua_list in ua_dict.values() for ua in ua_list]
    # Then pick a random UA from that brand
    return random.choice(all_uas)

def extract_user_id_prof(url, ua=None, access_token=None):
    """
    Extract numeric user ID from a Facebook profile URL.
    Supports numeric ID URLs and username URLs.
    If a username is used, a Graph API request is made to get numeric ID.
    """
    url = url.strip()
    
    # First, try numeric ID in profile.php?id= or ?id=
    match = re.search(r'id=(\d+)|profile\.php\?id=(\d+)', url)
    if match:
        return match.group(1) or match.group(2)
    
    # Try extracting from /{username} format
    match = re.search(r'facebook\.com/([\w\.]+)', url)
    if match:
        username = match.group(1)
        # If access_token provided, try Graph API lookup
        if access_token:
            headers = {"User-Agent": ua} if ua else {}
            try:
                resp = requests.get(f'https://graph.facebook.com/{username}?access_token={access_token}', headers=headers, timeout=10)
                data = resp.json()
                if "id" in data:
                    return data["id"]
            except Exception:
                return None
        else:
            # If no access_token, return username as fallback (won't work for reactions that need numeric ID)
            return username
    
    return None

def extract_facebook_uid_url(fb_url):
    fb_url = fb_url.strip()
    parsed = urlparse(fb_url)
    query = parse_qs(parsed.query)

    # Get comment_id if present
    comment_id = query.get("comment_id", [None])[0]

    # Case 1: /posts/{id or pfbid}/
    match = re.search(r'/posts/([\w\d]+)', fb_url)
    if match:
        post_id = match.group(1)
        if comment_id:
            return f"{post_id}_{comment_id}"
        return post_id

    # Case 2: /share/v/{code}/
    match = re.search(r'/share/v/([\w\d]+)', fb_url)
    if match:
        post_id = match.group(1)
        if comment_id:
            return f"{post_id}_{comment_id}"
        return post_id

    # Case 3: permalink.php?story_fbid=...&id=...
    if "story_fbid" in query:
        post_id = query["story_fbid"][0]
        if comment_id:
            return f"{post_id}_{comment_id}"
        return post_id

    # Case 4: numeric post ID fallback
    match = re.search(r'/(\d{10,})', fb_url)
    if match:
        post_id = match.group(1)
        if comment_id:
            return f"{post_id}_{comment_id}"
        return post_id

    return None

def get_profile_id(token_line):
    """
    Retrieve the profile or page ID.
    Supports:
      - raw access_token only
      - full 7-part format: uid|pw|access_token|cookie|device_id|secret|UA
    """
    parts = token_line.strip().split('|')

    # Case 1: raw access token only
    if len(parts) == 1 and parts[0].startswith("EAAAA"):
        access_token = parts[0]
        user_agent = "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36 Chrome/91.0.4472.77 Mobile Safari/537.36"

    # Case 2: full 7-part format
    elif len(parts) == 7:
        access_token = parts[2]
        user_agent = parts[6]

    else:
        print(f"Invalid token format: {token_line}")
        return None

    headers = {'user-agent': user_agent}

    try:
        # First try as a user
        r = requests.get("https://graph.facebook.com/me",
                         params={"access_token": access_token},
                         headers=headers)
        data = r.json()
        if "id" in data:
            return data["id"]

        # Then try as a page
        r = requests.get("https://graph.facebook.com/me/accounts",
                         params={"access_token": access_token},
                         headers=headers)
        data = r.json()
        if "data" in data and len(data["data"]) > 0:
            return data["data"][0]["id"]

    except Exception as e:
        print(f"Error in get_profile_id: {e}")

    return None
# ---------------------- Resolve pfbid to numeric ID ----------------------
def resolve_pfbid_to_numeric(post_url, ua):
    """
    Resolve a pfbid or share URL to numeric post ID.
    """
    headers = {
        "User-Agent": ua,
        "Accept": "text/html"
    }

    try:
        response = requests.get(post_url, headers=headers, timeout=10, allow_redirects=True)
        html = response.text

        # Look for numeric post ID in meta tags or JS
        match = re.search(r'/posts/(\d+)', html)
        if match:
            return match.group(1)

        match = re.search(r'"postID":"(\d+)"', html)
        if match:
            return match.group(1)

        # fallback: return original URL if not found
        return post_url

    except Exception as e:
        print(f"Error resolving pfbid: {e}")
        return post_url
    
def extract_post_ids_v1(url):
    group_pattern = r'groups/(\d+)/permalink/(\d+)/'
    post_pattern = r'(\d+)/posts/(\d+)/'
    photo_pattern = r'fbid=(\d+)'

    group_match = re.search(group_pattern, url)
    post_match = re.search(post_pattern, url)
    photo_match = re.search(photo_pattern, url)

    if group_match:
        group_id, post_id = group_match.groups()
        return f"{group_id}_{post_id}"
    elif post_match:
        group_id, post_id = post_match.groups()
        return f"{group_id}_{post_id}"
    elif photo_match:
        photo_id = photo_match.group(1)
        return photo_id
    else:
        return None 
    
def get_combined_data(url):
    """
    Fetch the response from the given URL and extract the `actrs` number and `post_id`.
    Combine these values and return the result.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: The combined string of `actrs` number and `post_id`, or an error message.
    """
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'cache-control': "max-age=0",
        'dpr': "2",
        'viewport-width': "980",
        'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Linux\"",
        'sec-ch-ua-platform-version': "\"\"",
        'sec-ch-ua-model': "\"\"",
        'sec-ch-ua-full-version-list': "\"Google Chrome\";v=\"131.0.6778.104\", \"Chromium\";v=\"131.0.6778.104\", \"Not_A Brand\";v=\"24.0.0.0\"",
        'sec-ch-prefers-color-scheme': "light",
        'upgrade-insecure-requests': "1",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "document",
        'accept-language': "en-US,en;q=0.9",
        'priority': "u=0, i",
        'Cookie': "sb=fuZTZ8Zyl9dXj5TFodlxDrGD; dpr=2; wd=980x1628; datr=fuZTZxL-gtbBjTkfeBq-VVDZ"
    }

    try:
        response = requests.get(url, headers=headers).text

        # Extract `actrs` number
        actrs_match = re.search(r'"actrs\\":\\"(\d+)\\"', response)
        actrs_number = actrs_match.group(1) if actrs_match else None

        # Extract `post_id`
        post_id_match = response.split('"post_id":"')[1].split('"')[0] if '"post_id":"' in response else None

        if actrs_number and post_id_match:
            return f"{actrs_number}_{post_id_match}"
        elif not actrs_number:
            return "actrs number not found!"
        elif not post_id_match:
            return "post_id not found!"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def extraction():
    clear_screen()
    print_overview()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        extract_account()
    elif choice == '2':
        extract_page()
    else:
        print(f"     {red}INVALID CHOICE")

def extract_account():
    clear_screen()
    print_overview()
    folder_path = "/sdcard/boostphere"
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    token_output_path = account_file

    extract_fra_logic(file_path, token_output_path, extract_type)

def extract_fra_logic(accounts_file, token_output_path, extract_type):
    """Process the accounts and extract tokens concurrently."""
    success_count = []

    # Load existing UIDs from the output file to avoid duplicates
    existing_uids = set()
    if os.path.exists(token_output_path):
        with open(token_output_path, 'r', encoding='utf-8') as f:
            existing_uids = {line.split('|')[0] for line in f if '|' in line}

    try:
        # Read accounts from input file
        with open(accounts_file, 'r', encoding='utf-8') as f:
            accounts = [line.strip() for line in f if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        def submit_account(account_line):
            parts = account_line.split('|')
            if len(parts) < 2:
                print(f"[SKIP] Invalid account line: {account_line}")
                return

            uid = parts[0]
            pw = parts[1]
            # Optional remaining fields
            access_token = parts[2] if len(parts) > 2 else ''
            extra1 = parts[3] if len(parts) > 3 else ''
            extra2 = parts[4] if len(parts) > 4 else ''
            secret = parts[5] if len(parts) > 5 else ''
            ua = parts[6] if len(parts) > 6 else ''

            account_logic(uid, pw, token_output_path, extract_type, success_count, existing_uids)

        # Process accounts concurrently
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(submit_account, acc) for acc in accounts]
            for future in futures:
                future.result()  # Wait for completion

        print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

import hashlib

def generate_sig(params, secret="62f8ce9f74b12f84c123cc23437a4a32"):
    sorted_params = "".join(f"{k}={v}" for k, v in sorted(params.items()))
    return hashlib.md5((sorted_params + secret).encode()).hexdigest()

def account_logic(uid_or_email, pw, path_file, extract_type, success_count, existing_uids):
    import requests
    ua_bgraph = generate_user_agent()
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

    headers = {
        'User-Agent': ua_bgraph,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': accessToken,
        'email': uid_or_email,
        'password': pw,
        'credentials_type': 'password',
        'method': 'auth.login',
        'format': 'json',
        'locale': 'en_US',
        'client_country_code': 'US',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'generate_session_cookies': '1',
        'generate_machine_id': '1',
        'generate_analytics_claim': '1',
        'device_id': str(uuid.uuid4()),   # random device id
    }

    # add sig
    data['sig'] = generate_sig(data)

    try:
        response = requests.post(
            'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true',
            data=data, headers=headers, timeout=15
        ).json()

        if 'access_token' in response:
            token = response['access_token']
            session_key = response.get('session_key', '')
            machine_id = response.get('machine_id', '')
            secret = response.get('secret', '')
            uid = str(response.get('uid', uid_or_email))

            # LOCK start
            with file_lock:
                if uid in existing_uids:
                    print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")
                    print(f"     \033[33m[DUPLICATE ACCOUNT]\033[0m: TO EXTRACT Account ───> {uid}.")
                    print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")
                    return

                with open(path_file, 'a', encoding='utf-8') as f:
                    f.write(f"{uid}|{pw}|{token}|{session_key}|{machine_id}|{secret}|{ua_bgraph}\n")

                existing_uids.add(uid)
                success_count.append(uid)
            # LOCK end

            print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[32m[SUCCESS]\033[0m: Extracted Account ─────> {uid}.")
            print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")

        else:
            print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")
            print(f"     \033[31m[FAILED]\033[0m: TO EXTRACT Account ─────> {uid_or_email}.")
            print(response)
            print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except Exception as e:
        print(f"[ERROR] {uid_or_email}: {str(e)}")

def extract_page():
    clear_screen()
    folder_path = "/sdcard/boostphere"  
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    fb_pages(file_path, account_file, extract_type)

def load_existing_tokens(path_file):
    """Load existing accounts or pages from the output file."""
    if os.path.exists(path_file):
        with open(path_file, 'r') as f:
            return {line.split('|')[0] for line in f.readlines()}  # Set of existing uids or page ids
    return set()

def fb_pages(accounts_file, token_output_path, extract_type):
    success_count = []
    existing_tokens = load_existing_tokens(token_output_path)

    try:
        with open(accounts_file, 'r') as file:
            accounts = file.readlines()

        accounts = [line.strip() for line in accounts if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(
                bgraph_page,
                account_line,           # pass the full line
                token_output_path,
                extract_type,
                success_count,
                existing_tokens
            ) for account_line in accounts]

            for future in futures:
                future.result()

        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully extracted.")
        print("\033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")


import requests
import time, random

def bgraph_page(line, path_file, extract_type, success_count, existing_tokens):
    try:
        parts = line.strip().split('|')
        if len(parts) < 2:
            print(f"❌ Invalid line: {line}")
            return

        uid         = parts[0]
        pw          = parts[1]
        access_token = parts[2] if len(parts) > 2 else None
        session_key  = parts[3] if len(parts) > 3 else None
        client_id    = parts[4] if len(parts) > 4 else None
        device_hash  = parts[5] if len(parts) > 5 else None
        user_agent   = parts[6] if len(parts) > 6 else "FBAN/FB4A;FBAV/526.0.0.0;FBBV/123456;FBDM/{density=2.0,width=1080,height=1920};"

        # Skip duplicates
        if uid in existing_tokens:
            print(f"⚠️ ACCOUNT → {uid} ALREADY EXISTS")
            return

        # ────────────── TRY ACCESS TOKEN FIRST ────────────── #
        if access_token:
            time.sleep(random.uniform(2, 5))
            pages = extract_fb_pagesv1(access_token, user_agent=user_agent)
            if pages:
                for page in pages:
                    page_id     = page['id']
                    page_token  = page['accessToken']
                    save_line   = f"{uid}|{page_id}|{page_token}|{user_agent}"
                    if save_line not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(save_line + "\n")
                        print(f"✅ {uid} → Page {page_id} EXTRACTED (using token)")
                        existing_tokens.add(save_line)
                success_count.append(uid)
                return
            else:
                print(f"⚠️ {uid} → Token invalid or no pages, trying login...")

        # ────────────── FALLBACK TO UID+PW LOGIN ────────────── #
        login_token = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"  # fb app token
        time.sleep(random.uniform(2, 5))
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
            'email': uid,
            'password': pw,
            'access_token': login_token
        }
        url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'

        response = requests.post(url, data=data).json()

        if 'access_token' in response:
            new_token = response['access_token']
            pages = extract_fb_pagesv1(new_token, user_agent=user_agent)
            if pages:
                for page in pages:
                    page_id     = page['id']
                    page_token  = page['accessToken']
                    save_line   = f"{uid}|{page_id}|{page_token}|{user_agent}"
                    if save_line not in existing_tokens:
                        with open(path_file, 'a') as f:
                            f.write(save_line + "\n")
                        print(f"✅ {uid} → Page {page_id} EXTRACTED (via login)")
                        existing_tokens.add(save_line)
                success_count.append(uid)
            else:
                print(f"❌ {uid} → Login succeeded but no pages")
        else:
            print(f"❌ {uid} → Login failed")

    except Exception as e:
        print(f"[ERROR] {uid} → {e}")


def extract_fb_pagesv1(token, user_agent=None):
    time.sleep(random.uniform(2, 5))
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {'Authorization': f'Bearer {token}'}
    if user_agent:
        headers['User-Agent'] = user_agent

    pages_data = []

    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"⚠️ Graph error: {response.text}")
            return None

        data = response.json()
        for page in data.get('data', []):
            pages_data.append({
                'id': page.get('id'),
                'accessToken': page.get('access_token')
            })

        url = data.get('paging', {}).get('next')  # pagination

    return pages_data


import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# ────────────────────────────── #
# Perform a reaction via b-graph
# ────────────────────────────── #
def perform_post_reaction_bgraph(token_line, uid_url, reaction_type, proxy=None):
    """
    Send a Facebook reaction using b-graph.facebook.com (Android app style).
    token_line format: uid|page_id|page_token|user_agent
    """
    parts = token_line.strip().split('|')
    if len(parts) < 4:
        return token_line, False, "Malformed line", "Unknown UA"

    uid = parts[0]              # original user_id
    page_id = parts[1]          # extracted page_id
    access_token = parts[2]     # page access token
    ua_bgraph = parts[3]        # user-agent

    time.sleep(random.uniform(1, 2))  # Delay between submissions

    react_url = f"https://b-graph.facebook.com/{uid_url}/reactions"
    params = {
        "type": reaction_type,
        "access_token": access_token
    }
    headers = {
        "User-Agent": ua_bgraph,
        "Authorization": f"OAuth {access_token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    proxies = {"http": proxy, "https": proxy} if proxy else None

    try:
        response = requests.post(
            react_url, headers=headers, data=params, proxies=proxies, timeout=10
        )
        data = {}
        try:
            data = response.json()
        except Exception:
            pass

        if response.status_code != 200 or "error" in data:
            return access_token, False, f"Error: {data.get('error', {}).get('message', 'Unknown')}", ua_bgraph

        # Verify reaction applied
        check_resp = requests.get(
            f"https://graph.facebook.com/{uid_url}?fields=reactions.summary(true)&access_token={access_token}",
            headers=headers, proxies=proxies, timeout=10
        )
        try:
            check_data = check_resp.json()
            summary = check_data.get("reactions", {}).get("summary", {})
            if summary.get("has_liked") or summary.get("total_count", 0) > 0:
                return access_token, True, "Reacted", ua_bgraph
            else:
                return access_token, False, "Reaction not applied", ua_bgraph
        except Exception:
            return access_token, False, "Verification failed", ua_bgraph

    except requests.RequestException as e:
        return token_line, False, f"Request error: {str(e)}", ua_bgraph


# ────────────────────────────── #
# Main Reactions Runner
# ────────────────────────────── #
def perform_reaction_pages():
    clear_screen()
    """Perform reactions based on user input for file choice, starting line, post link, reaction type, and number of reactions."""

    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }

    clear_screen()
    print_overview()
    print(f"""
 {white}CHOOSE TYPE OF REACTORS: 
 {blue}[1] {green}FRA ACCOUNT
 {blue}[2] {green}FRA PAGES
 {blue}[3] {green}RPW ACCOUNT
 {blue}[4] {green}RPW PAGES
 {red}[0] {red} EXIT
 {blue}───────────────────────────────────────────────────────────────\033[0m""")

    try:
        file_choice = int(input(f" {green}Choose: "))
        print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the tokens from the selected file
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)

    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    # Step 3: Ask the user for the starting line
    try:
        start_line = int(input(f" {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    # Step 4: Ask for the post link
    print(f" {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")
    z = input(f" {green}Enter the post link or ID: ")

    post_id = extract_post_ids_v1(z)
    if not post_id:
        post_id = get_combined_data(z)
    if not post_id:
        print("Unable to extract post ID from the URL!")
        return
    uid_url = post_id
    print(f" {blue}───────────────────────────────────────────────────────────────{reset}")
    print(f" {green}your post url is : {red}{uid_url}")
    print(f" {blue}───────────────────────────────────────────────────────────────{reset}")
    print(f""" {yellow}Choose the reaction type:
 {blue}[1] {green}LIKE
 {blue}[2] {green}LOVE
 {blue}[3] {green}WOW
 {blue}[4] {green}SAD
 {blue}[5] {green}ANGRY
 {blue}[6] {green}HAHA
 {blue}[7] {green}CARE
 {blue}───────────────────────────────────────────────────────────────\033[0m""")

    try:
        reaction_choice = int(input(f" {green}Choose: "))
        reaction_map = {
            1: "LIKE",
            2: "LOVE",
            3: "WOW",
            4: "SAD",
            5: "ANGRY",
            6: "HAHA",
            7: "CARE"
        }
        reaction_type = reaction_map.get(reaction_choice, None)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")

    # Step 6: Number of reactions
    try:
        num_reactions = int(input(f" {yellow}Enter the number of reactions: "))
        print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print(f" {blue}───────────────────────────────────────────────────────────────\033[0m")
        print("Please enter a valid number for reactions.")
        return

    # Step 7: Perform reactions
    max_workers = 1
    reactions_count = 0
    total_successful_reactions = 0
    tokens_used = 0
    future_to_token = {}

    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for token in tokens_batch:
                # Submit each token with a 2–5s spacing (submission delay)
                future = executor.submit(perform_post_reaction_bgraph, token, uid_url, reaction_type, proxy=None)
                future_to_token[future] = token

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                parts = token.split('|')
                page_id  = parts[0] if len(parts) > 0 else "Unknown"

                try:
                    access_token, success, response_text, ua_bgraph = future.result()
                    if success:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     [REACTOR] {yellow}{page_id}{reset} ──> {green}SUCCESSFULL REACTED!{reset}")
                    else:
                        print(f"     [REACTOR] {yellow}{page_id}{reset} ──> {red}FAILED: {response_text}{reset}")
                except Exception as e:
                    print(f"Error processing token {token}: {e}")

        tokens_used += len(tokens_batch)

        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    print("────────────────────────────────────────────")
    print(f"TOTAL SUCCESSFUL REACTIONS: {reactions_count}")


def Perform_React_Post_Photo_Video_Reels(token_line, uid_url, reaction_type):
    try:
        parts = token_line.strip().split('|')
        if len(parts) < 7:
            return None, False, "Invalid token format"

        uid = parts[0]
        access_token = parts[2]
        ua_bgraph = parts[6]
        url = f"https://b-graph.facebook.com/{uid_url}/reactions"
        payload = {"type": reaction_type, "access_token": access_token}
        headers = {"User-Agent": ua_bgraph}

        time.sleep(random.uniform(1, 2))  # Delay between submissions

        r = requests.post(url, data=payload, headers=headers)

        if r.status_code == 200:
            try:
                data = r.json()
                if data.get("success") is True:
                    return access_token, True, "Reacted"
                else:
                    return access_token, False, "Already reacted or no change"
            except Exception:
                return access_token, False, "Invalid JSON response"

        else:
            # check for expired/invalid tokens
            try:
                error_data = r.json().get("error", {})
                error_msg = error_data.get("message", "")
                error_code = error_data.get("code", "")

                if "Invalid OAuth access token" in error_msg:
                    return access_token, False, "Invalid Token"
                elif error_code == 190:
                    return access_token, False, "Token Expired"
                else:
                    return access_token, False, f"Error: {error_msg}"

            except Exception:
                return access_token, False, f"Error: {r.text}"

    except Exception as e:
        return None, False, f"Exception: {str(e)}"

def move_bad_token(original_file, bad_token, reason):
    """Move a bad token into the proper file and remove it from the original file."""
    if reason == "restricted":
        save_file = "/sdcard/boostphere/ACCOUNTRESTRICTED.txt"
    elif reason == "invalid":
        save_file = "/sdcard/boostphere/INVALIDTOKEN.txt"
    else:
        return  # safety guard

    # Save token to the respective file
    with open(save_file, "a", encoding="utf-8") as f:
        f.write(bad_token.strip() + "\n")

    # Remove token from the original file
    with open(original_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    updated = [line for line in lines if line.strip() != bad_token.strip()]
    with open(original_file, "w", encoding="utf-8") as f:
        f.writelines(updated)


READ_ACCESS_TOKEN = "EAAAAUaZA8jlABPfpl9XTK9Oluoyt533iOg0b4nuFJdjd10xlRU40z0lm9GQkl5C1H3gh67QQZAcfQCNHNa6o65ZAOTLZBKt53F6YVaBhspGsMZC14IrZB3Po2uEeh5ZBtxbqknZB9tyOhzVMSqmGxNsfKK8mDd4TloOvPN8c2uz67jZClMshznJOrZA9V950m0TQgZBtKwj8Te5ZAgZDZD"

def extract_post_id(url):
    patterns = [
        r'groups/(\d+)/permalink/(\d+)/',   # group posts
        r'(\d+)/posts/(\d+)/',              # user/page posts
        r'fbid=(\d+)',                      # photo posts
        r'story_fbid=(\d+)&id=(\d+)'        # story posts
    ]
    for p in patterns:
        match = re.search(p, url)
        if match:
            return "_".join(match.groups())
    return None

def get_reaction_count_for_type(post_url_or_id, reaction_type, access_token=READ_ACCESS_TOKEN):
    """Get total count of a specific reaction type for a post, handling pagination."""
    post_id = post_url_or_id if "_" in post_url_or_id else extract_post_id(post_url_or_id)

    if not post_id:
        print("⛔ Cannot extract post ID from URL.")
        return 0

    count = 0
    url = f"https://graph.facebook.com/v20.0/{post_id}/reactions?limit=100&access_token={access_token}"

    while url:
        try:
            resp = requests.get(url).json()
            if "error" in resp:
                print(f"ℹ️ Error fetching {reaction_type}: {resp['error']['message']}")
                return 0

            for reaction in resp.get("data", []):
                if reaction.get("type") == reaction_type:
                    count += 1

            # Pagination: go to next page if exists
            url = resp.get("paging", {}).get("next")

        except Exception as e:
            print(f"⛔ Graph API request failed: {e}")
            return 0

    # Only add +1 if count is greater than 0
    if count > 0:
        count += 1

    return count



# ────────────── MAIN FUNCTION ────────────── #
def Perform_reactionV2():
    """Perform reactions based on user input, with optimized thread usage and auto-handling of invalid/restricted tokens."""

    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────{reset}""")

    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load tokens
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    if not tokens:
        print("No tokens available from the selected file.")
        return

    # Step 3: Ask for starting line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {len(tokens)}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        if start_line < 1 or start_line > len(tokens):
            print(f"Please enter a valid line number between 1 and {len(tokens)}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    # Step 4: Post ID input
    z = input(f"    {green}Enter the post link or ID{reset} : ")
    post_id = extract_post_ids_v1(z)
    if not post_id:
        post_id = get_combined_data(z)
    if not post_id:
        print("Unable to extract post ID from the URL!")
        return
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    uid_url = post_id
    print(f"    {green}your post url is : {red}{uid_url}")
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")

    # Step 5: Reaction type
    print(f"""    {yellow}Choose the reaction type:
     {BLUE}[1] {green}LIKE
     {BLUE}[2] {green}LOVE
     {BLUE}[3] {green}WOW
     {BLUE}[4] {green}SAD
     {BLUE}[5] {green}ANGRY
     {BLUE}[6] {green}HAHA
     {BLUE}[7] {green}CARE
    {BLUE}───────────────────────────────────────────────────────────────{reset}""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE", 
            2: "LOVE", 
            3: "WOW", 
            4: "SAD", 
            5: "ANGRY", 
            6: "HAHA",
            7: "CARE"
        }
        reaction_type = reaction_map.get(reaction_choice)
        if not reaction_type:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # ✅ Fetch current count for this reaction
    current_count = get_reaction_count_for_type(uid_url, reaction_type)
    print(f"     {green}Current {blue}{reaction_type}{reset} count: {yellow}{current_count}{reset}")
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")

    # Step 6: Number of reactions
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions : {reset}"))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    except ValueError:
        print("Please enter a valid number for reactions.")
        return
    
    # Step 7: Processing loop using **single ThreadPoolExecutor**
    max_workers = 2
    total_success = total_fail = restricted_count = invalid_count = 0

    # Submit all tokens to the executor once
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(Perform_React_Post_Photo_Video_Reels, t, uid_url, reaction_type): t for t in tokens}

        for future in as_completed(futures):
            token_line = futures[future]
            try:
                access_token, status, message = future.result()
                uid = token_line.split('|')[0]

                if status is True and message == "Reacted":
                    total_success += 1
                    print(f"     [REACTOR] {yellow}{uid}{reset} ──> {green}SUCCESSFULLY REACTED!{reset}")
                elif status is False and "Already reacted" in message:
                    total_success += 1
                    print(f"     [REACTOR] {yellow}{uid}{reset} ──> {yellow}SKIPPED (Already reacted){reset}")
                else:
                    total_fail += 1
                    if "190" in message or "Invalid" in message or "Token Expired" in message:
                        invalid_count += 1
                        move_bad_token(file_path, token_line, "invalid")
                        print(f"     [REACTOR] {yellow}{uid}{reset} ──> {red}INVALID TOKEN → moved{reset}")
                    elif ("368" in message 
                          or "temporarily blocked" in message.lower()
                          or "abusive" in message.lower() 
                          or "disallowed" in message.lower()):
                        restricted_count += 1
                        move_bad_token(file_path, token_line, "restricted")
                        print(f"     [REACTOR] {yellow}{uid}{reset} ──> {red}ACCOUNT RESTRICTED → moved{reset}")
                    else:
                        print(f"     [REACTOR] {yellow}{uid}{reset} ──> {red}FAILED: {message}{reset}")

                # Stop if we reached the target number of reactions
                if total_success >= num_reactions:
                    break

            except Exception as e:
                print(f"     [REACTOR] ERROR processing token: {e}")

    # Step 8: Summary
    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_success}{reset}")
    print(f"{red}TOTAL FAILED REACTIONS: {total_fail}{reset}")
    print(f"{yellow}TOTAL RESTRICTED MOVED: {restricted_count}{reset}")
    print(f"{yellow}TOTAL INVALID MOVED: {invalid_count}{reset}")
    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")


def Perform_React_Post_Random(token, uid_url, reaction_type):
    """Send a reaction using the provided full-format token."""
    parts = token.split('|')
    if len(parts) < 7:
        uid = parts[0] if parts else "Unknown"
        return None, None, f"Invalid token format for UID {uid}"
    
    uid = parts[0]
    access_token = parts[2]  # Access token at index 2
    user_agent = parts[6]    # User-Agent at index 6

    auto_react = f'https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'
    
    try:
        response = requests.post(auto_react, headers={'User-Agent': user_agent}, timeout=10)
        return access_token, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return access_token, None, str(e)

def React_Post_Random():
    """Perform reactions based on user input, with auto-handling of restricted/invalid tokens."""
    # Step 1: Ask the user which file to use
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────{reset}""")
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load tokens
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    # Step 3: Ask the user for the starting line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    # Step 4: Ask for post link/ID
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/video/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    z = input(f"   {green}Enter the post link or ID: ")
    post_id = extract_post_ids_v1(z)

    if not post_id:
        post_id = get_combined_data(z)
    if not post_id:
        print("Unable to extract post ID from the URL!")
        return
    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    uid_url = post_id

    # Step 5: Reaction type
    print(f"""    {yellow}Choose the mixed reaction type:
     {blue}[1] {green}LIKE,LOVE,WOW
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────{reset}""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {
            1: "LIKE", 
            2: "LOVE", 
            3: "WOW", 
            4: "SAD", 
            5: "ANGRY", 
            6: "HAHA"}
        reaction_type = reaction_map.get(reaction_choice)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    
    # Step 6: Number of reactions
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    except ValueError:
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        print("Please enter a valid number for reactions.")
        return

    # Step 7: Process reactions
    max_workers = 5
    reactions_count = 0
    total_successful_reactions = 0
    tokens_used = 0
    failed_reactions = 0
    restricted_count = 0
    invalid_count = 0

    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(Perform_React_Post_Random, t, uid_url, reaction_type): t for t in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    access_token, status_code, response_text = future.result()
                    if status_code == 200:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED!{reset}")
                    else:
                        failed_reactions += 1
                        try:
                            error_data = json.loads(response_text).get("error", {})
                            error_code = error_data.get("code")

                            if error_code == 368:  # restricted
                                restricted_count += 1
                                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}ACCOUNT RESTRICTED → moved to ACCOUNTRESTRICTED.txt{reset}")
                                move_bad_token(file_path, token, "restricted")

                            elif error_code == 190:  # invalid/expired
                                invalid_count += 1
                                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}INVALID TOKEN → moved to INVALIDTOKEN.txt{reset}")
                                move_bad_token(file_path, token, "invalid")

                            else:
                                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT: {response_text}{reset}")

                        except Exception:
                            print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT: {response_text}{reset}")

                except Exception as e:
                    print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}ERROR: {e}{reset}")

        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    # Final summary (with reset so colors don’t bleed)
    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}{reset}")
    print(f"{red}TOTAL FAILED REACTIONS: {failed_reactions}{reset}")
    print(f"{yellow}TOTAL RESTRICTED MOVED: {restricted_count}{reset}")
    print(f"{yellow}TOTAL INVALID MOVED: {invalid_count}{reset}")
    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")

def perform_auto_follow(token_line, account_id, proxy=None):
    """
    Follow a Facebook account using a token line with UA.
    token_line format: uid|pw|token|session_key|machine_id|secret|ua_bgraph
    """
    parts = token_line.strip().split('|')
    if len(parts) != 7:
        return token_line, False, "Malformed line", "Unknown UA"

    uid = parts[0]
    pw = parts[1]  # not used
    access_token = parts[2]
    session_key = parts[3]  # optional
    machine_id = parts[4]   # optional
    secret = parts[5]       # optional
    ua_bgraph = parts[6]    # use this as User-Agent

    time.sleep(random.uniform(2, 5))

    headers = {
        "User-Agent": ua_bgraph,
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    proxies = {"http": proxy, "https": proxy} if proxy else None

    try:
        url = f"https://b-graph.facebook.com/v23.0/{account_id}/subscribers"
        response = requests.post(url, headers=headers, proxies=proxies, timeout=10)
        
        try:
            data = response.json()
        except Exception:
            data = {}

        if response.status_code == 200:
            return access_token, True, "Successfully followed", ua_bgraph
        elif "error" in data:
            return access_token, False, data["error"].get("message", "Unknown error"), ua_bgraph
        else:
            return access_token, False, f"Failed with status {response.status_code}", ua_bgraph

    except requests.exceptions.RequestException as e:
        return token_line, False, f"Request error: {str(e)}", ua_bgraph


def perform_auto_follow_function():
    """Automatically follow a target account using tokens and pages."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }

    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF FOLLOWERS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")

    # Select file
    file_choice = int(input(f"    {green}Choose the type of followers: "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    file_path = file_options.get(file_choice)
    if not file_path:
        print("Invalid choice.")
        return

    # Load tokens
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return

    if not tokens:
        print("No tokens found in the selected file.")
        return

    # Start line
    start_line = int(input(f"    {yellow}Enter the starting line (1 to {len(tokens)}): "))
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    tokens = tokens[start_line - 1:]

    # Get target account ID (numeric)
    account_url = input(f"   {yellow}Enter the target account URL: ")
    sample_token = tokens[0]
    ua_sample = sample_token.split('|')[6]
    access_token_sample = sample_token.split('|')[2]
    account_id = extract_user_id_prof(account_url, ua=ua_sample, access_token=access_token_sample)

    if not account_id:
        print(f"{red}Invalid account ID or username.")
        return
    print(f"    {blue}Target Account ID: {account_id}{blue}")

    # Follow limit
    try:
        follow_limit = int(input(f'    {red}LIMIT: '))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    except ValueError:
        print("Invalid number for follow limit.")
        return

    follow_count = 0
    failed_count = 0
    current_index = 0

    # Perform follows with threads
    with ThreadPoolExecutor(max_workers=1) as executor:
        while follow_count < follow_limit and current_index < len(tokens):
            futures = {}
            # Batch submit tokens
            for i in range(current_index, min(current_index + (follow_limit - follow_count), len(tokens))):
                token_line = tokens[i]
                futures[executor.submit(perform_auto_follow, token_line, account_id)] = token_line

            for future in as_completed(futures):
                token_line = futures[future]
                uid = token_line.split('|')[0]
                try:
                    _, success, message, ua = future.result()
                    if success:
                        follow_count += 1
                        print(f"     {green}[USER] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY FOLLOWED!")
                    else:
                        failed_count += 1
                        print(f"     {red}[USER] {yellow}{uid}  {blue}───────> {red}FAILED TO FOLLOW! ↳ {message}")
                except Exception as e:
                    failed_count += 1
                    print(f"     {red}[USER] {yellow}{uid}  {blue}───────> {red}ERROR: {e}")

            current_index += len(futures)

            if current_index >= len(tokens) and follow_count < follow_limit:
                current_index = 0  # Reuse tokens if needed

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f'     {green}SUCCESS: {follow_count}')
    print(f'     {red}FAILED: {failed_count}')

def perform_auto_follow_page(token_line, account_id, proxy=None):
    """
    Follow a Facebook account using a token line with UA.
    token_line format: uid|page_id|page_token|user_agent
    """
    parts = token_line.strip().split('|')
    if len(parts) < 4:
        return token_line, False, "Malformed line", "Unknown UA"

    uid         = parts[0]  # original user id
    page_id     = parts[1]  # page id (not always used here)
    access_token = parts[2] # page/user access token
    ua_bgraph   = parts[3]  # user-agent

    time.sleep(random.uniform(2, 5))

    headers = {
        "User-Agent": ua_bgraph,
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    proxies = {"http": proxy, "https": proxy} if proxy else None

    try:
        url = f"https://b-graph.facebook.com/v23.0/{account_id}/subscribers"
        response = requests.post(url, headers=headers, proxies=proxies, timeout=10)

        try:
            data = response.json()
        except Exception:
            data = {}

        if response.status_code == 200 and "error" not in data:
            return page_id, True, "Successfully followed", ua_bgraph
        elif "error" in data:
            return page_id, False, data["error"].get("message", "Unknown error"), ua_bgraph
        else:
            return page_id, False, f"Failed with status {response.status_code}", ua_bgraph

    except requests.exceptions.RequestException as e:
        return page_id, False, f"Request error: {str(e)}", ua_bgraph


def perform_auto_follow_for_page():
    """Automatically follow a target account using tokens and pages."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }

    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF FOLLOWERS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")

    # Select file
    try:
        file_choice = int(input(f"    {green}Choose the type of followers: "))
    except ValueError:
        print("Invalid choice.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    file_path = file_options.get(file_choice)
    if not file_path:
        print("Invalid choice.")
        return

    # Load tokens
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File not found.")
        return

    if not tokens:
        print("No tokens found in the selected file.")
        return

    # Start line
    try:
        start_line = int(input(f"    {yellow}Enter the starting line (1 to {len(tokens)}): "))
    except ValueError:
        print("Invalid line number.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    tokens = tokens[start_line - 1:]

    # Get target account ID (numeric)
    account_url = input(f"   {yellow}Enter the target account URL: ")
    sample_parts = tokens[0].split('|')
    ua_sample = sample_parts[3]
    access_token_sample = sample_parts[2]
    account_id = extract_user_id_prof(account_url, ua=ua_sample, access_token=access_token_sample)

    if not account_id:
        print(f"{red}Invalid account ID or username.")
        return
    print(f"    {blue}Target Account ID: {account_id}{blue}")

    # Follow limit
    try:
        follow_limit = int(input(f'    {red}LIMIT: '))
    except ValueError:
        print("Invalid number for follow limit.")
        return

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    follow_count = 0
    failed_count = 0
    current_index = 0

    # Perform follows with threads
    with ThreadPoolExecutor(max_workers=1) as executor:
        while follow_count < follow_limit and current_index < len(tokens):
            futures = {}
            # Batch submit tokens
            for i in range(current_index, min(current_index + (follow_limit - follow_count), len(tokens))):
                token_line = tokens[i]
                futures[executor.submit(perform_auto_follow_page, token_line, account_id)] = token_line

            for future in as_completed(futures):
                token_line = futures[future]
                parts = token_line.split('|')
                page_id = parts[1] if len(parts) > 1 else "Unknown"

                try:
                    _, success, message, ua = future.result()
                    if success:
                        follow_count += 1
                        print(f"     {green}[PAGE] {yellow}{page_id}  {blue}───────> {green}SUCCESSFULLY FOLLOWED!")
                    else:
                        failed_count += 1
                        print(f"     {red}[PAGE] {yellow}{page_id}  {blue}───────> {red}FAILED TO FOLLOW! ↳ {message}")
                except Exception as e:
                    failed_count += 1
                    print(f"     {red}[PAGE] {yellow}{page_id}  {blue}───────> {red}ERROR: {e}")

            current_index += len(futures)

            if current_index >= len(tokens) and follow_count < follow_limit:
                current_index = 0  # Reuse tokens if needed

    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    print(f'     {green}SUCCESS: {follow_count}')
    print(f'     {red}FAILED: {failed_count}')

def load_tokens(file_path):
    """Load tokens from the specified file."""
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
        return tokens
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return []
    
def make_http_request(method, url, headers=None, data=None, proxy=None):
    """Make an HTTP request with optional proxy."""
    try:
        proxies = {"http": proxy, "https": proxy} if proxy else None
        if method.upper() == 'POST':
            response = requests.post(url, headers=headers, data=data, proxies=proxies, timeout=10)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        else:
            print(f"Unsupported HTTP method: {method}")
            return None
        if response.status_code == 200:
            return response.json()
        else:
            return response.json()
    except Exception as e:
        print(f"HTTP request exception: {str(e)}")
        return None

def like_facebook_page(uid, token_line, proxy=None):
    """Only Like a Facebook page/profile using token line with UA."""
    parts = token_line.strip().split('|')
    
    if len(parts) < 7:
        return False, ["Malformed token line"]

    access_token = parts[2].strip()
    ua = parts[6].strip()

    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': ua
    }

    messages = []
    # Like only
    like_url = f"https://graph.facebook.com/v20.0/{uid}/likes"
    like_resp = make_http_request('POST', like_url, headers=headers, proxy=proxy)
    if like_resp is None:
        messages.append("Like request failed")
        success = False
    elif 'error' in like_resp:
        messages.append(f"Like error: {like_resp['error'].get('message')}")
        success = False
    else:
        messages.append("Liked successfully")
        success = True

    return success, messages


def like_facebook_page_function():
    """Main function to manage Like actions only."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")

    try:
        file_choice = int(input(f"    {green}Choose:  "))
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    if total_tokens == 0:
        print("No tokens available from the selected file.")
        return

    # Starting line input
    while True:
        try:
            start_line = int(input(f"Enter starting line (1 to {total_tokens}): "))
            if 1 <= start_line <= total_tokens:
                break
            else:
                print(f"Invalid line. Must be between 1 and {total_tokens}.")
        except ValueError:
            print("Enter a valid number.")

    tokens = tokens[start_line - 1:]
    max_limit = total_tokens - start_line + 1

    # Limit input
    while True:
        user_input = input(f"LIMIT (max {max_limit}, 0 to exit): ").strip()
        if user_input.lower() == "exit" or user_input == "0":
            print("Exiting...")
            return  # exit the function
        try:
            num_actions = int(user_input)
            if 1 <= num_actions <= max_limit:
                break
            else:
                print(f"Limit must be between 1 and {max_limit}.")
        except ValueError:
            print("Enter a valid number.")

    uid = input(f"    {green}Enter the Page/Profile UID or numeric ID: ").strip()
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    # Counters
    like_success = 0
    like_failed = 0

    # Perform actions with ThreadPoolExecutor
    from concurrent.futures import ThreadPoolExecutor, as_completed
    action_count = 0

    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = {}
        for token in tokens[:num_actions]:
            future = executor.submit(like_facebook_page, uid, token)
            futures[future] = token.split('|')[0]
            time.sleep(random.uniform(2.8, 5))  # delay between submissions

        for future in as_completed(futures):
            user_id = futures[future]
            success, messages = future.result()
            action_count += 1

            if success:
                like_success += 1
            else:
                like_failed += 1

            # Color-code messages
            colored_msgs = []
            for msg in messages:
                if "successfully" in msg.lower():
                    colored_msgs.append(f"\033[1;32m{msg}\033[0m")  # green
                else:
                    colored_msgs.append(f"\033[1;31m{msg}\033[0m")  # red

            print(f"[{user_id}] {' | '.join(colored_msgs)} | Target UID: {uid}")

    # Final Summary
    print(f"\n===== SUMMARY for UID: {uid} =====")
    print(f"✅ Like Success: {like_success}")
    print(f"❌ Like Failed: {like_failed}")
    print("=================================")
    print(f"Completed {action_count} requested actions.\n")


def react_comment(token_line, uid_url, reaction_type, proxy=None):
    parts = token_line.strip().split('|')
    if len(parts) != 7:
        return token_line, False, "Malformed line", "Unknown UA"

    access_token = parts[2]
    ua_bgraph = parts[6]

    url = f'https://graph.facebook.com/v18.0/{uid_url}/reactions'
    params = {'access_token': access_token, 'type': reaction_type}
    headers = {'User-Agent': ua_bgraph, 'Accept': 'application/json'}
    proxies = {"http": proxy, "https": proxy} if proxy else None

    try:
        response = requests.post(url, params=params, headers=headers, proxies=proxies, timeout=10)
        try:
            data = response.json()
            if 'success' in data and data['success'] is True:
                return token_line, True, "Successfully reacted", ua_bgraph
            elif 'error' in data:
                return token_line, False, data['error']['message'], ua_bgraph
            else:
                return token_line, False, str(data), ua_bgraph
        except json.JSONDecodeError:
            return token_line, False, response.text, ua_bgraph
    except requests.exceptions.RequestException as e:
        return token_line, False, str(e), ua_bgraph


def comment_react():
    """Perform comment reactions with auto-handling of restricted/invalid tokens."""
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────{reset}""")

    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load tokens
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines() if line.strip()]
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    available_tokens = len(tokens)
    if available_tokens == 0:
        print("No tokens available from the selected file.")
        return

    # Step 3: Ask the user for the starting line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {available_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
        if start_line < 1 or start_line > available_tokens:
            print(f"Please enter a valid line number between 1 and {available_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    # Step 4: Ask for comment link/ID
    fb_url = input(f"   {green}Enter Facebook comment link/ID: {reset}")
    uid_url = extract_facebook_uid_url(fb_url)
    if not uid_url:
        print("Unable to parse Facebook URL!")
        return

    # Handle pfbid/short links
    if uid_url.startswith("pfbid") or re.search(r'/share/v/', fb_url):
        ua_sample = tokens[0].split('|')[6]
        numeric_id = resolve_pfbid_to_numeric(fb_url, ua_sample)
        if "_" in uid_url:
            _, comment_id = uid_url.split("_")
            uid_url = f"{numeric_id}_{comment_id}"
        else:
            uid_url = numeric_id

    if "_" not in uid_url:
        comment_id = input(f"   {green}Enter COMMENT ID: {reset}")
        uid_url = f"{uid_url}_{comment_id}"
      
    # Step 5: Reaction type
    print(f"""    {yellow}Choose the reaction type:
     {blue}[1] {green}LIKE
     {blue}[2] {green}LOVE
     {blue}[3] {green}WOW
     {blue}[4] {green}SAD
     {blue}[5] {green}ANGRY
     {blue}[6] {green}HAHA
    {blue}───────────────────────────────────────────────────────────────{reset}""")
    
    try:
        reaction_choice = int(input(f"     {green}Choose: "))
        reaction_map = {1: "LIKE", 2: "LOVE", 3: "WOW", 4: "SAD", 5: "ANGRY", 6: "HAHA"}
        reaction_type = reaction_map.get(reaction_choice)
        if reaction_type is None:
            print("Invalid reaction choice.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 6: Number of reactions
    try:
        num_reactions = int(input(f"     {yellow}Enter the number of reactions: "))
        print(f"    {blue}───────────────────────────────────────────────────────────────{reset}")
    except ValueError:
        print("Please enter a valid number for reactions.")
        return

    # Step 7: Process reactions
    max_workers = 2
    reactions_count = 0
    total_successful_reactions = 0
    tokens_used = 0
    failed_reactions = 0
    restricted_count = 0
    invalid_count = 0

    while total_successful_reactions < num_reactions and tokens_used < available_tokens:
        remaining_tokens = tokens[tokens_used:]
        tokens_batch = remaining_tokens[:num_reactions - total_successful_reactions]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_token = {executor.submit(react_comment, t, uid_url, reaction_type): t for t in tokens_batch}

            for future in as_completed(future_to_token):
                token = future_to_token[future]
                uid = token.split('|')[0]
                try:
                    _, success, response_text, _ = future.result()
                    if success:
                        reactions_count += 1
                        total_successful_reactions += 1
                        print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY REACTED TO COMMENT!{reset}")
                    else:
                        failed_reactions += 1
                        try:
                            error_data = json.loads(response_text).get("error", {})
                            error_code = error_data.get("code")

                            if error_code == 368:  # restricted
                                restricted_count += 1
                                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}ACCOUNT RESTRICTED → moved to ACCOUNTRESTRICTED.txt{reset}")
                                move_bad_token(file_path, token, "restricted")

                            elif error_code == 190:  # invalid
                                invalid_count += 1
                                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}INVALID TOKEN → moved to INVALIDTOKEN.txt{reset}")
                                move_bad_token(file_path, token, "invalid")

                            else:
                                print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT: {response_text}{reset}")

                        except Exception:
                            print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}FAILED TO REACT: {response_text}{reset}")

                except Exception as e:
                    print(f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {red}ERROR: {e}{reset}")

        tokens_used += len(tokens_batch)
        if tokens_used >= available_tokens:
            print("No more tokens available.")
            break

    # Final summary
    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")
    print(f"{green}TOTAL SUCCESSFUL REACTIONS: {total_successful_reactions}{reset}")
    print(f"{red}TOTAL FAILED REACTIONS: {failed_reactions}{reset}")
    print(f"{yellow}TOTAL RESTRICTED MOVED: {restricted_count}{reset}")
    print(f"{yellow}TOTAL INVALID MOVED: {invalid_count}{reset}")
    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")

def comment_with_token(post_id, comment, access_token_line):
    # Extract the correct parts from your token format: uid|password|access_token|...
    parts = access_token_line.split('|')
    if len(parts) < 3:
        return f"Invalid token format: {access_token_line}"

    uid = parts[0]
    token = parts[2]
    user_agent = parts[6]
    try:
        auto_comment_url = f'https://graph.facebook.com/{post_id}/comments'
        params = {
            'message': comment,
            'access_token': token
        }
        headers = {
            'user-agent': user_agent # your custom UA function
        }
        time.sleep(1)
        response = requests.post(auto_comment_url, params=params, headers=headers)

        if response.status_code == 200:
            return f"     {red}[REACTOR] {yellow}{uid}  {blue}───────> {green}SUCCESSFULLY COMMENTED!"
        else:
            return f"{red}[FAILED] {uid} → {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"


def comment_function():
    """Perform comments using multiple tokens from a file."""

    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF REACTORS: 
     {yellow}[1] {green}FRA ACCOUNT 
     {yellow}[2] {green}FRA PAGES
     {yellow}[3] {green}RPW ACCOUNT
     {yellow}[4] {green}RPW PAGES
     {red}[0] {red}EXIT 
    {blue}───────────────────────────────────────────────────────────────{reset}\033[0m""")

    try:
        file_choice = int(input(f"     {green}Choose: "))
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error loading tokens: {e}")
        return

    if not tokens:
        print("No tokens available.")
        return

    try:
        start_line = int(input(f"    {green}Enter the starting line (1 to {len(tokens)}{reset}): "))
        if start_line < 1 or start_line > len(tokens):
            print("Invalid starting line.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens = tokens[start_line - 1:]

    post_id = input(f"    {green}Enter the post ID or link : {reset}")
    post_id = get_combined_data(post_id)

    try:
        num_comments = int(input(f"    {red}Enter the number of comments: {reset}"))
        if num_comments <= 0:
            print("Must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    comments_input = input(f"    {green}Enter all comments separated by commas:{reset}")
    comments_list = [c.strip() for c in comments_input.split(',')][:num_comments]

    try:
        num_accounts = int(input(f"   {green}Enter number of accounts to use (1 to {reset}{len(tokens)}): "))
        if num_accounts <= 0 or num_accounts > len(tokens):
            print("Invalid number of accounts.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    random.shuffle(comments_list)
    comments_count = 0
    max_workers = 2
    
    print("Starting comments...")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_data = {
            executor.submit(comment_with_token, post_id, comments_list[i % len(comments_list)], tokens[i]):
            (tokens[i], comments_list[i % len(comments_list)])
            for i in range(num_accounts)
        }

        for future in as_completed(future_to_data):
            token_line, comment_text = future_to_data[future]
            result = future.result()
            if "SUCCESSFULLY" in result:
                comments_count += 1
                print(f"{result} ─ Comment: {green}{comment_text}{white}")
            else:
                print(result)

    print(f"Total comments made: {comments_count}")

def extract_post_comment_id(url: str):
    """Extract a valid post_id or comment_id from a Facebook URL."""
    try:
        # If the URL has comment_id param → return comment_id
        comment_match = re.search(r'comment_id=(\d+)', url)
        if comment_match:
            return comment_match.group(1)

        # If the URL has fbid param → return fbid
        fbid_match = re.search(r'fbid=(\d+)', url)
        if fbid_match:
            return fbid_match.group(1)

        # If the URL has /posts/<id> → return post id
        post_match = re.search(r'/posts/(\d+)', url)
        if post_match:
            return post_match.group(1)

        # If the URL has /videos/<id> → return video id
        video_match = re.search(r'/videos/(\d+)', url)
        if video_match:
            return video_match.group(1)

        return None
    except Exception:
        return None
    
def reply_comment(target_id, comment, access_token_line):
    """Comment on a post or reply to a comment using a dedicated token."""
    parts = access_token_line.split('|')
    if len(parts) < 7:
        return False, "Token format error", None, None

    uid = parts[0]
    token = parts[2]
    ua = parts[6]

    if not token.startswith(("EA", "EAA")):
        return False, "Invalid token", None, None

    try:
        url = f'https://graph.facebook.com/v19.0/{target_id}/comments'
        params = {'message': comment, 'access_token': token}
        headers = {'user-agent': ua}

        time.sleep(1)
        response = requests.post(url, params=params, headers=headers)

        if response.ok:
            return True, "", f"{uid} → Commented: {comment}", None
        else:
            return False, response.text, None, None

    except requests.exceptions.RequestException as e:
        return False, str(e), None, None

def comment_reply():
    clear_screen()
    print_overview()
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    print(f"""CHOOSE TYPE OF REACTORS: 
     [1] FRA ACCOUNT 
     [2] FRA PAGES
     [3] RPW ACCOUNT
     [4] RPW PAGES
     [0] EXIT
───────────────────────────────────────────────────────────────""")
    
    try:
        file_choice = int(input("Choose: "))
        if file_choice not in file_options:
            print(f"{RED}Invalid choice{RESET}")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print(f"{RED}Please enter a valid number{RESET}")
        return

    # Load tokens
    try:
        with open(file_path, 'r') as f:
            tokens = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{RED}Error loading tokens:{RESET} {e}")
        return

    if not tokens:
        print(f"{RED}No tokens available{RESET}")
        return

    # Starting line
    try:
        start_line = int(input(f"Enter starting line (1-{len(tokens)}): "))
        if start_line < 1 or start_line > len(tokens):
            print(f"{RED}Invalid line number{RESET}")
            return
    except ValueError:
        print(f"{RED}Please enter a valid number{RESET}")
        return

    tokens = tokens[start_line-1:]

    # Post URL
    url = input("Enter the post URL (with comment_id if replying): ")
    post_id_comment = extract_post_comment_id(url)
    if not post_id_comment:
        print(f"{RED}Invalid URL or missing comment_id{RESET}")
        return

    # Comments input
    comments_input = input("Enter all comments separated by commas: ")
    comments_list = [c.strip() for c in comments_input.split(',') if c.strip()]
    if not comments_list:
        print(f"{RED}No comments entered{RESET}")
        return
    num_comments = len(comments_list)

    # Number of accounts
    try:
        num_accounts = int(input(f"Enter number of accounts to use (1-{len(tokens)}): "))
        if num_accounts <= 0 or num_accounts > len(tokens):
            print(f"{RED}Invalid number of accounts{RESET}")
            return
    except ValueError:
        print(f"{RED}Please enter a valid number{RESET}")
        return

    tokens = tokens[:num_accounts]

    print("Starting comment replies...")

    success_count = 0
    restricted_count = 0
    invalid_count = 0

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {}
        for i in range(num_accounts):
            comment_text = comments_list[i % num_comments]
            futures[executor.submit(reply_comment, post_id_comment, comment_text, tokens[i])] = (tokens[i], comment_text)

        for future in as_completed(futures):
            token_line, comment_text = futures[future]
            uid = token_line.split("|")[0] if "|" in token_line else "Unknown"

            try:
                success, response_text, message, _ = future.result()
                if success:
                    success_count += 1
                    print(f"     {GREEN}[REPLY] {YELLOW}{uid}  {BLUE}───────> {GREEN}SUCCESSFULLY REPLIED{RESET} ─ Comment: {WHITE}{comment_text}{RESET}")
                else:
                    try:
                        error_data = json.loads(response_text).get("error", {})
                        error_code = error_data.get("code")
                    except Exception:
                        error_code = None

                    if error_code == 368:  # restricted
                        restricted_count += 1
                        print(f"     {RED}[REPLY] {YELLOW}{uid}  {BLUE}───────> {RED}ACCOUNT RESTRICTED → moved to ACCOUNTRESTRICTED.txt{RESET}")
                        move_bad_token(file_path, token_line, "restricted")

                    elif error_code == 190:  # invalid
                        invalid_count += 1
                        print(f"     {RED}[REPLY] {YELLOW}{uid}  {BLUE}───────> {RED}INVALID TOKEN → moved to INVALIDTOKEN.txt{RESET}")
                        move_bad_token(file_path, token_line, "invalid")

                    else:
                        print(f"     {RED}[REPLY] {YELLOW}{uid}  {BLUE}───────> {RED}FAILED TO REPLY: {response_text}{RESET}")

            except Exception as e:
                print(f"     {RED}[REPLY] {YELLOW}{uid}  {BLUE}───────> {RED}ERROR: {e}{RESET}")

    print(f"\n{blue}[REPLY] Process finished! ✅{reset}")
    print(f"{green}Successful replies: {success_count}{reset}")
    print(f"{red}Restricted accounts: {restricted_count}{reset}")
    print(f"{red}Invalid tokens: {invalid_count}{reset}")

def extract_group_id(group_input):
    """Extract numeric group ID from a URL or return input if already numeric."""
    match = re.search(r'groups/(\d+)', group_input)
    if match:
        return match.group(1)
    if group_input.isdigit():
        return group_input
    return None

def join_groupv1(group_id, profile_id, token_line):
    """Attempt to join a group using uid|pw|access_token|cookie|device_id|secret|UA format."""
    parts = token_line.strip().split('|')
    if len(parts) != 7:
        print(f"Invalid token format: {token_line}")
        return False

    uid = parts[0]
    access_token = parts[2]
    user_agent = parts[6]

    try:
        url = f'https://graph.facebook.com/{group_id}/members/{profile_id}'
        params = {'access_token': access_token}
        headers = {'user-agent': user_agent}
        response = requests.post(url, params=params, headers=headers)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

from concurrent.futures import ThreadPoolExecutor, as_completed

def perform_group_join():
    """Perform group joins based on user input."""
    blue = "\033[34m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    reset = "\033[0m"

    clear_screen()
    print_overview()

    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }

    print(f""" {blue}CHOOSE TYPE OF ACCOUNTS TO JOIN GROUP:{reset}
 {yellow}[1]{reset} {green}FRA ACCOUNT
 {yellow}[2]{reset} {green}FRA PAGES
 {yellow}[3]{reset} {green}RPW ACCOUNT
 {yellow}[4]{reset} {green}RPW PAGES
 {red}[0]{reset} EXIT
 {blue}───────────────────────────────────────────────────────────────{reset}""")

    try:
        file_choice = int(input(f"{green}Choose: {reset}"))
        if file_choice not in file_options:
            print(f"{red}Invalid choice{reset}")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print(f"{red}Please enter a valid number{reset}")
        return

    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            tokens = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{red}Error loading tokens: {e}{reset}")
        return

    if not tokens:
        print(f"{red}No tokens available{reset}")
        return

    try:
        start_line = int(input(f"{green}Enter starting line (1 to {len(tokens)}): {reset}"))
        if start_line < 1 or start_line > len(tokens):
            print(f"{red}Invalid line number{reset}")
            return
    except ValueError:
        print(f"{red}Please enter a valid number{reset}")
        return

    tokens = tokens[start_line - 1:]

    group_id_input = input(f"{green}Enter the group ID or URL: {reset}")
    group_id = extract_group_id(group_id_input)
    if not group_id:
        print(f"{red}Invalid group ID{reset}")
        return

    try:
        num_tokens = int(input(f"{green}Enter number of accounts to join: {reset}"))
        if num_tokens <= 0 or num_tokens > len(tokens):
            print(f"{red}Number exceeds available tokens{reset}")
            return
    except ValueError:
        print(f"{red}Invalid number{reset}")
        return

    join_count = 0
    failed_count = 0
    max_workers = 2

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_uid = {}
        for token in tokens[:num_tokens]:
            parts = token.split('|')
            if len(parts) < 3:
                print(f"{red}[FAILED]{reset} Invalid token format: {yellow}{token}{reset}")
                continue

            uid = parts[0]               # UID is first part
            # access_token = parts[2]    # still available if needed
            future = executor.submit(join_groupv1, group_id, uid, token)
            future_to_uid[future] = uid

        for future in as_completed(future_to_uid):
            uid = future_to_uid[future]
            try:
                success = future.result()
                if success:
                    join_count += 1
                    print(f"{green}[SUCCESS]{reset} {uid} joined group {group_id}")
                else:
                    failed_count += 1
                    print(f"{red}[FAILED]{reset} {uid} could not join group {group_id}")
            except Exception as e:
                print(f"{red}Error processing UID {uid}: {e}{reset}")

    print(f"{blue}───────────────────────────────────────────────────────────────{reset}")
    print(f"{green}TOTAL SUCCESSFUL: {join_count}{reset}")
    print(f"{red}TOTAL FAILED: {failed_count}{reset}")


def share_private(fb_token_line, post_url, privacy="SELF"):
    parts = fb_token_line.strip().split('|')
    if len(parts) != 7:
        return False  # Malformed line
    uid = parts[0]
    token = parts[2]
    ua_bgraph = parts[6]
    fb_url = 'https://graph.facebook.com/v13.0/me/feed'
    data = {
        'link': post_url,
        'published': '0',
        'privacy': f'{{"value":"{privacy}"}}',
        'access_token': token
    }
    headers = {'User-Agent': ua_bgraph}
    try:
        resp = rq.post(fb_url, data=data, headers=headers, timeout=10).json()
        return 'id' in resp
    except Exception:
        return False

# ========== Main Share Function ==========

from concurrent.futures import ThreadPoolExecutor
import threading, time, requests as rq

def perform_share_private():
    """Perform shares based on user input for file choice, starting line, post link, and number of shares."""
    # Step 1: File selection menu
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print(f"""     {white}CHOOSE TYPE OF SHARERS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice == 0:
            return
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load tokens
    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    if total_tokens == 0:
        print("⛔ No tokens available in file.")
        return
    print(f"📌 Total tokens in file: {total_tokens}")

    # Step 3: Ask start line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {total_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > total_tokens:
            print(f"Please enter a valid line number between 1 and {total_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    available_from_start = total_tokens - (start_line - 1)
    print(f"📌 Tokens available from line {start_line}: {available_from_start}")
    tokens = tokens[start_line - 1:]

    # Step 4: Ask for post URL
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_url = input(f"   {green}Enter the Facebook post URL: ").strip()

    # Handle /share/ redirects
    if '/share/' in post_url:
        try:
            response = rq.get(post_url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True, timeout=10)
            post_url = response.url
            print(f"🔄 Redirect resolved. Final URL: {post_url}")
        except Exception as e:
            print(f"⚠️ Error following redirect: {e}")
            return

    # Step 5: Ask desired number of shares (NO LIMIT check)
    try:
        max_shares = int(input(f"     {yellow}Enter your desired number of shares: "))
        if max_shares < 1:
            print("Please enter a number greater than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Reuse tokens if desired shares > available tokens
    if max_shares > len(tokens):
        print(f"⚠️ Desired shares ({max_shares}) exceed available tokens ({len(tokens)}).")
        repeats = (max_shares // len(tokens)) + 1
        tokens = (tokens * repeats)[:max_shares]
    else:
        tokens = tokens[:max_shares]

    # Step 6: Share loop
    completed = 0
    completed_lock = threading.Lock()
    failed_uids = []

    def worker(fb_token_line):
        nonlocal completed
        parts = fb_token_line.strip().split('|')
        uid = parts[0] if parts else "Unknown"

        success = share_public(fb_token_line, post_url, privacy="EVERYONE")
        if success:
            with completed_lock:
                completed += 1
                print(f"✅ Shares completed: {completed}/{max_shares}", end='\r')
        else:
            with completed_lock:
                failed_uids.append(uid)

        # Random delay between 2.8s and 9.6s
        time.sleep(random.uniform(2.8, 9.6))

    print("\n🚀 Starting share process...\n")
    with ThreadPoolExecutor(max_workers=5) as exe:
        for fb_token_line in tokens:
            exe.submit(worker, fb_token_line)

    # Step 7: Results
    print(f"\n✅ Finished. Total shares: {completed}/{max_shares}")
    if failed_uids:
        print("❌ Failed UIDs:")
        for uid in failed_uids:
            print(uid)
    print()

    
def share_public(fb_token_line, post_url, privacy="EVERYONE"):
    parts = fb_token_line.strip().split('|')
    if len(parts) != 7:
        return False  # Malformed line
    uid = parts[0]
    token = parts[2]
    ua_bgraph = parts[6]
    fb_url = 'https://graph.facebook.com/v13.0/me/feed'
    data = {
        'link': post_url,
        'published': '1',
        'privacy': f'{{"value":"{privacy}"}}',
        'access_token': token
    }
    headers = {'User-Agent': ua_bgraph}
    try:
        resp = rq.post(fb_url, data=data, headers=headers, timeout=10).json()
        return 'id' in resp
    except Exception:
        return False

# ========== Main Share Function ==========

def perform_share_public():
    """Perform shares based on user input for file choice, starting line, post link, and number of shares."""
    # Step 1: File selection menu
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE TYPE OF SHARERS: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  
    
    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice == 0:
            return
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load tokens
    tokens = load_tokens(file_path)
    total_tokens = len(tokens)
    if total_tokens == 0:
        print("⛔ No tokens available in file.")
        return
    print(f"📌 Total tokens in file: {total_tokens}")

    # Step 3: Ask start line
    try:
        start_line = int(input(f"    {green}Enter the starting line {red}(1 to {total_tokens}{red}): "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if start_line < 1 or start_line > total_tokens:
            print(f"Please enter a valid line number between 1 and {total_tokens}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    available_from_start = total_tokens - (start_line - 1)
    print(f"📌 Tokens available from line {start_line}: {available_from_start}")
    tokens = tokens[start_line - 1:]

    # Step 4: Ask for post URL
    print(f"    {green}FORMAT {yellow}: {red}https://www.facebook.com/100078043222260/posts/110105688267538/?mibextid=rS40aB7S9Ucbxw6v")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    post_url = input(f"   {green}Enter the Facebook post URL: ").strip()

    # Handle /share/ redirects
    if '/share/' in post_url:
        try:
            response = rq.get(post_url, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True, timeout=10)
            post_url = response.url
            print(f"🔄 Redirect resolved. Final URL: {post_url}")
        except Exception as e:
            print(f"⚠️ Error following redirect: {e}")
            return

    # Step 5: Ask max shares
    try:
        max_shares = int(input(f"     {yellow}Maximum number of shares to send (max {available_from_start}): "))
        if max_shares < 1 or max_shares > available_from_start:
            print(f"Please enter a number between 1 and {available_from_start}.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    tokens_to_use = tokens[:max_shares]

    # Step 6: Share loop
    completed = 0
    completed_lock = threading.Lock()
    failed_uids = []

    def worker(fb_token_line):
        nonlocal completed
        parts = fb_token_line.strip().split('|')
        uid = parts[0] if parts else "Unknown"

        success = share_public(fb_token_line, post_url, privacy="EVERYONE")
        if success:
            with completed_lock:
                completed += 1
                print(f"✅ Shares completed: {completed}/{max_shares}", end='\r')
        else:
            with completed_lock:
                failed_uids.append(uid)



    print("\n🚀 Starting share process...\n")
    with ThreadPoolExecutor(max_workers=1) as exe:
        for fb_token_line in tokens_to_use:
            exe.submit(worker, fb_token_line)
        # Random delay between 2.8s and 9.6s
        time.sleep(random.uniform(2.8, 9.6))

    # Step 7: Results
    print(f"\n✅ Finished. Total shares: {completed}/{max_shares}")
    if failed_uids:
        print("❌ Failed UIDs:")
        for uid in failed_uids:
            print(uid)
    print()

def refresh_token(uid, pw, ua, old_machine):
    """
    Refresh Facebook token using the same machine_id + UA for a stable long-lived token.
    Returns: (access_token, session_key, machine_id, secret) or (None, None, None, None) on failure.
    """
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'  # FB4A App Token

    headers = {
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'email': uid,
        'password': pw,
        'access_token': accessToken,
        'machine_id': old_machine,   # <-- Reuse old machine_id
        'device_id': old_machine     # <-- Reuse as device_id too
    }

    try:
        response = requests.post(
            'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true',
            data=data, headers=headers, timeout=15
        ).json()

        if 'access_token' in response:
            token = response['access_token']
            session_key = response.get('session_key', '')
            machine_id = response.get('machine_id', old_machine)
            secret = response.get('secret', '')
            return token, session_key, machine_id, secret

        else:
            print(f"[FAILED] {uid}: {response}")
            return None, None, None, None

    except Exception as e:
        print(f"[ERROR] {uid}: {e}")
        return None, None, None, None
        
def val_status(token_line):
    """
    Check a Facebook token and return its status.
    token_line format: uid|pw|token|session_key|machine_id|secret|ua_bgraph
    Returns: status string ("Alive", "Expired", "Checkpoint", "Disabled", "Invalid", "Malformed", "Request failed")
    """
    parts = token_line.strip().split('|')
    if len(parts) != 7:
        return "Malformed"

    token = parts[2]
    ua_bgraph = parts[6]

    url = f"https://graph.facebook.com/v20.0/me?access_token={token}"
    headers = {"User-Agent": ua_bgraph}
    time.sleep(random.uniform(5, 10))  # Delay between submissions

    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            try:
                data = response.json()
            except ValueError:
                if attempt < 2:
                    time.sleep(1)
                    continue
                print(f"[WARN] Non-JSON response for token {token}: {response.text[:100]}")
                return "Request failed"

            if response.status_code == 200 and "id" in data:
                return "Alive"
            elif "error" in data:
                err = data["error"]
                code = err.get("code")
                if code == 102:
                    return "Checkpoint"
                elif code == 368:
                    return "Disabled"
                elif code in [190, 102, 10]:  # common invalid codes
                    return "Expired"
                else:
                    return f"Invalid (code {code})"
            else:
                return "Request failed"

        except requests.RequestException as e:
            if attempt < 2:
                time.sleep(1)
                continue
            print(f"[ERROR] Request failed for token {token}: {e}")
            return "Request failed"

    return "Request failed"

def refresh_token_extraction():
    """Main menu for token extraction (formerly extraction)."""
    clear_screen()
    print_overview()
    print(f"     {white}[1] {yellow}EXTRACT {red}ACCOUNT")
    print(f"     {white}[2] {yellow}EXTRACT {red}PAGES")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {green}CHOICE: ").strip() 
    if choice == '1':
        refresh_token_ui2()
    elif choice == '2':
        refresh_token_ui2()
    else:
        print(f"     {red}INVALID CHOICE")

# ------------------------
def refresh_token_ui2():
    """UI for selecting file type and input for extraction (formerly axl1)."""
    clear_screen()
    print_overview()
    folder_path = "/sdcard/boostphere"
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[31m[01] \033[32mFRA EXTRACT ACCOUNT")
    print(f"     \033[31m[02] \033[32mFRA EXTRACT PAGES")
    print(f"     \033[31m[03] \033[32mRPW EXTRACT ACCOUNT")
    print(f"     \033[31m[04] \033[32mRPW EXTRACT PAGES")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    
    save_choice = input(f"     \033[32mCHOICE: ").strip()

    if save_choice == '1':
        account_file = os.path.join(folder_path, "FRAACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '2':
        account_file = os.path.join(folder_path, "FRAPAGES.txt")
        extract_type = 'page'
    elif save_choice == '3':
        account_file = os.path.join(folder_path, "RPWACCOUNT.txt")
        extract_type = 'account'
    elif save_choice == '4':
        account_file = os.path.join(folder_path, "RPWPAGES.txt")
        extract_type = 'page'
    else:
        print("Invalid choice. Exiting.")
        return

    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    print(f"     \033[33mTHE FORMAT SHOULD BE \033[31muid|pass")
    print(f"    \033[34m───────────────────────────────────────────────────────────────\033[0m")
    file_path = input(f"     \033[33mPATH: ").strip()

    refresh_token_function(file_path, account_file, extract_type)


def refresh_token_function(accounts_file, token_output_path, extract_type):
    """Process accounts and refresh tokens concurrently (overwrite mode)."""
    refreshed_lines = []
    success_count = []

    try:
        with open(accounts_file, 'r', encoding='utf-8') as file:
            accounts = [line.strip() for line in file if '|' in line.strip()]

        if not accounts:
            print(f"No valid accounts found in {accounts_file}.")
            return

        def process_account(line):
            parts = line.split('|')
            if len(parts) < 7:
                return None  # malformed line

            uid, pw, old_token, old_session, old_machine, old_secret, ua = parts

            # only refresh token (keep old session/machine/secret/ua)
            token, _, _, _ = refresh_token(uid, pw, ua, old_machine)
            if token is None:
                print(f"[{uid}] Failed to refresh token")
                return None

            # build new line (only token replaced)
            new_line = f"{uid}|{pw}|{token}|{old_session}|{old_machine}|{old_secret}|{ua}\n"
            success_count.append((uid))
            print(f"[{uid}] Token refreshed ✅")
            return new_line

        with ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(process_account, accounts))

        # collect only successful ones
        refreshed_lines = [line for line in results if line is not None]

        # append to file (instead of overwriting)
        with open(token_output_path, 'a', encoding='utf-8') as f_out:
            f_out.writelines(refreshed_lines)

        print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")
        print(f"     \033[1;34m[SUCCESS]\033[0m: {len(success_count)} {extract_type}(s) successfully refreshed.")
        print("    \033[1;37m───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
        return

def fetch_account_info(file_options):
    """
    Fetch account info and associated pages from a file with 7-field token format:
    uid|pw|token|session_key|machine_id|secret|ua_bgraph
    """
    clear_screen()
    print(f"     {yellow}CHOOSE WHICH FILE YOU WANT TO CHECK:")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    for key, value in file_options.items():
        print(f"     {red}[{key}] {yellow}{value.split('/')[-1]}")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    try:
        file_choice = int(input(f"  {red}Choose: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    accounts_file = file_options.get(file_choice)
    if not accounts_file:
        print("Invalid choice. Exiting.")
        return

    try:
        with open(accounts_file, 'r') as file:
            accounts = [line.strip() for line in file if line.strip()]

        for account_line in accounts:
            parts = account_line.split('|')
            if len(parts) != 7:
                print(f"[WARNING] Malformed line, skipping: {account_line}")
                continue

            uid, pw, token, session_key, machine_id, secret, ua_bgraph = parts

            # Fetch account info
            account_info = get_account_info(token)
            account_name = account_info.get('name') if account_info and 'name' in account_info else 'No name available'
            print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            if account_info:
                print(f"     {yellow}ACCOUNT NAME {red}: {green}{account_name} (UID: {uid})")
            else:
                print(f"     {yellow}FAILED TO FETCH ACCOUNT INFORMATION ! {white}= {red}{uid}")
                continue  # skip page fetching if account info failed

            # Fetch pages
            pages = extract_fb_pages(token, ua_bgraph)
            if pages and isinstance(pages, list) and len(pages) > 0:
                print(f"\n          {yellow}PAGES ASSOCIATED WITH {white}: {red}{account_name}")
                for page in pages:
                    page_name = page.get('name', 'No name available')
                    page_id = page.get('id', 'No ID')
                    print(f"       👉 {yellow}{page_name} {white}= {green}PAGE ID: {red}{page_id}")
                print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
            else:
                print(f"     {red}NO PAGES ASSOCIATED WITH THIS ACCOUNT !")
                print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    except FileNotFoundError:
        print(f"File not found: {accounts_file}")
    except Exception as e:
        print(f"[ERROR] {str(e)}")


def get_account_info(token):
    url = 'https://graph.facebook.com/v18.0/me'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"[ERROR] Error fetching account info: {str(e)}")
        return None

# File options mapping
file_options = {
    1: "/sdcard/boostphere/FRAACCOUNT.txt",
    2: "/sdcard/boostphere/FRAPAGES.txt",
    3: "/sdcard/boostphere/RPWACCOUNT.txt",
    4: "/sdcard/boostphere/RPWPAGES.txt"
}

def extract_fb_pages(token, ua_bgraph=None):
    """
    Extract pages associated with a Facebook account.
    Returns a list of pages, each page is a dict with 'name' and 'id'.
    """
    url = "https://graph.facebook.com/v18.0/me/accounts"
    params = {
        "fields": "name,id",  # ensure name and id are returned
        "access_token": token
    }
    headers = {"User-Agent": ua_bgraph} if ua_bgraph else {}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        pages = data.get("data", [])
        # Ensure each page has name and id keys
        valid_pages = []
        for p in pages:
            page_name = p.get('name', 'No name available')
            page_id = p.get('id', 'No ID')
            valid_pages.append({'name': page_name, 'id': page_id})
        return valid_pages
    except Exception as e:
        print(f"[ERROR] Error fetching pages: {str(e)}")
        return []

def check_ua_line(line, retries=2):
    """
    Check if a token + UA combo is valid.
    Returns: status string ("UA Safe", "Token Expired", "Token Invalid", "Request Failed")
    """
    parts = line.strip().split('|')
    if len(parts) != 7:
        return "Malformed"

    uid, pw, token, session_key, machine_id, secret, ua = parts

    url = f"https://graph.facebook.com/v20.0/me?access_token={token}"
    headers = {"User-Agent": ua}

    for attempt in range(retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "id" in data:
                    return "UA Safe"  # Token works with this UA
            elif response.status_code == 400 or response.status_code == 401:
                data = response.json()
                err = data.get("error", {})
                code = err.get("code")
                subcode = err.get("error_subcode")
                # Identify expired or checkpoint tokens
                if code == 102:
                    return "Token Expired"
                elif code == 368 or code == 190:
                    return "Token Invalid"
            else:
                return "Request Failed"
        except requests.RequestException:
            if attempt < retries:
                time.sleep(1)
                continue
            return "Request Failed"
    return "Request Failed"


def check_ua_file(file_path):
    """
    Check all accounts in a file for UA + token validity.
    Saves only valid UA/token combos back to file.
    """
    valid_lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        status = check_ua_line(line)
        parts = line.strip().split('|')
        uid = parts[0] if len(parts) >= 1 else "Unknown"
        print("───────────────────────────────────────────────")
        if status == "UA Safe":
            print(f"✅ ACCOUNT {uid}: UA safe / token works")
            valid_lines.append(line.strip())
        elif status == "Token Expired":
            print(f"⚠️ ACCOUNT {uid}: Token expired / needs refresh")
        elif status == "Token Invalid":
            print(f"❌ ACCOUNT {uid}: Token invalid / disabled")
        elif status == "Malformed":
            print(f"❌ ACCOUNT {uid}: Malformed line / skipped")
        else:
            print(f"⚠️ ACCOUNT {uid}: Request failed / retry later")

    # Save only UA-safe lines back
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in valid_lines:
            f.write(line + "\n")
    print(f"\nCheck complete. {len(valid_lines)} UA-safe accounts saved back.")

def token_validation():
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt"
    }
    clear_screen()
    print_overview()
    print(f"""     {white}CHOOSE ACCOUNT TO CHECK: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  
    try:
        choice = int(input(f"     Enter your choice: "))
    except ValueError:
        print("Invalid input. Exiting...")
        return

    if choice == 0:
        print("Exiting...")
        return
    elif choice not in file_options:
        print("Invalid choice. Exiting...")
        return

    file_path = file_options[choice]
    print(f"     {blue}COPY THIS /sdcard/boostphere/_invalid.txt{reset}")
    # Ask for custom invalid tokens path
    invalid_file_path = input("    Enter full path for invalid tokens file : ").strip()
    if not invalid_file_path:
        # default fallback
        base_dir, base_name = os.path.split(file_path)
        invalid_file_path = os.path.join(base_dir, f"_{base_name.split('.')[0]}_invalid.txt")

    # Ensure folder exists
    invalid_dir = os.path.dirname(invalid_file_path)
    if invalid_dir and not os.path.exists(invalid_dir):
        os.makedirs(invalid_dir, exist_ok=True)

    # Read tokens
    if not os.path.exists(file_path):
        print(f"{red}File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    valid_tokens = []
    invalid_tokens = []

    for line in lines:
        parts = line.strip().split('|')
        if len(parts) != 7:
            print(f"{red}Malformed line, skipping: {line.strip()}")
            invalid_tokens.append(line.strip())
            continue

        uid = parts[0]
        status = val_status(line)

        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if status == "Alive":
            valid_tokens.append(line.strip())
            print(f"     {green}ACCOUNT ─────> {blue}{uid} {white}= {yellow}IS VALID")
        else:
            invalid_tokens.append(line.strip())
            print(f"     {red}ACCOUNT ─────> {blue}{uid} {white}= {yellow}{status} - MOVED TO INVALID")

    # Save valid tokens
    with open(file_path, 'w', encoding='utf-8') as file:
        for token_line in valid_tokens:
            file.write(token_line + "\n")

    # Save invalid tokens to custom path
    with open(invalid_file_path, 'a', encoding='utf-8') as file:
        for token_line in invalid_tokens:
            file.write(token_line + "\n")

    print(f"{green}Check complete. Valid tokens remain in {file_path}")
    print(f"{red}Invalid tokens moved to {invalid_file_path}")

def shuffle_accounts_ui():
    """Shuffle accounts in a text file with the same UI style as perform_reaction_fastes."""
    clear_screen()
    print_overview()  # show your standard logo at the top
    # Step 1: Ask the user which file to shuffle
    file_options = {
        1: "/sdcard/boostphere/FRAACCOUNT.txt",
        2: "/sdcard/boostphere/FRAPAGES.txt",
        3: "/sdcard/boostphere/RPWACCOUNT.txt",
        4: "/sdcard/boostphere/RPWPAGES.txt",
        5: "/sdcard/boostphere/id.txt"  # optional default token file
    }

    print(f"""     {white}CHOOSE FILE TO SHUFFLE: 
     {blue}[1] {green}FRA ACCOUNT 
     {blue}[2] {green}FRA PAGES
     {blue}[3] {green}RPW ACCOUNT
     {blue}[4] {green}RPW PAGES
     {blue}[5] {green}ID TXT
     {red}[0]  {red} EXIT 
    {blue}───────────────────────────────────────────────────────────────\033[0m""")  

    try:
        file_choice = int(input(f"    {green}Choose:  "))
        print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
        if file_choice == 0:
            return
        if file_choice not in file_options:
            print("Invalid choice.")
            return
        file_path = file_options[file_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    # Step 2: Load the file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    if not lines:
        print(f"No lines found in {file_path}.")
        return

    # Step 3: Shuffle
    random.shuffle(lines)

    # Step 4: Save back
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(line + "\n" for line in lines)
        print(f"{green}Shuffling done! File saved: {yellow}{file_path}")
    except Exception as e:
        print(f"{red}Error saving shuffled file: {e}")

    print(f"{blue}───────────────────────────────────────────────────────────────\033[0m")

def print_overview():
    logo()
    reset = "\033[0m"
    """Show stored accounts & pages overview."""
    # Make sure files exist
    for path in ['/sdcard/boostphere/FRAACCOUNT.txt',
                 '/sdcard/boostphere/FRAPAGES.txt',
                 '/sdcard/boostphere/RPWACCOUNT.txt',
                 '/sdcard/boostphere/RPWPAGES.txt']:
        open(path, 'a').close()

    # Count accounts and pages
    total_accounts, total_pages = count_tokens('/sdcard/boostphere/FRAACCOUNT.txt',
                                               '/sdcard/boostphere/FRAPAGES.txt')
    total_account_rpw, total_pages_rpw = count_tokens('/sdcard/boostphere/RPWACCOUNT.txt',
                                                      '/sdcard/boostphere/RPWPAGES.txt')

    print(f"""
      {blue}──────────────────────────────────────────────────────────────{reset}
                 {blue}OVERVIEW OF STORED ACCOUNT & PAGES💫{reset}
          
                            {red}FRA ACCOUNT{reset} : {yellow}{total_accounts}{reset}
                            {red}FRA PAGES{reset}   : {yellow}{total_pages}{reset}
                            {red}RPW ACCOUNT{reset} : {yellow}{total_account_rpw}{reset}
                            {red}RPW PAGES{reset}   : {yellow}{total_pages_rpw}{reset}
      {blue}──────────────────────────────────────────────────────────────{reset}
    """)

def clear_text_files():
    """
    Clear the contents of specified text files based on user choice.
    """
    clear_screen()  # Assuming clear_screen is defined elsewhere
    print_overview()         # Assuming jovan is defined elsewhere

    # Dictionary of file paths for resetting
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }

    print(f"     {blue}Choose File To Reset:")
    print(f"     {yellow}[01]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[02]  {blue}FRA PAGES")
    print(f"     {yellow}[03]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[04]  {blue}RPW PAGES")
    print(f"     {yellow}[05]  {blue}All files")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")

    user_choice = input(f"    {red}Enter your choice: ").strip()

    # Clear all files if option 5 is selected
    if user_choice == '5':
        for file_path in file_paths.values():
            try:
                with open(file_path, 'w') as file:
                    file.truncate(0)  # Clear the file content
                print(f"Successfully cleared: {file_path}")
            except Exception as e:
                print(f"Error clearing {file_path}: {str(e)}")
        return

    # Handle clearing a single file based on the user's choice
    selected_file = file_paths.get(user_choice)
    if selected_file:
        try:
            with open(selected_file, 'w') as file:
                file.truncate(0)  # Clear the file content
            print(f"Successfully cleared: {selected_file}")
        except Exception as e:
            print(f"Error clearing {selected_file}: {str(e)}")
    else:
        print("Invalid choice. Please enter a valid number.")


def transfer_file_content():
    while True:
        print(f"     {white}CHOOSE FILE TO TRANSFER{reset}")
        print(f"     {yellow}[1]  {blue}FRA ACCOUNT{reset}")
        print(f"     {yellow}[2]  {blue}FRA PAGES{reset}")
        print(f"     {yellow}[3]  {blue}RPA ACCOUNT{reset}")
        print(f"     {yellow}[4]  {blue}RPA PAGES{reset}")
        print(f"     {yellow}[0]  {blue}EXIT{reset}")
        try:
            source_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if source_choice == 0:
            return main()
        if source_choice not in file_options:
            print("Invalid option. Try again.")
            continue

        source_file = file_options[source_choice]
        if not os.path.exists(source_file):
            print(f"File not found: {source_file}")
            continue

        # now choose destination
        while True:
            print("""
            CHOOSE DESTINATION FILE:
            [1] FRA ACCOUNT
            [2] FRA PAGES
            [3] RPW ACCOUNT
            [4] RPW PAGES
            [0] CANCEL
            """)
            try:
                dest_choice = int(input("Enter destination: "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if dest_choice == 0:
                main()
            if dest_choice not in file_options:
                print("Invalid option. Try again.")
                continue

            dest_file = file_options[dest_choice]

            # prevent transferring into same file
            if source_file == dest_file:
                print("Source and destination are the same! Choose different files.")
                continue

            # transfer (append all source lines to destination)
            with open(source_file, "r", encoding="utf-8") as src:
                lines = src.readlines()

            with open(dest_file, "a", encoding="utf-8") as dst:
                dst.writelines(lines)

            # clear source file
            open(source_file, "w", encoding="utf-8").close()

            print(f"✅ Transferred {len(lines)} lines from {os.path.basename(source_file)} → {os.path.basename(dest_file)}")
            return

def remove_duplicates():
    clear_screen()
    print_overview()
    file_paths = {
        "1": "/sdcard/boostphere/FRAACCOUNT.txt",
        "2": "/sdcard/boostphere/FRAPAGES.txt",
        "3": "/sdcard/boostphere/RPWACCOUNT.txt",
        "4": "/sdcard/boostphere/RPWPAGES.txt"
    }
    
    print(f"     {red}Choose which file to remove duplicates from:")
    print(f"     {yellow}[1]  {blue}FRA ACCOUNT")
    print(f"     {yellow}[2]  {blue}FRA PAGES")
    print(f"     {yellow}[3]  {blue}RPW ACCOUNT")
    print(f"     {yellow}[4]  {blue}RPW PAGES")
    print(f"    {blue}───────────────────────────────────────────────────────────────\033[0m")
    choice = input(f"     {white}Enter your choice: ").strip()
    
    if choice not in file_paths:
        print("Invalid choice. Please try again.")
        return
    
    file_path = file_paths[choice]
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        seen_uids = set()  # To store unique uids
        unique_lines = []

        for line in lines:
            # Split the line into 'uid' and 'password'
            if '|' in line:
                uid, password = line.split('|', 1)  # Split only at the first '|'
                if uid not in seen_uids:
                    unique_lines.append(line)  # Keep the line if 'uid' is unique
                    seen_uids.add(uid)  # Add the 'uid' to the set
        
        # Write the unique lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(unique_lines)
        
        print(f"     {green}Successfully removed duplicates from: {file_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


import os
import random
import time
import requests

import os
import random
import time
import requests

BASE_URL = "https://b-graph.facebook.com"
DIRECTORY = r"C:\Users\ADMIN\Pictures\new"  # Your photos folder

# Load tokens

# Fetch fb_dtsg for a token
def fetch_fb_dtsg(token, ua):
    try:
        headers = {"User-Agent": ua}
        resp = requests.get(f"{BASE_URL}/me?access_token={token}", headers=headers).json()
        fb_dtsg = resp.get("fb_dtsg")  # Some tokens include fb_dtsg in the response
        return fb_dtsg
    except Exception as e:
        print(f"Failed to fetch fb_dtsg: {e}")
        return None

# Upload profile picture via b-graph
def upload_profile_picture(token, ua, file_path, fb_dtsg=None, bio=None, location=None):
    try:
        with open(file_path, 'rb') as f:
            files = {'source': f}
            data = {"access_token": token, "profile": 1}
            if fb_dtsg:
                data["fb_dtsg"] = fb_dtsg
            if bio:
                data["about"] = bio
            if location:
                data["location"] = location
            headers = {"User-Agent": ua}
            url = f"{BASE_URL}/me/photos"
            resp = requests.post(url, files=files, data=data, headers=headers).json()
            return resp
    except Exception as e:
        return {"error": str(e)}

# Main function
def start():
    token_file_path = input("Enter the path to your token file: ").strip()
    tokens = load_tokens(token_file_path)
    if not tokens:
        print("No valid tokens found.")
        return

    if not os.path.exists(DIRECTORY):
        print(f"Directory not found: {DIRECTORY}")
        return

    photos = os.listdir(DIRECTORY)
    if not photos:
        print(f"No photos found in {DIRECTORY}")
        return

    for t in tokens:
        fb_dtsg = fetch_fb_dtsg(t["token"], t["ua"])
        photo_file = os.path.join(DIRECTORY, random.choice(photos))
        result = upload_profile_picture(t["token"], t["ua"], photo_file, fb_dtsg=fb_dtsg)
        if "error" in result:
            print(f"❌ Failed for {t['uid']}: {result['error']}")
        elif "id" in result:
            print(f"✅ Uploaded profile picture for {t['uid']} - Photo ID: {result['id']}")
        else:
            print(f"❌ Unknown failure for {t['uid']}: {result}")
        time.sleep(2)  # avoid rate limits

# Menu
def set_profile():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========= PROFILE PICTURE UPLOADER =========")
        print("[1] Set Profile Picture")
        print("[0] Exit")
        print("============================================")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            start()
            input("Press Enter to return to menu...")
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

def main():
    # Softer ANSI colors
    blue = "\033[34m"     # dark blue
    red = "\033[31m"      # dark red
    yellow = "\033[33m"   # dark yellow
    green = "\033[32m"    # green
    reset = "\033[0m"

    while True:
    
        # Make sure files exist
        for path in ['/sdcard/boostphere/FRAACCOUNT.txt',
                     '/sdcard/boostphere/FRAPAGES.txt',
                     '/sdcard/boostphere/RPWACCOUNT.txt',
                     '/sdcard/boostphere/RPWPAGES.txt']:
            open(path, 'a').close()

        # Count accounts and pages
        total_accounts, total_pages = count_tokens('/sdcard/boostphere/FRAACCOUNT.txt',
                                                   '/sdcard/boostphere/FRAPAGES.txt')
        total_account_rpw, total_pages_rpw = count_tokens('/sdcard/boostphere/RPWACCOUNT.txt',
                                                          '/sdcard/boostphere/RPWPAGES.txt')
        logo()
        print(f"""
      {blue}──────────────────────────────────────────────────────────────{reset}
                 {blue}OVERVIEW OF STORED ACCOUNT & PAGES💫{reset}
          
                            {red}FRA ACCOUNT{reset} : {yellow}{total_accounts}{reset}
                            {red}FRA PAGES{reset}   : {yellow}{total_pages}{reset}
                            {red}RPW ACCOUNT{reset} : {yellow}{total_account_rpw}{reset}
                            {red}RPW PAGES{reset}   : {yellow}{total_pages_rpw}{reset}
      {blue}──────────────────────────────────────────────────────────────{reset}
                           {blue}Services We Offer✨{reset}

      {WHITE}[ 01 ]{reset} {blue}EXTRACTION{reset}                    {yellow}- [PAGE & ACCOUNT]{reset}
      {WHITE}[ 02 ]{reset} {blue}REACT TO POST V1{reset}              {yellow}- [PAGE]{reset}
      {WHITE}[ 03 ]{reset} {blue}REACT TO POST V2{reset}              {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 04 ]{reset} {blue}AUTO COMMENT{reset}                  {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 05 ]{reset} {blue}COMMENT REPLY{reset}                 {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 06 ]{reset} {blue}COMMENT REACT{reset}                 {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 07 ]{reset} {blue}AUTO FOLLOW{reset}                   {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 08 ]{reset} {blue}AUTO PAGE LIKES & FOLLOWERS{reset}   {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 09 ]{reset} {blue}AUTO GROUP JOIN{reset}               {yellow}- [ACCOUNT]{reset}
      {blue}──────────────────────────────────────────────────────────────{reset}
      {WHITE}[ 10 ]{reset} {blue}AUTO SHARE PUBLIC{reset}             {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 11 ]{reset} {blue}AUTO SHARE PRIVATE{reset}            {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 12 ]{reset} {blue}AUTO SHUFFLE TOKEN{reset}            {yellow}- [PAGE & ACCOUNT]{reset}
      {blue}──────────────────────────────────────────────────────────────{reset}
      {WHITE}[ 13 ]{reset} {blue}TOKEN VALIDATION{reset}              {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 14 ]{reset} {blue}TOKEN REFRESHER{reset}               {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 15 ]{reset} {blue}ACCOUNT CHECKER{reset}               {yellow}- [ACCOUNT]{reset}
      {WHITE}[ 16 ]{reset} {RED}RESET TOOL{reset}                    
      {WHITE}[ 17 ]{reset} {blue}TRANSFER ACCOUNT{reset}              {yellow}- [PAGE & ACCOUNT]{reset}
      {WHITE}[ 18 ]{reset} {blue}REMOVE DUPLICATE ACCOUNT{reset}      {yellow}- [PAGE & ACCOUNT]{reset}
      {WHITE}[ 19 ]{reset} {blue}AUTO FOLLOW USING PAGE{reset}        {yellow}- [PAGE]{reset}
      {WHITE}[ 20 ]{reset} {RED}EXIT TOOL{reset} 
      {blue}──────────────────────────────────────────────────────────────{reset}
        """)

        choice = input("CHOICE: ").strip()

        # Execute choice
        if choice == '1':
            extraction()
        elif choice == '2':
            perform_reaction_pages()
        elif choice == '3':
            Perform_reactionV2()
        elif choice == '4':
            comment_function()
        elif choice == '5':
            comment_reply()
        elif choice == '6':
            comment_react()
        elif choice == '7':
            perform_auto_follow_function()
        elif choice == '8':
            like_facebook_page_function()
        elif choice == '9':
            perform_group_join()
        elif choice == '10':
            perform_share_public()
        elif choice == '11':
            perform_share_private()
        elif choice == '12':
            shuffle_accounts_ui()
        elif choice == '13':
            token_validation()
        elif choice == '14':
            refresh_token_extraction()
        elif choice == '15':
            fetch_account_info(file_options)
        elif choice == '16':
            clear_text_files()
        elif choice == '17':
            transfer_file_content()
        elif choice == '18':
            remove_duplicates()
        elif choice == '19':
            perform_auto_follow_for_page()
        elif choice == '20':
            print("Exiting...")
            break
        else:
            print(f"{reset}Invalid choice.")

        input("\nPress ENTER to return to menu...")

if __name__ == "__main__":
    main()
