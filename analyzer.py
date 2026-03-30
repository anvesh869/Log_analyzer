# Step 1: Open and read the log file
with open("logs.txt", "r") as file:
    logs = file.readlines()

# Step 2: Print logs (just to test)
for log in logs:
    print(log.strip())
failed_attempts = []

for log in logs:
    if "Failed login" in log:
        failed_attempts.append(log)

print("Failed Login Attempts:")
for attempt in failed_attempts:
    print(attempt.strip())
    failed_ips = {}

for log in logs:
    if "Failed login" in log:
        parts = log.split(" ")
        ip = parts[-1].strip()
        
        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

print("Failed Login Count by IP:")
for ip, count in failed_ips.items():
    print(ip, "->", count)
    print("\nSuspicious Activity:")

for ip, count in failed_ips.items():
    if count > 3:
        print(f"ALERT: Possible brute-force attack from {ip} ({count} attempts)")
