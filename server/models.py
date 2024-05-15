from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
# wait what the heck is an association proxy?



metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class VideoGame(db.Model):

    __tablename__ = 'video_games_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    review = db.relationship("Review", back_populates='videogame')

    publications = association_proxy("review", "publication")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'publications': [pub.to_dict() for pub in self.publications]
        }

class Publication(db.Model):

    __tablename__ = 'publication_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    review = db.relationship("Review", back_populates='publication')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
    

class Review(db.Model):
    __tablename__ = 'review_table'

    id = db.Column(db.Integer, primary_key=True)

    rating = db.Column(db.Integer, default=0)

    videogame_id = db.Column(db.Integer, db.ForeignKey('video_games_table.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication_table.id'))

    publication = db.relationship('Publication', back_populates='review')
    videogame = db.relationship('VideoGame', back_populates='review')

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'videogame_id': self.videogame_id,
            'publication_id': self.publication_id,
            'publication': self.publication.to_dict(),
            'videogame': self.videogame.to_dict()
        }
    
    def __repr__(self):
        return f"Reviews(id={self.id}, rating={self.rating}, publication={self.publication.name})"