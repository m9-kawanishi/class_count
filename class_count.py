import os, sys
import numpy as np
import csv

# カウントしたいID
ID_count = int(sys.argv[2])

def main():
    # ファイルを一斉取得するディレクトリ指定
    path = str(sys.argv[1]+"/")    
    files = os.listdir(path)
    ID_err = []  # 誤認識したIDを格納する配列
    class_count = 0  # 正解カウント
    undetected_count = 0  # 未検出カウント
    for file in files:
        # 拡張子取得
        extension = os.path.splitext(file)[1]
        if extension == ".txt":
            #テキストファイルオープン
            with open(path+file, encoding="cp932") as f:
                contents = f.read().split( )
            # 数値に変換
            contents = [float(num) for num in contents]
            contents = np.array(contents).reshape(-1,5)
            for ID in contents[:,0]:
                if ID == ID_count:
                    class_count += 1  # 正解カウント
                    break  # 1個目のクラスで正解だったらループを抜ける
                else:
                    # 誤認識したクラスを取得
                    ID_err.append(ID)
                    break  # 単に誤認識クラスを確認したいときはここをコメントアウト
            # 未検出なら
            if len(contents[:,0]) == 0:
                print(f"未検出: {file}")
                undetected_count += 1

    # IDのカウント辞書
    count_dict = {}

    # ID走査
    for num in ID_err:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    print("\n誤認識カウント========================")
    for num, count in count_dict.items():
        print(f"{int(num)}: {count}個")
    if undetected_count:
        print(f"未検出: {undetected_count}")
    print("====================================")

    print(f"正解したカウントは {class_count}")
                

if __name__ == "__main__":
    main()