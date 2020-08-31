import mysql.connector
import os

user_name = os.environ.get('DB_USER')
user_pass = os.environ.get('DB_PASS')

db = mysql.connector.connect(
    host='127.0.0.1',
    user=user_name,
    passwd=user_pass,
    database='valorant_games')

mycursor = db.cursor()

# Creating a table to contain players
mycursor.execute('CREATE TABLE player_list (id SMALLINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))')

# Creating a table to show performance of each player
mycursor.execute('CREATE TABLE performance (player_id SMALLINT, K SMALLINT, D SMALLINT, A SMALLINT,'
                 'KDA REAL, combat_score INT, econ_rating SMALLINT, MVP BOOL,'
                 'FOREIGN KEY (player_id) REFERENCES player_list (id))')

# Creating a table of agents (characters in game)
mycursor.execute('CREATE TABLE Agents_Table (id SMALLINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))')

# To check created tables
mycursor.execute('SHOW TABLES')
for table in mycursor:
    print(table)

# Adding players to the player_list table
add_player = "INSERT INTO player_list (name) VALUES (%s)"
mycursor.execute(add_player, ('Austin',))
mycursor.execute(add_player, ('Will',))
mycursor.execute(add_player, ('Matt',))
mycursor.execute(add_player, ('Kevin',))
mycursor.execute(add_player, ('Justin',))
mycursor.execute(add_player, ('Taewoo',))

# Adding agents to the agent_table
add_agent = 'INSERT INTO agents_table (name) VALUES (%s)'
mycursor.execute(add_agent, ('Breach',))
mycursor.execute(add_agent, ('Brimstone',))
mycursor.execute(add_agent, ('Cypher',))
mycursor.execute(add_agent, ('Jett',))
mycursor.execute(add_agent, ('Killjoy',))
mycursor.execute(add_agent, ('Omen',))
mycursor.execute(add_agent, ('Phoenix',))
mycursor.execute(add_agent, ('Raze',))
mycursor.execute(add_agent, ('Reyna',))
mycursor.execute(add_agent, ('Sage',))
mycursor.execute(add_agent, ('Sova',))
mycursor.execute(add_agent, ('Viper',))
db.commit()

# track victories
mycursor.execute('ALTER TABLE performance '
                 'ADD COLUMN (WON Bool)')

# keep track of won rounds on attack side vs defense side
mycursor.execute('ALTER TABLE performance '
                 'ADD COLUMN (Attack SMALLINT)')
mycursor.execute('ALTER TABLE performance '
                 'ADD COLUMN (Defense SMALLINT)')

# connecting tables
mycursor.execute('ALTER TABLE performance '
                 'ADD COLUMN (agent_id smallint), '
                 'ADD CONSTRAINT id FOREIGN KEY (agent_id) '
                 'REFERENCES agents_table (id)')

add_performance = 'INSERT INTO performance (player_id, K, D, A, KDA, combat_score, ' \
                  'econ_rating, MVP, WON, Attack, Defense, agent_id)' \
                  'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'


# useful functions
def person_by_agents(player):
    """
    :player: a players to see stats of
    :return: average of all agents for the person
    """
    # to find stats of a particular person with all agents
    execution_code = ('SELECT player_list.name, AVG(K) AS AVG_KILL, AVG(D) AS AVG_DEATH, AVG(A) AS AVG_ASSIST, '
                      'ROUND(AVG(KDA), 2) AS AVG_KDA, AVG(combat_score) AS AVG_COMBAT, AVG(econ_rating) AS AVG_ECON, '
                      'SUM(WON) AS GAME_WON, agents_table.name AS Agent, '
                      'CONCAT(ROUND(SUM(WON)/COUNT(WON)*100, 1), "%") AS WIN_RATE '
                      'FROM performance '
                      'JOIN agents_table '
                      'ON agents_table.id = agent_id '
                      'JOIN player_list '
                      'ON player_list.id = player_id '
                      'WHERE player_list.name = %s '
                      'GROUP BY agents_table.name')
    mycursor.execute(execution_code, (player,))
    print(mycursor.column_names)
    for line in mycursor:
        print(line)
    return ''


def avg_all(players):
    """
    :players: a list of players to take average of
    :return: average of all stats for everyone in the list
    """
    # to know how many strings to replace
    format_string = ', '.join(['%s'] * len(players))
    execution_code = ('SELECT player_list.name, ROUND(AVG(K), 2) AS AVG_KILL,'
                      'ROUND(AVG(D), 2) AS AVG_DEATH, ROUND(AVG(A), 2) AS AVG_ASSIST, '
                      'ROUND(AVG(KDA), 2) AS AVG_KDA, ROUND(AVG(combat_score), 2) AS AVG_COMBAT_SCORE,'
                      'ROUND(AVG(econ_rating), 2) AS AVG_ECON_RATING, SUM(WON) AS GAMES_WON,'
                      'COUNT(WON) AS GAMES_PLAYED, SUM(MVP) AS MVP,'
                      'CONCAT(ROUND(SUM(WON)/COUNT(WON)*100, 1), "%") AS WIN_RATE '
                      'FROM performance '
                      'JOIN player_list '
                      'ON player_list.id = player_id '
                      'WHERE player_list.name in ({}) '
                      'GROUP BY player_list.name '
                      'ORDER BY AVG_KDA DESC').format(format_string)
    mycursor.execute(execution_code, tuple(players))
    print(mycursor.column_names)
    for line in mycursor:
        print(line)
    return ''


mycursor.execute('SELECT * FROM player_list;')

# creating a player list to iterate through
name_list = [name[1] for name in mycursor]
print(name_list)

print(avg_all(name_list))

for player in name_list:
    print(person_by_agents(player))


# ADDING STATS
# adding_game 1
mycursor.execute(add_performance, (6, 25, 20, 11, round(36 / 20.0, 2), 302, 77, True, False, 6, 6, 11))
mycursor.execute(add_performance, (4, 22, 24, 8, round(30 / 24.0, 2), 253, 62, False, False, 6, 6, 4))
mycursor.execute(add_performance, (3, 23, 17, 4, round(27 / 17.0, 2), 251, 67, False, False, 6, 6, 7))
mycursor.execute(add_performance, (2, 10, 19, 3, round(13 / 19.0, 2), 119, 30, False, False, 6, 6, 6))
mycursor.execute(add_performance, (1, 26, 18, 4, round(30 / 18.0, 2), 269, 67, False, False, 6, 6, 10))

# adding game 2
mycursor.execute(add_performance, (6, 17, 18, 4, round(21 / 18.0, 2), 215, 54, False, True, 6, 7, 7))
mycursor.execute(add_performance, (4, 23, 18, 9, round(32 / 18.0, 2), 298, 90, True, True, 6, 7, 4))
mycursor.execute(add_performance, (3, 15, 17, 7, round(22 / 17.0, 2), 220, 58, False, True, 6, 7, 2))
mycursor.execute(add_performance, (2, 16, 16, 6, round(22 / 16.0, 2), 199, 56, False, True, 6, 7, 10))

# adding game 3
mycursor.execute(add_performance, (6, 25, 20, 4, round(29 / 20.0, 2), 243, 59, False, False, 4, 9, 11))
mycursor.execute(add_performance, (5, 18, 21, 13, round(31 / 21.0, 2), 207, 42, False, False, 4, 9, 6))
mycursor.execute(add_performance, (4, 23, 20, 2, round(25 / 20.0, 2), 247, 76, True, False, 4, 9, 4))
mycursor.execute(add_performance, (3, 16, 22, 8, round(24 / 22.0, 2), 182, 42, False, False, 4, 9, 7))

# adding game 4
mycursor.execute(add_performance, (6, 25, 13, 7, round(32 / 13.0, 2), 302, 79, True, True, 4, 9, 6))
mycursor.execute(add_performance, (4, 23, 17, 6, round(28 / 17.0, 2), 264, 46, False, True, 4, 9, 8))
mycursor.execute(add_performance, (3, 15, 12, 3, round(18 / 12.0, 2), 186, 51, False, True, 4, 9, 2))
mycursor.execute(add_performance, (2, 15, 16, 4, round(19 / 14.0, 2), 202, 48, False, True, 4, 9, 5))
mycursor.execute(add_performance, (1, 14, 15, 3, round(17 / 15.0, 2), 193, 40, False, True, 4, 9, 10))

# adding game 5
mycursor.execute(add_performance, (6, 7, 17, 5, round(12 / 17.0, 2), 137, 35, False, False, 4, 1, 3))
mycursor.execute(add_performance, (4, 8, 17, 8, round(16 / 17.0, 2), 135, 42, False, False, 4, 1, 4))
mycursor.execute(add_performance, (3, 12, 16, 2, round(14 / 16.0, 2), 195, 52, False, False, 4, 1, 2))
mycursor.execute(add_performance, (2, 12, 15, 9, round(21 / 15.0, 2), 199, 53, True, False, 4, 1, 9))

# adding game 6
mycursor.execute(add_performance, (6, 27, 13, 4, round(31 / 13.0, 2), 354, 84, True, True, 6, 7, 7))
mycursor.execute(add_performance, (4, 18, 14, 0, round(18 / 14.0, 2), 237, 45, False, True, 6, 7, 4))
mycursor.execute(add_performance, (3, 7, 14, 4, round(11 / 14.0, 2), 112, 35, False, True, 6, 7, 2))
mycursor.execute(add_performance, (2, 8, 18, 9, round(17 / 18.0, 2), 130, 28, False, True, 6, 7, 3))

# adding game 7
mycursor.execute(add_performance, (6, 21, 7, 1, round(22 / 7.0, 2), 297, 105, True, True, 6, 7, 6))
mycursor.execute(add_performance, (5, 13, 11, 3, round(16 / 11.0, 2), 163, 46, False, True, 6, 7, 10))
mycursor.execute(add_performance, (3, 12, 9, 0, round(12 / 9.0, 2), 159, 44, False, True, 6, 7, 2))
mycursor.execute(add_performance, (2, 14, 15, 3, round(17 / 15.0, 2), 212, 50, False, True, 6, 7, 6))
mycursor.execute(add_performance, (1, 15, 10, 2, round(17 / 10.0, 2), 211, 72, False, True, 6, 7, 11))

# adding game 8
mycursor.execute(add_performance, (6, 25, 6, 9, round(34 / 6.0, 2), 499, 177, True, True, 12, 1, 3))
mycursor.execute(add_performance, (5, 13, 8, 5, round(18 / 8.0, 2), 236, 63, False, True, 12, 1, 10))
mycursor.execute(add_performance, (1, 9, 8, 5, round(14 / 8.0, 2), 182, 59, False, True, 12, 1, 8))

# adding game 9
mycursor.execute(add_performance, (6, 17, 18, 4, round(21 / 18.0, 2), 285, 61, True, False, 2, 4, 2))
mycursor.execute(add_performance, (4, 11, 16, 1, round(12 / 16.0, 2), 136, 52, False, False, 2, 4, 4))
mycursor.execute(add_performance, (3, 14, 17, 2, round(16 / 17.0, 2), 236, 52, False, False, 2, 4, 7))
mycursor.execute(add_performance, (2, 9, 16, 8, round(17 / 16.0, 2), 158, 41, False, False, 2, 4, 5))

# adding game 10
mycursor.execute(add_performance, (6, 13, 15, 3, round(16 / 15.0, 2), 190, 73, True, False, 2, 5, 11))
mycursor.execute(add_performance, (5, 11, 17, 5, round(16 / 17.0, 2), 184, 62, False, False, 2, 5, 3))
mycursor.execute(add_performance, (4, 13, 13, 2, round(15 / 13.0, 2), 184, 46, False, False, 2, 5, 4))
mycursor.execute(add_performance, (3, 8, 18, 2, round(10 / 18.0, 2), 175, 41, False, False, 2, 5, 2))
mycursor.execute(add_performance, (2, 6, 16, 3, round(9 / 16.0, 2), 122, 40, False, False, 2, 5, 5))

# adding game 11
mycursor.execute(add_performance, (6, 20, 15, 4, round(24 / 15.0, 2), 258, 72, True, False, 6, 3, 3))
mycursor.execute(add_performance, (5, 11, 18, 10, round(21 / 18.0, 2), 156, 41, False, False, 6, 3, 10))
mycursor.execute(add_performance, (4, 12, 15, 3, round(15 / 15.0, 2), 166, 52, False, False, 6, 3, 6))
mycursor.execute(add_performance, (3, 9, 15, 5, round(14 / 15.0, 2), 157, 48, False, False, 6, 3, 7))
mycursor.execute(add_performance, (2, 13, 21, 7, round(20 / 21.0, 2), 201, 49, False, False, 6, 3, 9))

# adding game 12
mycursor.execute(add_performance, (6, 22, 16, 6, round(28 / 16.0, 2), 281, 61, True, True, 7, 6, 6))
mycursor.execute(add_performance, (5, 10, 18, 7, round(17 / 18.0, 2), 171, 38, False, True, 7, 6, 9))
mycursor.execute(add_performance, (4, 21, 14, 4, round(25 / 14.0, 2), 273, 59, False, True, 7, 6, 10))
mycursor.execute(add_performance, (3, 18, 15, 7, round(25 / 15.0, 2), 247, 75, False, True, 7, 6, 7))
mycursor.execute(add_performance, (2, 6, 17, 4, round(10 / 17.0, 2), 83, 26, False, True, 7, 6, 5))

# adding game 13
mycursor.execute(add_performance, (6, 24, 16, 6, round(30 / 16.0, 2), 285, 81, True, True, 5, 8, 11))
mycursor.execute(add_performance, (5, 19, 17, 4, round(23 / 17.0, 2), 242, 52, False, True, 5, 8, 10))
mycursor.execute(add_performance, (4, 21, 16, 6, round(27 / 16.0, 2), 251, 71, False, True, 5, 8, 4))
mycursor.execute(add_performance, (3, 14, 20, 8, round(22 / 20.0, 2), 200, 49, False, True, 5, 8, 5))
mycursor.execute(add_performance, (2, 9, 16, 6, round(15 / 16.0, 2), 135, 43, False, True, 5, 8, 2))

# adding game 14
mycursor.execute(add_performance, (6, 16, 14, 1, round(17 / 14.0, 2), 260, 62, True, False, 3, 1, 2))
mycursor.execute(add_performance, (5, 11, 15, 1, round(12 / 15.0, 2), 190, 47, False, False, 3, 1, 3))
mycursor.execute(add_performance, (4, 5, 16, 1, round(6 / 16.0, 2), 113, 35, False, False, 3, 1, 10))
mycursor.execute(add_performance, (2, 9, 17, 2, round(11 / 17.0, 2), 175, 49, False, False, 3, 1, 5))
mycursor.execute(add_performance, (1, 8, 14, 2, round(10 / 14.0, 2), 159, 44, False, False, 3, 1, 9))

# adding game 15
mycursor.execute(add_performance, (6, 26, 9, 8, round(34 / 9.0, 2), 340, 139, True, True, 10, 3, 6))
mycursor.execute(add_performance, (5, 22, 11, 2, round(23 / 11.0, 2), 334, 69, False, True, 10, 3, 10))
mycursor.execute(add_performance, (4, 17, 11, 2, round(19 / 11.0, 2), 232, 52, False, True, 10, 3, 4))
mycursor.execute(add_performance, (2, 8, 14, 5, round(13 / 14.0, 2), 147, 42, False, True, 10, 3, 9))
mycursor.execute(add_performance, (1, 8, 14, 8, round(16 / 14.0, 2), 149, 40, False, True, 10, 3, 8))

# adding game 16
mycursor.execute(add_performance, (6, 14, 17, 4, round(18 / 17.0, 2), 148, 52, False, False, 3, 3, 6))
mycursor.execute(add_performance, (5, 7, 16, 4, round(11 / 16.0, 2), 129, 30, False, False, 3, 3, 3))
mycursor.execute(add_performance, (2, 10, 17, 4, round(14 / 17.0, 2), 164, 41, False, False, 3, 3, 4))

# adding game 17
mycursor.execute(add_performance, (6, 27, 18, 5, round(32 / 18.0, 2), 362, 80, True, False, 3, 6, 11))
mycursor.execute(add_performance, (5, 17, 15, 4, round(21 / 15.0, 2), 214, 49, False, False, 3, 6, 10))
mycursor.execute(add_performance, (2, 12, 15, 1, round(13 / 15.0, 2), 161, 48, False, False, 3, 6, 5))

# adding game 18
mycursor.execute(add_performance, (6, 18, 15, 8, round(26 / 15.0, 2), 269, 61, True, False, 4, 3, 7))
mycursor.execute(add_performance, (5, 9, 16, 1, round(10 / 16.0, 2), 126, 33, False, False, 4, 3, 3))
mycursor.execute(add_performance, (4, 11, 17, 6, round(17 / 17.0, 2), 149, 34, False, False, 4, 3, 4))
mycursor.execute(add_performance, (2, 12, 18, 2, round(14 / 18.0, 2), 170, 39, False, False, 4, 3, 6))
mycursor.execute(add_performance, (1, 14, 13, 6, round(20 / 13.0, 2), 180, 45, False, False, 4, 3, 11))

# adding game 19
mycursor.execute(add_performance, (6, 26, 16, 7, round(33 / 16.0, 2), 311, 79, True, True, 4, 9, 2))
mycursor.execute(add_performance, (5, 10, 19, 6, round(16 / 19.0, 2), 149, 40, False, True, 4, 9, 8))
mycursor.execute(add_performance, (4, 20, 18, 5, round(25 / 18.0, 2), 240, 56, False, True, 4, 9, 6))
mycursor.execute(add_performance, (2, 16, 17, 4, round(20 / 17.0, 2), 187, 57, False, True, 4, 9, 9))
mycursor.execute(add_performance, (1, 22, 16, 6, round(28 / 16.0, 2), 265, 72, False, True, 4, 9, 10))

# adding game 20
mycursor.execute(add_performance, (6, 21, 14, 3, round(24 / 14.0, 2), 236, 62, False, True, 6, 7, 10))
mycursor.execute(add_performance, (5, 16, 21, 5, round(21 / 21.0, 2), 218, 49, False, True, 6, 7, 7))
mycursor.execute(add_performance, (4, 12, 17, 4, round(16 / 17.0, 2), 173, 35, False, True, 6, 7, 4))
mycursor.execute(add_performance, (2, 15, 17, 0, round(15 / 17.0, 2), 161, 38, False, True, 6, 7, 6))
mycursor.execute(add_performance, (1, 22, 15, 5, round(27 / 15.0, 2), 282, 75, True, True, 6, 7, 11))

db.commit()