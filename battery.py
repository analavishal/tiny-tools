import wmi
import winsound
import ctypes

t = wmi.WMI(moniker = "//./root/wmi")
b = t.ExecQuery('Select * from BatteryFullChargedCapacity')
total = b[0].FullChargedCapacity
b = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
charge = round((b[0].RemainingCapacity / total) * 100)
chargerConnected = b[0].PowerOnLine
while True:
    if charge <= 40 and not chargerConnected:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        ctypes.windll.user32.MessageBoxW(0, "Connect charger", "Battery Health", 1)
    elif charge >= 80 and chargerConnected:
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        ctypes.windll.user32.MessageBoxW(0, "Remove charger", "Battery Health", 1)
    b = t.ExecQuery('Select * from BatteryStatus where Voltage > 0')
    charge = round((b[0].RemainingCapacity / total) * 100)
    chargerConnected = b[0].PowerOnLine
