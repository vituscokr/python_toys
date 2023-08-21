# isTesting = false 로 만들것 
# Setting 파일에서 isTesting 검사용으로 사용하기 위해서 만든 파이썬 파일 
setting_filepath = r"[파일경로]"
fin = open(setting_filepath, "rt", encoding="utf8");
find_is_test = False
for line in fin:
    strings = line.split("=")
    if strings[0].strip() == "static const bool isTest":
        find_is_test = True
        value = strings[1].strip().replace(";", "")
        if value == "false":
            print("릴리즈 버전입니다.")
        if value == "true":
            print("테스트 버전입니다.")

if find_is_test == False:
    print("설정파일을 확인하여 주십시오.")