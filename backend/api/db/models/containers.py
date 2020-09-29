from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON, Text, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

from datetime import datetime


class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True)

    # alternative: DateTime(timezone=True), sqlalchemy.sql.func.now()
    created_at = Column(DateTime,
                        nullable=False, unique=False, index=False,
                        default=datetime.utcnow)
    updated_at = Column(DateTime,
                        nullable=False, unique=False, index=False,
                        default=datetime.utcnow, onupdate=datetime.utcnow)

    # rename to title
    title = Column(String(255),
                   nullable=False, unique=True, index=True)
    url = Column(Text,
                 nullable=False, unique=True, index=False)

    items = relationship('TemplateItem',
                         backref='template', cascade='all, delete-orphan')


class TemplateItem(Base):
    __tablename__ = 'template_item'
    id = Column(Integer, primary_key=True)

    type = Column(Integer,
                  nullable=False, unique=False, index=False)
    title = Column(String(255),
                   nullable=False, unique=False, index=True)
    platform = Column(String(64),
                      nullable=False, unique=False, index=False)
    description = Column(Text,
                         nullable=True, unique=False, index=False)
    name = Column(String(255),
                  nullable=True, unique=False, index=True)
    logo = Column(Text,
                  nullable=True, unique=False, index=False)
    image = Column(String(128),
                   nullable=False, unique=False, index=False)
    notes = Column(Text,
                   nullable=True, unique=False, index=False)
    categories = Column(JSON,
                        nullable=True, unique=False, index=False)
    restart_policy = Column(String(20),
                            nullable=True, unique=False, index=False)
    ports = Column(JSON,
                   nullable=True, unique=False, index=False)
    volumes = Column(JSON,
                     nullable=True, unique=False, index=False)
    env = Column(JSON,
                 nullable=True, unique=False, index=False)
    devices = Column(JSON,
                    nullable=True, unique=False, index=False)
    labels = Column(JSON,
                    nullable=True, unique=False, index=False)
    sysctls = Column(JSON,
                     nullable=True, unique=False, index=False)
    cap_add = Column(JSON,
                     nullable=True, unique=False, index=False)
    template_id = Column(Integer,
                         ForeignKey('templates.id'))


class TemplateVariables(Base):
    __tablename__ = 'template_variables'
    id = Column(Integer, primary_key=True)
    variable = Column(String(255),
                      nullable=False, unique=True, index=True)
    replacement = Column(String(255),
<<<<<<< HEAD
        nullable=False, unique=True, index=True)

class Compose(Base):
    __tablename__ = 'compose_templates'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True, unique=True)
    description = Column(String(256), nullable=True)
    url = Column(String(256), nullable=True)
    path = Column(String(256), unique=True)
=======
                         nullable=False, unique=True, index=True)
>>>>>>> ff5cde45e70a3c82a1e2f714da6e769b5bee580a
