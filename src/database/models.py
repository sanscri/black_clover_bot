from sqlalchemy import BigInteger, Integer, Text, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


# Модель для таблицы пользователей
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)

class Race(Base):
    __tablename__ = 'races'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class Devil(Base):
    __tablename__ = 'devils'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class Spirit(Base):
    __tablename__ = 'spirits'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class Grimoire(Base):
    __tablename__ = 'grimoire'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)



class Spell(Base):
    __tablename__ = 'spell'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
