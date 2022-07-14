#!/bin/bash
# cat yakei_kobe.csv | grep 六甲

# cat yakei_kobe.csv | cut -d , -f 1,2 # -dオプションで区切り文字を、-fオプションで列の番号(複数指定可能)を指定する。

#cat yakei_kobe.csv | sed 's/,/ /g' #カンマを半角スペースを置き換える。末尾のgは1行に検索する正規表現が複数回出現する場合でも全て置き換えることを意味する。
# sedコマンド: 's/検索する正規表現/置換する文字列/オプション'

#cat gihyo.jp/dp/index.html | grep -E 'class="paging-number"'
#cat gihyo.jp/dp/index.html | grep -E 'class="paging-number".*-'

# ファイル全体から目的の行を抜き出し
    # - 方策1:sedコマンドを使って正規表現にマッチした箇所を抜き出す。
        # s/.*(抜き出したい箇所にマッチする正規表現).*/\1/というコマンドを引数に与え()内だけ抜き出す。
        # echo abcdefgh | sed -E 's/.*(d.).*/\1/'
    # - 方策2:sedコマンドを使って正規表現にマッチした箇所を取り除き、結果的に残った箇所を抜き出す。
        # echo '<li class="paging-number">1 - 30 / 2098</li>' | sed -E 's/<[^>]*>//g'
    # - 方策3:cutコマンドを使って特定の文字で区切られた文字列からn番目を抜き出す。
        # csvファイルやUnixのpasswdファイルのように、特定の文字で区切られた文字列から一部の列を抜き出す際に役立つ。
        # cutコマンドは-dオプションで区切り文字を-fオプションで抜き出す列の番号を指定する
        # echo '1,高浜岸壁,神戸市中央区東川崎町1' | cut -d , -f 2
    # - 方策4:awkコマンドを使ってスペースで桁揃えされた文字列からn番目を抜き出す。
        # cutコマンドは区切り文字に1文字しか指定できない。このため、スペースで桁揃えされた文字列のように、区切り文字れが連続するようなケースは
        # 向かない。このような場合はスペースで区切られている場合に限定されるが、awkコマンドが使える
        # awkコマンドの引数に{print $n}という文字列を与えるとn番目の文字列を抜き出す。
        # echo 'PID    COMAND       %CPU  TIME  #TH  #WQ #PORT    MEM' | awk '{print $4}'

# 方策1で書籍の総数を抜き出す
# cat gihyo.jp/dp/index.html | grep -E 'class="paging-number".*-' | sed -E 's@.*/ ([0-9]+).*@\1@'

# cat gihyo.jp/dp/index.html | grep 'itemprop="name"'
cat gihyo.jp/dp/index.html | grep 'itemprop="name"' | wc -l
