log_file = "./logs/auth.log"

failed_attempts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split("from")[1].split()[0]
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("Suspicious IPs:")
for ip, count in failed_attempts.items():
    if count > 2:
        print(f"{ip} - {count} failed attempts")