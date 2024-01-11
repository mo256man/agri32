import os
import datetime
import subprocess as sp
import sqlite3

os.chdir(os.path.dirname(os.path.abspath(__file__)))					# カレントディレクトリに移動
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")				# 現在時刻
dbname = "agri.db"

def read_config(key):
	# コンフィグを1項目取得する
	sql = f"SELECT value FROM config WHERE [index]='{key}';"
	conn = sqlite3.connect(dbname)
	cur = conn.cursor()
	cur.execute(sql)
	result = cur.fetchone()[0] 				# fetchoneは要素数=1のタプルを返すのでその要素を取り出す
	cur.close()
	conn.close()
	return result
        
def write_config(key, value):
	# コンフィグを1項目更新する
	conn = sqlite3.connect(dbname)
	cur = conn.cursor()
	sql = f"UPDATE config SET value='{value}' WHERE [index]='{key}';"
	cur.execute(sql)
	conn.commit()
	cur.close()
	conn.close()

def main():
	autorestart = read_config("autorestart")							# 現在の再起動設定を読み込む
	print(autorestart)
	if autorestart == "1":												# 再起動する設定ならば
		write_config("autorestart", "2")								# 設定のautorestartを2に変更した上で
		print(f"{now} リブート")											# リブートする
		cmd = "sudo reboot"												# linuxコマンド
		sp.Popen(cmd.split())											# 空白で区切ってリストにし、実行する
	else:
		pass
		print(f"{now} リブートしない")

if __name__ == "__main__":
	main()
