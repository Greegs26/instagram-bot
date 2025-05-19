import random
import requests

# Load saved post links
with open("saved_posts_test.txt", "r") as f:
    links = [line.strip() for line in f if line.strip()]

# Check that we have at least one
if not links:
    print("No links found in saved_posts_test.txt")
else:
    selected = random.choice(links)
    print(f"Sending to Discord: {selected}")

    # Replace this with your actual webhook URL
    WEBHOOK_URL = "https://discord.com/api/webhooks/1374055629798506507/yzjoraVqf0vC6Zijzt31vsAzMQU4WDSu4eJyD2E7bED7gm6XBLGMRDHuYBqv44dk8Gp4"

    data = {
        "content": f"🌟 Here's your random Instagram post: {selected}"
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("✅ Message sent to Discord!")
    else:
        print(f"❌ Failed to send message. Status code: {response.status_code}")