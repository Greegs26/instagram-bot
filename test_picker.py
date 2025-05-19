import random

# Load the file
with open("saved_posts_test.txt", "r") as f:
    links = [line.strip() for line in f if line.strip()]

# Check if there are any links
if not links:
    print("No links found in saved_posts_test.txt")
else:
    # Pick 1 random link
    selected = random.choice(links)
    print(f"Today's post: {selected}")