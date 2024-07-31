from scapy.all import ARP, Ether, srp
import requests

def scan(ip_range):
    # Vytvoří ARP požadavek pro daný rozsah IP adres
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    # Odeslat ARP požadavek a přijmout odpovědi
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device_info = {
            'ip': element[1].psrc,
            'mac': element[1].hwsrc
        }
        devices_list.append(device_info)

    return devices_list

def is_wled_device(ip):
    try:
        # Pokusí se připojit k webovému rozhraní zařízení WLED na portu 80
        response = requests.get(f'http://{ip}', timeout=2)
        if response.status_code == 200:
            # Může být přítomno v HTML kódu zařízení
            if "WLED" in response.text:
                return True
    except requests.RequestException:
        pass
    return False

def print_results(devices_list):
    print("IP Address\t\tMAC Address\t\tType")
    print("-----------------------------------------")
    for device in devices_list:
        device_type = "WLED" if is_wled_device(device['ip']) else "Unknown"
        print(f"{device['ip']}\t\t{device['mac']}\t\t{device_type}")

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"  # Nastavte na váš rozsah IP adres
    devices = scan(ip_range)
    print_results(devices)
