from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
major = Table('major', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255)),
    Column('link', String(length=255)),
    Column('description', String(length=255)),
)

major_topics = Table('major_topics', post_meta,
    Column('topic_id', Integer),
    Column('major_id', Integer),
)

course = Table('course', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=255)),
    Column('link', String(length=255)),
    Column('upvotes', Integer),
    Column('downvotes', Integer),
    Column('provider_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['major'].create()
    post_meta.tables['major_topics'].create()
    post_meta.tables['course'].columns['provider_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['major'].drop()
    post_meta.tables['major_topics'].drop()
    post_meta.tables['course'].columns['provider_id'].drop()
