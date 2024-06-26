from sqlmodel import SQLModel, create_engine 
#import .models
db_type = 'postgresql'
db_name = 'standb' 
db_user = 'stanuser'
db_port = '6432'
db_ip = '192.168.1.66' 
user_pass = 'pgpwd4stan'
echo = True

postgresql_url = f'{db_type}://{db_user}:{user_pass}@{db_ip}:{db_port}/{db_name}'

engine = create_engine(postgresql_url, echo=echo)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def drop_table():
    SQLModel.metadata.drop_all(engine)

if __name__ == '__main__':
    drop_table()
    create_db_and_tables()
