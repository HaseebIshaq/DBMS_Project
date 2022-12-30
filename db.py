import oracledb


dsn="project_high"
username="admin"
password="b7_!uuDQYW#mF9Z"
wallet_dir="C:/Users/FIRE FLY LAPTOP'S/OneDrive - Higher Education Commission/Desktop/AI 201/wallet"
wallet_pass="b7_!uuDQYW#mF9Z"

# db= orm.Database()



con=oracledb.connect(
    user=username,
    password=password,
    dsn=dsn,
    config_dir=wallet_dir,
    wallet_location=wallet_dir,
    wallet_password=wallet_pass
    )

# db.bind(provider='oracle', user=username, password=password, dsn=dsn)

# x = 4
# data = db.select("select * from vehicles where v_id = $x")

# print(data)

cur = con.cursor()

# print("Establishing connection:")

# # insert into table
# # cur.execute("insert into vehicles values(5,'biek',2,8)")

# # retrieve from table
# # cur.execute("select * from vehicles")

i = ''
q = f'select count(c_id) into {i} from CUSTOMERS'
cur.execute(f'select count(c_id) into {i} from CUSTOMERS')

# #delete from table
n = input()
# q = f'delete from vehicles where V_ID =\'' + n +'\''
q = f'delete from vehicles where V_ID ={n}'



# # cur.execute(q)

# # con.commit()

# db_version = cur.fetchall()
# print(db_version)

# # print(i)



# cur.close()