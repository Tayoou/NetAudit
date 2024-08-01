import pyshark
from wireless.RoamLoss import Roam

filepath = '/mnt/c/wsl/temp.pcap'
capture = pyshark.FileCapture(filepath, display_filter='udp', decryption_key='12345678:CUCC-5')
print(capture[0])
# capture = Roam(filepath, )
