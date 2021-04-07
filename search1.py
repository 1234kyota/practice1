
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv

with open('kimetsu.csv') as f:
    reader = csv.reader(f)
    for source in reader:
        print(source)
        

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        print("{}は見つかりません".format(word))
        source.append(word)
        with open('kimetsu.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(source)


    print(source)

if __name__ == "__main__":
    search()
