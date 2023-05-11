import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
from firebase_admin import storage
import cv2
import datetime


def create(animal):
    cred = credentials.Certificate('./ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred,{
    'storageBucket': 'wildial.appspot.com'
})
    bucket = storage.bucket()
    db = firestore.client()
    firebase1 = firebase.FirebaseApplication('https://wildial.firebaseio.com/', None)
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    blob = bucket.blob(today)
    blob.upload_from_filename('./savedimage.jpeg')
    name=blob.public_url
    print(name)
  
    db.collection('USER1').add(
      {
        'name': animal,
        'location': 'Maniyur',
        'deviceid':'device1',
        'imagepath':name,
        'time':today
        
      }
      
    )
    