import os

OLD_TEXT = "https://whatsapp.com/channel/0029VbC7N9N7j6gDxkIlz80Y"   # जिसे बदलना है
NEW_TEXT = "https://whatsapp.com/channel/0029VbAvDSX0QeahEg4kkE3U"     # जिससे बदलना है

folder_path = os.getcwd()

for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if OLD_TEXT in content:
            content = content.replace(OLD_TEXT, NEW_TEXT)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"Updated: {filename}")

print("\n✅ Done! All HTML files updated successfully.")
