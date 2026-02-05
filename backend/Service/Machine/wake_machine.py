from wakeonlan import send_magic_packet

from enums.status import Status

def wake_machine(mac_addr):
    send_magic_packet(mac_addr)
    print(f"Sent magic packet to {mac_addr}")
    return Status.POWERING_ON
    
