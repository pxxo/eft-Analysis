import mysql.connector

# MySQLサーバーへの接続情報
host = "185.27.134.10"
database = "if0_35016980_TarkovGuideApp"
user = "if0_35016980"
password = "d0ogC3IDOBP"

try:
    # MySQLサーバーに接続
    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )

    if connection.is_connected():
        print("MySQLに接続されました")

    # ここでSQLクエリを実行できます
    # SQLクエリを実行
    cursor = connection.cursor()
    cursor.execute("SELECT taskname FROM tasks")

    # 結果を取得
    result = cursor.fetchall()

except Exception as e:
    print(f"エラーが発生しました: {str(e)}")

finally:
    # 接続を閉じる
    if "connection" in locals() and connection.is_connected():
        connection.close()
        print("MySQL接続が閉じられました")
