### pickle ###
# pickle : 프로그램에서 사용하고 있는 데이터를 파일 형태로 저장

import pickle
# profile_file = open("profile.pickle", "wb")     # pickle에서는 encoding 설정 필요 없음
# profile = {"이름": "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)

# pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 저장

# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()