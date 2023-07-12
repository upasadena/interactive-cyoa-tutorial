# Python program to automatically compress gifs
# Will ignore gifs that already exist in raw_gifs folder

# Imports
import os

# Path to images
images_path = "./docs/images/"
# Path to store raw gifs
raw_gifs_path = images_path + "raw_gifs/"

# List of gif files
gifs = []

input("Are you sure you want to run this program? ")

# Find gifs in the folder
images_dir = os.scandir(images_path)
for entry in images_dir:
    if entry.is_file() and entry.name.endswith(".gif"):
        print(f"Gif found: {entry.name}")
        gifs.append(entry.name)

# Move gifs to the raw_data folder
# Then compresses them
print("Compressing gifs now!")
for i, gif in enumerate(gifs):
    # os.rename essentially moves files
    old_gif_path = images_path + gif
    new_gif_path = raw_gifs_path + gif

    print(f"Checking if {gif} exists in raw_gifs folder…")
    if os.path.isfile(new_gif_path):
        print("File exists! Skipping…")
        continue
    print("File doesn't exist!")

    print(f"Moving '{gif}' to raw_gifs folder")
    os.rename(old_gif_path, new_gif_path)

    # Gifsicle must be in path
    # Compresses the gif and sends it back
    print("Done!")
    print(f"({i+1}/{len(gifs)}) Compressing '{gif}'…")
    os.system(f"gifsicle -O3 --lossy=80 --colors=256 {new_gif_path} -o {old_gif_path}")

print("Completed succesfully!")