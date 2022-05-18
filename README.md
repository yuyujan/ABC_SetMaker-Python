# ABC_SetMaker

ABC_SetMakerはAtCoder Beginner ContestにPythonを利用して参加している人に向けたものです。
実行するとターミナルの実行元のフォルダ内に以下のフォルダとファイルを生成します。

フォルダ：ABCxxx  (xxxは入力内容に依存)
ファイル：ABCxxx-A.py ABCxxx-B.py ABCxxx-C.py ABCxxx-D.py ABCxxx-E.py ABCxxx-F.py ABCxxx-G.py ABCxxx-Ex  (xxxは入力内容に依存)

コンテストに参加するたびにファイルを沢山作るのがめんどくさい‥‥
過去問をやっていきたいけどファイル名とか全部適当で管理できてない‥‥

そのような人を対象としています。


# Requirement

Python3が必要です。
Python2系列だと動かない気がします。

特にpip installするものはないです。

# Installation

作業フォルダに"ABC_SetMaker.py"を配置してください。

# Usage

作業フォルダの場所で"ABC_SetMaker.py"を実行します。
"New folder name?>>>ABC"という形で尋ねられるので、249のようにコンテストが第何回であるか入力してください。
それに応じたフォルダとファイルを生成します。

自分はVSCodeで作業フォルダを開き、その中にこの"ABC_SetMaker.py"を配置しています。
過去問を解く場合は"ABC_SetMaker.py"をVSCodeの実行とデバッグから走らせています。

# Note

初期設定だとA問題からEx問題に対応して計8つのファイルを生成します。
C問題までしかやりません！というかたは直接"ABC_SetMaker.py"を書き換え、配列ABC_tasknameからD以降を削除してください。

また、各ファイルにはよくある入力の受け取り方をコメントにして書き込むようにしてます。
コメントについても同様で、こんなもの不要だ！という方は変数writetxtをコメントアウトしたり書き換えたりしてください。

# Author

* 作成者：yuyujan
