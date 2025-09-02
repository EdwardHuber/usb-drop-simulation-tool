# USB Drop Simulation Tool

Detects and logs **USB insertion/removal** events for training and forensic simulations.  
Cross-platform: Linux (udev) and Windows (WMI).

## Linux
```bash
pip3 install -r requirements-linux.txt
sudo python3 usb_monitor_linux.py
## windows
pip install -r requirements-windows.txt
python usb_monitor_windows.py
