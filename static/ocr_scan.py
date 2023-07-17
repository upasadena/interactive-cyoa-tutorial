import os
import glob

OUTPUT_FOLDER = "results"

image_files = [f for f in glob.glob("*.png")]   # Switch to .jpg or other types
                                                # according to your use case

os.system(f"mkdir {OUTPUT_FOLDER}")

print("Scanning files now…")

for i, image in enumerate(image_files):
    print(f"[Scanning image {i+1} of {len(image_files)}]")
    os.system(f"tesseract \"./{image}\" \"./{OUTPUT_FOLDER}/{image}\"")

print("Completed!")