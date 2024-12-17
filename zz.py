import os

#(그래) (상식) 같이 ( 지우기 )
def main():
    # txt 폴더의 파일들을 리스트로
    txtList = os.listdir('./txt')

    # txt 파일들 for 문 돌리기
    for txt_file in txtList:
        # 파일 열기
        with open("./txt/"+txt_file, "r", encoding="utf-8") as f:
            # 기존 내용 읽기
            lines = f.readlines()

        # 수정된 텍스트 쓰기
        with open("./srt/"+txt_file, "w", encoding="utf-8") as f:
            # 줄마다 ()와 [] 내용 제거하면서 개행 유지
            for line in lines:
                # () 내용 제거
                while '(' in line and ')' in line:
                    start_index = line.find("(")
                    end_index = line.find(")")
                    line = line[:start_index] + line[end_index + 1:]
                # [] 내용 제거
                while '[' in line and ']' in line:
                    start_index = line.find("[")
                    end_index = line.find("]")
                    line = line[:start_index] + line[end_index + 1:]
                # 줄이 비어있지 않으면 쓰기
                if line.strip():
                    f.write(line)

main()
