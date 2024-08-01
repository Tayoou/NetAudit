import pyshark

class Roam:
    def __init__(self, pwd: str, filter: str) -> None:
        self.pwd = str
        self.filter = filter
        self.capture = pyshark.FileCapture(str, display_filter=filter)

    def decryption_psk(self):
        pass
    
    def get_ip_id(self, packet):
        if 'IP' in packet:
            return int(packet.ip.id)
        else:
            return -1
            
    def packet_sort(self, mode: str):
        if 'ip.id' == mode:
            paclist = list(self.capture)
            paclist.sort(key=Roam.get_ip_id)
            return paclist
        else:
            print('wrong sort mode')

    def loss_location(self):
        pass