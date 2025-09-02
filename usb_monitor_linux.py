#!/usr/bin/env python3
"""
USB Drop Simulation (Linux)
Logs USB add/remove events to stdout and csv.

Usage:
  sudo python3 usb_monitor_linux.py
"""
import pyudev, csv, time, os

def main():
    ctx = pyudev.Context()
    mon = pyudev.Monitor.from_netlink(ctx)
    mon.filter_by('block')
    ts = time.strftime("%Y%m%d-%H%M%S")
    os.makedirs("logs", exist_ok=True)
    csvp = f"logs/usb_events_{ts}.csv"
    with open(csvp, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["timestamp","action","device","model","serial"])
        for dev in iter(mon.poll, None):
            if dev.get('ID_BUS') != 'usb':
                continue
            row = [time.strftime("%Y-%m-%d %H:%M:%S"),
                   dev.action,
                   dev.device_node or "",
                   dev.get('ID_MODEL') or "",
                   dev.get('ID_SERIAL_SHORT') or ""]
            print(row)
            w.writerow(row); f.flush()

if __name__ == "__main__":
    main()
