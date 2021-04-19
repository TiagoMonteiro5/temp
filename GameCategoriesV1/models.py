from config import db, ma

class Game(db.Model):
    __tablename__ = 'game'
    game_id = db.Column(db.Integer, primary_key = True, nullable = False)
    game_name = db.Column(db.String(255), nullable = False)
    
    def serialize(self):
        return {
            'game_id':self.game_id,
            'game_name':self.game_name
        }

    def __repr__(self):
        return '<Game {}, {}>'.format(self.game_id, self.game_name)

"""    
class GameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        sqla_session = db.session    
"""