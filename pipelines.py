# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql.connections

class TutorialPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "Admin@123",
            db = "practice"
        )
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS quotes_tb(
            title text,
            author text,
            tags text
        )""")
   
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.cursor.execute("""INSERT INTO quotes_tb VALUES(%s, %s, %s)""", (
            item["title"][0],
            item["author"][0],
            item["tags"][0]
        ))
        self.conn.commit()