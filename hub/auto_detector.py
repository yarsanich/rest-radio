MICROBIT_VID = 3368
MICROBIT_PID = 516

from serial import Serial
import serial.tools.list_ports
from pathlib import Path


default_ports = ["/dev/ttyACM0", "/dev/ttyACM1", "/dev/ttyACM2", "/dev/ttyACM3"]


"""
We can autodetect the presence of a bridge micro:bit by resetting (sending a break) and waiting to see a SLIP_END character.
"""
def auto_detect_microbit():
    ports = list(serial.tools.list_ports.comports())

    micro_bits = []
    for p in ports:
        if isinstance(p, tuple):
            micro_bits += [p[0]]
        elif p.vid == MICROBIT_VID and p.pid == MICROBIT_PID:
            micro_bits += [p.device]

    selected = None

    for mb in micro_bits:
        try:
            s = Serial(port= mb,baudrate=115200, timeout=5)
        except:
            continue
        s.send_break()

        c = s.read(1)

        # check for slip end
        if c == chr(0xC0):
            selected = s

        if selected is not None:
            break

    # if we get here, all hope is lost, pick from a pre determined set of ports.
    if selected is None:
        for port in default_ports:
            io_port = Path(port)

            if io_port.exists():
                selected = port
                break

    return selected