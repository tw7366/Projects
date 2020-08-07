import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='tw7366',
    passwd='Tlsxodn1',
    database='valorant_games'
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE Valorant_Games")
# mycursor.execute("CREATE TABLE player_list (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))")
#mycursor.execute("CREATE TABLE performance (player_id int, game_num int, kda REAL, combat_score INT,"
#                 "econ_rating smallint, MVP bool, FOREIGN KEY (player_id) REFERENCES player_list (id))")

# mycursor.execute('SHOW TABLES')
# for table in mycursor:
#     print(table)
# add_player = "INSERT INTO player_list (name) VALUES (%s)"
# mycursor.execute(add_player, ('Austin',))
# mycursor.execute(add_player, ('Will',))
# mycursor.execute(add_player, ('Matt',))
# mycursor.execute(add_player, ('Kevin',))
# mycursor.execute(add_player, ('Justin',))
# mycursor.execute(add_player, ('Taewoo',))
# db.commit()


