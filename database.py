from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_schema import Base


class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///database.db')
        Base.metadata.bind = self.engine
        dbs = sessionmaker(bind=self.engine)
        self._session = dbs()

    @staticmethod
    def get_table_comments():
        return [table.comment for table in Base.metadata.sorted_tables]

    @staticmethod
    def get_table_column_names(table_id):
        table = Base.metadata.sorted_tables[table_id]
        return [column.comment for column in table.columns]

    def get_table_rows(self, table_id):
        table = Base.metadata.sorted_tables[table_id]
        return [i for i in self._session.execute(f'SELECT * FROM {table}')]

    def remove_row_in_table(self, table_id, row_id: str):
        table = Base.metadata.sorted_tables[table_id]
        if row_id.isdigit():
            if self._session.execute(f'SELECT * FROM {table} WHERE {table}_id={row_id}'):
                self._session.execute(f'DELETE FROM {table} WHERE {table}_id={row_id}')
                self._session.commit()

    def update_data(self, table_id, items):
        table = Base.metadata.sorted_tables[table_id]
        for item in items:
            item = tuple([int(item[0])] + item[1:])
            self._session.execute(f'''INSERT OR IGNORE INTO {table} VALUES {item}''')
        self._session.commit()


if __name__ == '__main__':
    a = Database()
    print(a.get_table_rows(0))
