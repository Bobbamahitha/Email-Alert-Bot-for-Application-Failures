import time, random

# Some sample log messages
messages = [
    "INFO Application started successfully",
    "INFO User logged in",
    "INFO Health check passed",
    "ERROR Database connection failed",
    "FAILURE Payment gateway timed out",
    "CRITICAL Server crashed due to memory leak"
]

# Open log file in append mode
with open("application.log", "a") as f:
    while True:
        # Pick a random message
        log = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {random.choice(messages)}\n"
        # Write to log file
        f.write(log)
        f.flush()
        print("📝 Wrote log:", log.strip())
        # Wait 5 seconds before writing the next log
        time.sleep(5)
