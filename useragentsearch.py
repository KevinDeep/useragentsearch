import user_agents
from termcolor import colored
print("\033[92m  _    _                                                         _               _____                                _  \033[0m")   
print("\033[92m | |  | |                         /\                            | |             / ____|                              | |  \033[0m")  
print("\033[92m | |  | |  ___    ___   _ __     /  \      __ _    ___   _ __   | |_   ______  | (___     ___    __ _   _ __    ___  | |__\033[0m ") 
print("\033[92m | |  | | / __|  / _ \ | '__|   / /\ \    / _` |  / _ \ | '_ \  | __| |______|  \___ \   / _ \  / _` | | '__|  / __| | '_ \ \033[0m")
print("\033[92m | |__| | \__ \ |  __/ | |     / ____ \  | (_| | |  __/ | | | | | |_            ____) | |  __/ | (_| | | |    | (__  | | | |\033[0m")
print("\033[92m  \____/  |___/  \___| |_|    /_/    \_\  \__, |  \___| |_| |_|  \__|          |_____/   \___|  \__,_| |_|     \___| |_| |_|\033[0m")
print("\033[92m                                           __/ |                                                                          \033[0m")  
print("\033[92m                                          |___/                                                                           \033[0m")  
print("\033[92m                           <======= 𝐓𝐨𝐨𝐥𝐬  𝐂𝐫𝐞𝐚𝐭𝐞𝐝  𝐁𝐲  𝐊𝐞𝐯𝐢𝐧 𝐃𝐞𝐞𝐩 【𝐀𝐫𝐜𝐡𝐚𝐧𝐠𝐞𝐥 𝐖𝐡𝐢𝐭𝐞】=======> \033[0m")
def analyze_user_agent(user_agent_string):
    ua = user_agents.parse(user_agent_string)

    information = {
        "Device": {
            colored("Model", 'white', attrs=['bold']): ua.device.family,
            colored("Brand", 'white', attrs=['bold']): ua.device.brand,
        },
        "Operating System": {
            colored("Name", 'white', attrs=['bold']): ua.os.family,
            colored("Version", 'white', attrs=['bold']): ua.os.version_string,
        },
        "Browser": {
            colored("Name", 'white', attrs=['bold']): ua.browser.family,
            colored("Version", 'white', attrs=['bold']): ua.browser.version_string,
        },
        colored("Is Mobile Device?", 'white', attrs=['bold']): ua.is_mobile,
        colored("Is a Bot?", 'white', attrs=['bold']): ua.is_bot,
        colored("Is Tablet Device?", 'white', attrs=['bold']): ua.is_tablet,
        colored("Supports Cookies?", 'white', attrs=['bold']): ua.is_pc,
    }

    return information

# Add a blank line before the "Enter the User-Agent" prompt
print()
user_agent_string = input(colored("Enter the User-Agent to analyze: ", 'green', attrs=['bold']))

# Perform analysis
info = analyze_user_agent(user_agent_string)

# Print formatted information with blank lines between sections
for category, data in info.items():
    if category == "Device":
        print()  # Add a blank line before "Device"
    print(colored(f"{category}:", 'green', attrs=['bold']))
    if isinstance(data, bool):
        # Handle boolean information
        print(f"  {colored(str(data), 'green', attrs=['bold'])}")
    else:
        for key, value in data.items():
            if value is not None:
                print(f"  {key}: {colored(value, 'green', attrs=['bold'])}")
    print()  # Add a blank line between categories
