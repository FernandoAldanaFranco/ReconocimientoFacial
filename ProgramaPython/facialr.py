#####################################
from deepface import DeepFace

obj = DeepFace.analyze(img_path = "hugo1.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print (obj)

#####################################

