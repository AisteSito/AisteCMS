import os
import json
import frontmatter

# Пути
FOLDERS = ["villa", "appart", "rent", "sold"]

def load_json(json_path):
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_json(data, json_path):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def md_to_dict(md_path):
    post = frontmatter.load(md_path)
    data = {
        "slug": post.get("slug", ""),
        "Name": post.get("Name", ""),
        "M2": post.get("M2", ""),
        "TotalFloors": post.get("TotalFloors", ""),
        "Bedroom": post.get("Bedroom", ""),
        "ZonaM2": post.get("ZonaM2", ""),
        "Bathroom": post.get("Bathroom", ""),
        "Price": post.get("Price", ""),
        "descrizione": post.get("descrizione", ""),
        "text1": post.get("text1", ""),
        "text3": post.get("text3", ""),
        "text4": post.get("text4", ""),
        "textFinal": post.get("textFinal", ""),
        "images": post.get("images", [])
    }
    return data

def update_json():
    for folder in FOLDERS:
        json_path = os.path.join(folder, f"{folder}.json")
        records = load_json(json_path)
        records_by_slug = {r["slug"]: r for r in records if r.get("slug")}

        for filename in os.listdir(folder):
            if filename.endswith(".md"):
                path = os.path.join(folder, filename)
                record = md_to_dict(path)

                if record["slug"]:
                    # Обновляем или добавляем
                    records_by_slug[record["slug"]] = record

        # Перезаписываем JSON
        save_json(list(records_by_slug.values()), json_path)

if __name__ == "__main__":
    update_json()
    print("✅ JSON файлы обновлены из md файлов")