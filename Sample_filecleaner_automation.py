
import os        # python comes with these two already but please import or none of the code will work
import shutil

SOURCE = r"C:\Users\HP\Documents\Splice"  # should be changed to match your directory

TARGET_FOLDERS = [           # you can add file names and this code will look for anything containing that name
    "piano",
    "guitar",
    "percussion",
    "snare",
]

TARGET_MAP = {name.lower(): name for name in TARGET_FOLDERS}

for root, dirs, files in os.walk(SOURCE):
    if os.path.abspath(root) == os.path.abspath(SOURCE):
        pass
    elif os.path.basename(root).lower() in TARGET_MAP:
        continue

    for file in files:
        if not file.lower().endswith(".wav"):
            continue

        src = os.path.join(root, file)
        name_stem = os.path.splitext(file)[0].lower()

        for key, folder_name in TARGET_MAP.items():
            if key in name_stem:
                target_folder = os.path.join(SOURCE, folder_name)
                dst_file = os.path.join(target_folder, file)

                os.makedirs(target_folder, exist_ok=True)

                if os.path.exists(dst_file):
                    base, ext = os.path.splitext(file)
                    i = 2
                    while True:
                        candidate = os.path.join(
                            target_folder, f"{base} ({i}){ext}"
                        )
                        if not os.path.exists(candidate):
                            dst_file = candidate
                            break
                        i += 1

                shutil.move(src, dst_file)
                print(f"MOVED → {folder_name}: {file}")
                break



