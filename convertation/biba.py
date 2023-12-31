from pymongo import MongoClient
from PIL import Image
import io

def save(collection):
    client = MongoClient()
    db = client['picture_mongo']
    images = db[collection]

    im = Image.open("i.jpg")

    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')

    image = {
        'data': image_bytes.getvalue()
    }

    image_id = images.insert_one(image).inserted_id