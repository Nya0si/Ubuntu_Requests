import requests
import os
import hashlib
from urllib.parse import urlparse

def fetch_image(url, download_dir="Fetched_Images", seen_hashes=set()):
    """
    Fetches an image from a given URL and saves it to the specified directory.
    Prevents duplicates and checks HTTP headers before saving.
    """

    try:
        # Create directory if it doesn't exist
        os.makedirs(download_dir, exist_ok=True)

        # Fetch the image with timeout
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check content type header before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipping {url} — not an image (Content-Type: {content_type})")
            return None

        # Extract filename from URL or fallback
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(download_dir, filename)

        # Compute hash to avoid duplicates
        file_hash = hashlib.md5(response.content).hexdigest()
        if file_hash in seen_hashes:
            print(f"✗ Skipping {filename} — duplicate detected")
            return None
        seen_hashes.add(file_hash)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")
    return None


def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A mindful tool for collecting and sharing images\n")

    # Ask if user wants single or multiple URLs
    choice = input("Do you want to fetch one image or multiple (one/many)? ").strip().lower()

    seen_hashes = set()  # Track duplicate images

    if choice == "many":
        urls = input("Enter image URLs separated by spaces:\n").split()
        for url in urls:
            fetch_image(url, seen_hashes=seen_hashes)
    else:
        url = input("Please enter the image URL: ")
        fetch_image(url, seen_hashes=seen_hashes)

    print("\n🌿 Connection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
