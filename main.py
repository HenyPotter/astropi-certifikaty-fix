import fitz 
import os

text = "AstroPi Hackathon Frýdek-Místek"

def rgb255_to_float(r, g, b):
    return (r / 255, g / 255, b / 255)

barva_rgb = rgb255_to_float(241, 241, 241)

input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".pdf"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        doc = fitz.open(input_path)
        page = doc[0]

        rect = fitz.Rect(320, 360, 800, 381)

        page.draw_rect(
            rect,
            color=barva_rgb,
            fill=barva_rgb,
            fill_opacity=1
        )

        page.insert_text(
            (322, 376),
            text,
            fontsize=17,
            fontname="helv",
            color=(0, 0, 0)
        )

        doc.save(output_path)
        doc.close()

        print(f"Opraveno: {output_path}")

print("✅ Všechna PDF byla zpracována.")
