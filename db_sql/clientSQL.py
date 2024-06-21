import asyncio
import asyncpg

class Cleint:

    def __init__(self, user:str, password:str, 
                 host: str = '127.0.0.1',
                 port: int = 27017,
                 db_name: str = 'database'):
        
        conn = await asyncpg.connect(user=user, password=password,
                                 database=db_name, host=host)
        values = await conn.fetch(
            'SELECT * FROM mytable WHERE id = $1',
            10,
        )
        await conn.close()