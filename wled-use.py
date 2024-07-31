import requests
import keyboard

def turn_on_wled(ip):
    url = f"http://{ip}/win&T=1"  # URL pro zapnutí WLED pásku
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"WLED na {ip} zapnuto.")
        else:
            print(f"Chyba při zapínání WLED na {ip}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Nelze se připojit k WLED na {ip} - {e}")

def turn_off_wled(ip):
    url = f"http://{ip}/win&T=0"  # URL pro vypnutí WLED pásku
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"WLED na {ip} vypnuto.")
        else:
            print(f"Chyba při vypínání WLED na {ip}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Nelze se připojit k WLED na {ip} - {e}")

def set_wled_color(ip, r, g, b):
    url = f"http://{ip}/win&R={r}&G={g}&B={b}"  # URL pro nastavení barvy WLED pásku
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Barva WLED na {ip} nastavena na ({r}, {g}, {b}).")
        else:
            print(f"Chyba při nastavení barvy WLED na {ip}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Nelze se připojit k WLED na {ip} - {e}")

if __name__ == "__main__":
    wled_ip = input("Zadejte IP adresu WLED zařízení: ")
    
    print("Stiskněte ESC pro ukončení programu.")
    
    while True:
        if keyboard.is_pressed('esc'):
            print("Program ukončen.")
            break
        
        action = input("Chcete zapnout, vypnout nebo nastavit barvu WLED? (zapnout/vypnout/barva): ").strip().lower()
        
        if action == 'zapnout':
            turn_on_wled(wled_ip)
        elif action == 'vypnout':
            turn_off_wled(wled_ip)
        elif action == 'barva':
            r = int(input("Zadejte hodnotu červené (0-255): "))
            g = int(input("Zadejte hodnotu zelené (0-255): "))
            b = int(input("Zadejte hodnotu modré (0-255): "))
            set_wled_color(wled_ip, r, g, b)
        else:
            print("Neplatná volba. Prosím zvolte 'zapnout', 'vypnout' nebo 'barva'.")
