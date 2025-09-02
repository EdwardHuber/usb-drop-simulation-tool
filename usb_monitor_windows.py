#!/usr/bin/env python3
"""
USB Drop Simulation (Windows)
Uses WMI to watch for volume changes and logs to CSV.
Run in an elevated PowerShell/CMD if needed.
"""
import time, csv, os
import wmi  # pip install wmi

def main():
    c = wmi.WMI()
    ts = time.strftime("%Y%m%d-%H%M%S")
    os.makedirs("logs", exist_ok=True)
    csvp = f"logs\\usb_events_{ts}.csv"
    with open(csvp, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp","event","drive","description"])
        watcher = c.Win32_VolumeChangeEvent.watch_for()
        print("[*] Watching for USB volume events (Ctrl+C to stop)...")
        while True:
            e = watcher()
            row = [time.strftime("%Y-%m-%d %H:%M:%S"), e.EventType, getattr(e, 'DriveName', ''), getattr(e, 'Description', '')]
            print(row)
            w.writerow(row); f.flush()

if __name__ == "__main__":
    main()
