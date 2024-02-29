from my_imports import *

def get_random_user_agent():
    
    # Define a custom user agents for ua rotation
    user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' 
    ]
    # Returns a random user agent from the user_agent_list.
    return random.choice(user_agent_list)

def calling_options():
    # Allows you to cusotmize: ingonito mode, maximize window size, headless browser, disable certain features, etc
    option= webdriver.ChromeOptions()

    # Going undercover:
    option.add_argument("--incognito")

    # Consider this if the application works and you know how it works for speed ups and rendering!

    option.add_argument('--headless')

    option.add_argument("--no-sandbox")  # Bypass OS security model
    option.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    user_agent = get_random_user_agent()
    option.add_argument(f"user-agent={user_agent}")
    return option

def get_random_feed():
    return random.choice(feed)

# chromedriver_autoinstaller.install()

