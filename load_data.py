from scipy.io import loadmat
import pandas as pd

def get_meta(mat_path, db):
    meta = loadmat(mat_path)
    full_path = meta[db][0, 0]["full_path"][0]
    dob = meta[db][0, 0]["dob"][0]  # Matlab serial date number
    gender = meta[db][0, 0]["gender"][0]
    photo_taken = meta[db][0, 0]["photo_taken"][0]  # year
    face_score = meta[db][0, 0]["face_score"][0]
    second_face_score = meta[db][0, 0]["second_face_score"][0]
    # age = [calc_age(photo_taken[i], dob[i]) for i in range(len(dob))]
    data = {"file_name": full_path, "gender": gender, "score": face_score,
            "second_score": second_face_score}
    dataset = pd.DataFrame(data)
    return dataset

data = get_meta("wiki.mat", "wiki")
