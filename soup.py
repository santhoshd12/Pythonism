from bs4 import BeautifulSoup
print(BeautifulSoup)
import requests
from bs4 import BeautifulSoup
url = "https://github.com/Keerthiga-28/php-website.git"
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the webpage.\n")
else:
    print("Failed to retrieve the webpage")
    exit()
soup = BeautifulSoup(response.content, 'html.parser')
# Check for headers (h1, h2)
print("Checking for headers...")
h1_tags = soup.find_all('h1')
h2_tags = soup.find_all('h2')
if h1_tags:
    print(f"Found {len(h1_tags)} <h1> tags:")
    for h1 in h1_tags:
        print(f" - {h1.get_text(strip=True)}")
else:
    print("No <h1> tags found.")
if h2_tags:
    print(f"\nFound {len(h2_tags)} <h2> tags:")
    for h2 in h2_tags:
        print(f" - {h2.get_text(strip=True)}")
else:
    print("No <h2> tags found.")
# Check for links
print("\nChecking for links...")
links = soup.find_all('a', href=True)
print(f"Found {len(links)} links:")
for link in links[:5]:  # Display only the first 5 links 
    print(f" - {link.get('href')}")
print("\nChecking for forms...")
forms = soup.find_all('form')
print(f"Found {len(forms)} forms.")
for form in forms:
    action = form.get('action', 'No action specified')
    method = form.get('method', 'No method specified')
    print(f" - Form action: {action}, method: {method}")
print("\nChecking for buttons...")
buttons = soup.find_all('button')
submit_inputs = soup.find_all('input', {'type': 'submit'})
print(f"Found {len(buttons)} <button> tags and {len(submit_inputs)} submit inputs.")
for button in buttons[:5]:
    print(f" - Button: {button.get_text(strip=True)}")
for submit in submit_inputs[:5]:
    print(f" - Submit input: {submit.get('name') or 'No name'}")
