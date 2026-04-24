import sys
#sys is a built in python module that lets you interact with runtime environment
error_count = 0
failed_count = 0

log_file = sys.argv[1]

with open(log_file, "r") as file:
  for line in file:
    line = line.lower()
    if "error" in line:
      error_count += 1
    if "failed" in line:
      failed_count +=1
print("Error Count:", error_count)
print("Failed Count:", failed_count)
