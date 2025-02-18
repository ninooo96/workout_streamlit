import pandas as pd
from PIL import Image, ImageSequence

def get_scheda(path):
    return pd.read_csv(path, delimiter = ';')


def resize_gif(input_path, output_path, new_size):
    with Image.open(input_path) as img:
        frames = []
        
        # Ridimensiona ogni frame
        for frame in ImageSequence.Iterator(img):
            frame = frame.resize(new_size, Image.LANCZOS)
            frames.append(frame)

        # Salva mantenendo l'animazione
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:], 
            loop=img.info.get("loop", 0), 
            duration=img.info.get("duration", 100),
            disposal=2  # Evita artefatti nei frame
        )


