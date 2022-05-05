import vidaug.augmentors as va
import random

sometimes = lambda aug: va.Sometimes(0.5, aug) 
seq = va.Sequential([ 
    sometimes(va.RandomCrop(size=(224, 224))),
    sometimes(va.RandomRotate(degrees=10)),
   sometimes(va.VerticalFlip()),
    sometimes(va.HorizontalFlip()),
    sometimes(va.GaussianBlur(1.5))
])