# https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_quick_guide.htm

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///wopas.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    profile = Column(String)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

an_author = Authors(name = 'John Doe', profile='google.com')

session.add_all([
    Authors(name = 'Alan Kay', profile='apple.com'),
    Authors(name = 'Mark Zuckerberg', profile='facebook.com'),
    Authors(name = 'Linus Torvalds', profile="linux.com")
])
session.add(an_author)
session.commit()

result = session.query(Authors).all()

for row in result:
    print("id ", row.id, "name ", row.name, "profile ", row.profile)

x = session.query(Authors).get(2)
x.profile = 'myspace.com'
session.commit()

x = session.query(Authors).update({ Authors.profile: "Jack" }, synchronize_session = False)
session.commit()

# session.query(class).filter(criteria)
# session.query(Authors).filter(Authors.id>2)
# ==
# !=
# like
# in_([])
# and_()
# or_()
# all()
# first()
# one()
# scalar()

from sqlalchemy import text
for author in session.query(Authors).filter(text("id<3")):
    print(author.name)

author = session.query(Authors).filter(text("id = :value")).params(value = 1).one()
print(author.name)

author = session.query(Authors).from_statement(text("SELECT * FROM authors")).all()

# Below didn't work
# stmt = text("SELECT name, profile FROM authors")
# stmt = stmt.columns(Authors.id, Authors.name, Authors.profile)
# session.query(Authors.id, Authors.name, Authors.profile).from_statement(stmt).all()


