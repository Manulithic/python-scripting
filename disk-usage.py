import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True)

for line in result.stdout.split("\n"):
  parts = line.split()
  if len(parts) > 5 and parts[-6] == "/dev/root":
    usage = int(parts[-2].replace("%", ""))
    if usage > 70:
      print ("High Disk Usage", usage, "%")
    else:
      print("Normal Disk Usage", usage, "%")
