from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.sql import text

class Raw():
    def __init__(self, db: sessionmaker) -> None:
        self.db = db

    def jsonify_results(self, collection: CursorResult) -> dict:
        results = [
            {
                "id": item.id,
                "name": item.name,
                "color": item.color
            } for item in collection]

        return {"results": results}
    
    def all(self):
        collection = self.db.execute(text("SELECT * FROM pop"))
        return self.jsonify_results(collection)

    def commit_refresh(self, args: dict, stm) -> dict:
        self.db.execute(statement=stm,params=args)
        self.db.commit()
        return self.all()

    def filter_by(self, pop_id: int):
        stm = text("SELECT * FROM pop WHERE id = :pop_id")
        collection = self.db.execute(statement=stm,params={"pop_id": int(pop_id)})
        return self.jsonify_results(collection)

    def delete_by(self, pop_id: int):
        stm = text("DELETE FROM pop WHERE id = :pop_id")
        return self.commit_refresh(args={"pop_id": int(pop_id)}, stm=stm)
    
    def insert_entry(self, pop_name: str, pop_color: str):
        args = {"pop_name": pop_name, "pop_color": pop_color}
        stm = text("INSERT INTO pop(name, color) VALUES(:pop_name, :pop_color)")
        return self.commit_refresh(args=args, stm=stm)

    def update_entry(self, pop_id: int, pop_name: str, pop_color: str):
        args = {"pop_id": pop_id, "pop_name": pop_name, "pop_color": pop_color}
        stm = text("UPDATE pop SET name=:pop_name, color=:pop_color WHERE id=:pop_id")
        return self.commit_refresh(args=args, stm=stm)
