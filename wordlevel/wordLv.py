#必要ライブラリのインポート
import openpyxl 
# openpyxlを使ってエクセルファイルを開く
workbook = openpyxl.load_workbook("j8_2016.xlsx")
# シートを取得,シート名はSheet1
ws = workbook["Sheet1"]
# target_valueが一致するセルの座標を検索
# 8000行2列の中に探したい文字列があるとして設定
word=input("英単語を入力してください")
for r in ws.iter_rows(max_row=8000, max_col=2):
# 列を一つずつ探索
    for c in r:
    # もしc.valueがtarget_valueと一致したらその行番号を返す
        if c.value == word:
             #セル番地を指定する:M10
            cell_nloc=c.coordinate
             #行数のみcell_nloc[1]を取得に格納
            cell_row_n=openpyxl.utils.cell.coordinate_from_string(cell_nloc)[1]
             #列数のみをcell_nloc[0]取得し、アルファベットから数字にする
            cell_col_m=openpyxl.utils.column_index_from_string(cell_nloc[0])
ans=int(cell_row_n)
ans=ans-1
anser=str(ans)

print("頻度順位："+ anser)
if ans >= 1 and ans<=1000:
    print("Lv1の単語")
elif ans >=1001 and ans<= 2000:
    print("Lv2の単語")

elif ans >=2001 and ans<= 3000:
    print("Lv3の単語")
elif ans >=3001 and ans<= 4000:
    print("Lv4の単語")  
elif ans >=4001 and ans<= 5000:
    print("Lv5の単語")
elif ans >=5001 and ans<= 6000:
    print("Lv6の単語")
elif ans >=6001 and ans<= 7000:
    print("Lv7の単語")
elif ans >=7001 and ans<= 8000:
    print("Lv8の単語")  
else :
    print("辞書に記載のない単語")
    

#print("セル番地："+ cell_nloc)


#print("セル列番号："+ str(cell_col_m))
