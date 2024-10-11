import subprocess
import shlex
import re

def check_ping_output(ping_output: str) -> str:
    if "Request timed out." in ping_output:
        return "đéo đúng"

    time_values = re.findall(r'time=(\d+)ms', ping_output)

    if time_values:
        max_time = max(map(int, time_values))
        return f"Thời gian truy cập lớn nhất: {max_time}ms"
    else:
        return "Không tìm thấy giá trị 'time' trong đầu ra của lệnh ping."


# def check_tracert(address: str) -> str:


s = "ping -c 4 8.8.8.8"
v = "Tracert 8.8.4.4"

command = shlex.split(s)
commandv = shlex.split(v)
result = subprocess.run(command, capture_output=True, text=True, shell=True)
djtmemay = subprocess.run(commandv, capture_output=True, text=True, shell=True)

print(result.stdout)
print(djtmemay.stdout)

output_result = check_ping_output(result.stdout)
print(output_result)