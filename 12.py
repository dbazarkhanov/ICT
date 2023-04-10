import numpy as np
import sklearn.linear_model as skmod
import sklearn.preprocessing as skprepro

l_sport= ["Base Jump", "Tea with friends", "Video games"]
favorite_sport = ["Base Jump", "Tea with friends", "Base Jump", "Tea with friends", "Tea with friends", "Base Jump", "Base Jump", "Tea with friends", "Video games", "Base Jump", "Base Jump", "Video games", "Tea with friends", "Video games", "Tea with friends", "Video games", "Video games", "Video games"]
age = [32, 48, 28, 83, 87, 28, 25, 81, 20, 30, 25, 12, 80, 23, 87, 12, 24, 19]

# Create an ecnoder LabelEncoder() and use fit_transform() function
encoder = skprepro.LabelEncoder()
# encoder= encoder.fit(favorite_sport)
encoder= encoder.fit(l_sport)
fav_code = encoder.transform(favorite_sport)
print(fav_code)

#label encoder : the inverse_transform method and the class_ attributes.
print(encoder.inverse_transform(np.array([2])))

