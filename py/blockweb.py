from datetime import datetime

redirect = "127.0.0.1"
sites = ['www.youtube.com', 'www.facebook.com']
path = 'C:/Windows/System32/drivers/etc/hosts'


def block_site(sites, r=redirect, path=path):
    try:
        with open(path, 'r+') as file:
            content = file.read()
            for site in sites:
                if site not in content:
                    file.write(f'{r} {site}\n')
                    print(f'Redirect added for {site}')
    except PermissionError:
        print('Permission denied to modify the hosts file. Please run the script as an administrator.')
    except Exception as e:
        print(f"An error occurred: {e}")


def unblock_websites(sites, path=path):
    try:
        with open(path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in sites):
                    file.write(line)
            file.truncate()
            print('Redirect removed for websites')
    except PermissionError:
        print('Permission denied to modify the hosts file. Please run the script as an administrator.')
    except Exception as e:
        print(f"An error occurred: {e}")


# Main interaction logic
choice = input('Do you want to block or unblock the website (b/u): ').lower()

if choice == 'b':
    n = int(input('How many websites do you want to block: '))
    new_sites = []
    for i in range(n):
        site = input(f'Enter website #{i + 1} (e.g., www.example.com): ').strip()
        new_sites.append(site)
    block_site(new_sites)

elif choice == 'u':
    n = int(input('How many websites do you want to unblock: '))
    sites_to_unblock = []
    for i in range(n):
        site = input(f'Enter website #{i + 1} (e.g., www.example.com): ').strip()
        sites_to_unblock.append(site)
    unblock_websites(sites_to_unblock)

else:
    print("Invalid choice! Please enter 'b' to block or 'u' to unblock.")
