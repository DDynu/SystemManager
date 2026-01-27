import subprocess
from enums.status import Status

def check_online(ip_addr, count=3):
    cmd = ['ping', ip_addr, '-c', str(count)]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc.wait()
    
    try:
        o, e = proc.communicate(timeout=float(count))
        # print('Output: ' + o.decode('ascii'))
        # print('Error: '  + e.decode('ascii'))
        # print('code: ' + str(proc.returncode))
        if (int(proc.returncode) == 0):
            return Status.POWER_ON
        else:
            print("Cannot reach system")
            return Status.POWER_OFF

    except subprocess.TimeoutExpired as e:
        print("Timeout: ", e)
        return Status.POWER_OFF

# Testing
# if __name__ == '__main__':
#     print("HEY", os.getcwd())
#     print(check_online(sys.argv[1], int(sys.argv[2])))
