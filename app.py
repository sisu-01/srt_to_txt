import pysrt
import os

def main():

    #path = input("경로를 입력하세요: ")

    #srt 폴더의 파일들을 리스트로
    srtList = os.listdir(f"./srt")

    #srt 파일들 for문 돌리기
    for srt in srtList:

        print(srt)
        #pysrt 파일로 가져오기
        subs = pysrt.open(f".//srt/{srt}")
        
        #파일 제목
        file_name = srt.rpartition('.')[0]

        #txt로 내용 옮기기
        f = open(f"./txt/{file_name}.txt", "w",encoding="utf-8")        
        temp = ""
        for sub in subs:
            temp += sub.text+"\n\n"
        temp = temp.replace("[주제곡]","")
        temp = temp.replace("자막 번역: 김지은","")
        temp = temp.replace("자막: 김지은","")
        temp = temp.replace("\"거창한 생각을\n표현하려면\"","")
        temp = temp.replace("\"거창한 단어를 써야 한다\"","")
        temp = temp.replace("\"달빛 아래 나무에서 자기\"","")
        temp = temp.replace("<i>","")
        temp = temp.replace("</i>","")
        temp = temp.replace("</i>","")

        temp = temp.replace("♪ First thing we`d climb a tree ♪","")
        temp = temp.replace("♪ And maybe then we`d talk ♪","")
        temp = temp.replace("♪ Or sit silently ♪","")
        temp = temp.replace("♪ And listen to our thoughts ♪","")
        temp = temp.replace("♪ With illusions of someday ♪","")
        temp = temp.replace("♪ Casting a golden light ♪","")
        temp = temp.replace("♪ No dress rehearsal ♪","")
        temp = temp.replace("♪ This is our life ♪","")
        temp = temp.replace("♪ You are ahead by a century ♪","")
        temp = temp.replace("-♪ This is our life ♪","")
        temp = temp.replace("-♪ You are ahead by a century ♪","")
        
        #temp = temp.replace("","")
        
        f.write(temp)
        f.close()

main()
