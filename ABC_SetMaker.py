import os
ABC_taskname = ["A", "B", "C", "D", "E", "F", "G", "Ex"]
# ファイル名のリストです
# A~Cまでの3完が目標の場合、この配列の"D"以降を消していただけるといいと思います


new_path = input("New folder name?>>>ABC")
# フォルダ名の入力です
# 249,251などABC~~~の数字の部分だけを入力してください

new_path = "ABC"+new_path

absolete_path = os.path.abspath(new_path)
# なんとなく絶対パスを表示したかったので絶対パスを取得

writetxt = "#N, Q = map(int, input().split())\n#a = list(map(int, input().split()))\n#S = input()\n#\n#x=[]\n#for i in range(n):\n#    x.append(int(input()))"
# よくあるデータの受け取り方をコメントとしてデフォルトで書き込むようにしています
# 不要な場合はコメントアウトしていただいたり、適宜書き換えていただければと思います

if not os.path.exists(new_path):  # フォルダが既に存在しないことを確認
    os.mkdir(new_path)
    print("\"" + absolete_path + "\" was created successfully")  # メッセージの英語は適当です

    for i in range(0, len(ABC_taskname)):
        f = open(absolete_path+"\\"+new_path+"-" +
                 ABC_taskname[i]+".py", "w", encoding="utf-8")
        f.write("#"+ABC_taskname[i]+"問題"+"\n"+"\n"+writetxt)
        f.close()
    print(os.listdir(absolete_path), "were created successfully!")


else:
    print("\"", os.path.abspath(new_path), "\" already exists")
    print(os.listdir(absolete_path))

# 色々しなきゃいけない例外処理がある気がするけど何もしてないです
# 一応既に同名フォルダが有る場合は上書きはしないようにしてあるのですが、ご利用はご自身の責任で...
