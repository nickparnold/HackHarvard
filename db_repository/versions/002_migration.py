from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
goals = Table('goals', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('monthly', Numeric),
    Column('max', Numeric),
    Column('user_id', String(length=24)),
)

nest_config = Table('nest_config', post_meta,
    Column('config_id', Integer, primary_key=True, nullable=False),
    Column('hvac_state', Boolean),
    Column('temp', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['goals'].create()
    post_meta.tables['nest_config'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['goals'].drop()
    post_meta.tables['nest_config'].drop()
