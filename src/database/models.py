import enum
from sqlalchemy import BigInteger, Enum, Integer, Text, ForeignKey, String, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from .database import Base


# Модель для таблицы пользователей
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)


class UserStats(Base):
    __tablename__ = 'stats'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    current_hp: Mapped[int] = mapped_column(BigInteger, nullable=False)
    max_hp: Mapped[int] = mapped_column(BigInteger, nullable=False)
    mana: Mapped[int] = mapped_column(BigInteger, nullable=False)
    mana_max: Mapped[int] = mapped_column(BigInteger, nullable=False)
    attack: Mapped[int] = mapped_column(BigInteger, nullable=False)
    defense:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    strength:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    agility:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    intelligence:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    crit_chance:  Mapped[float] = mapped_column(Float, nullable=False)
    crit_damage:  Mapped[float] = mapped_column(Float, nullable=False)

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


class MagicAttribute(Base):
    __tablename__ = 'magic_attributes'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class ENUM_SPELL_TYPE(str, enum.Enum):
    CREATION = 'CREATION'
    CURSE = 'CURSE'
    FORBIDDEN = 'FORBIDDEN'
    HEALING = 'HEALING'
    REINFORCEMENT = 'REINFORCEMENT'
    RESTRAINING = 'RESTRAINING'
    SEAL = 'SEAL'
    TRAP = 'TRAP'
    WEAKENING = 'WEAKENING'
    DEVIL_UNION = 'DEVIL_UNION'
    SPIRIT_UNION = 'SPIRIT_UNION'
    PASSIVE = 'PASSIVE'

class Spell(Base):
    __tablename__ = 'spells'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)

class RarityEnum(str, enum.Enum):
    GARBAGE = "GARBAGE"
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"
    UNIQUE = "UNIQUE"



class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[RarityEnum] = mapped_column(PgEnum(RarityEnum, name='rarity', create_type=False), nullable=False, default=RarityEnum.GARBAGE)



class Country(Base):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)


class Region(Base):
    __tablename__ = 'regions'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)

class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)


class Location(Base):
    __tablename__ = 'locations'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    roads: Mapped[list["Road"]] = relationship("Roads", back_populates="locations", cascade="all, delete-orphan")

class Road(Base):
    __tablename__ = 'roads'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    duration: Mapped[str] = mapped_column(String, nullable=True)

    source_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    source: Mapped["Location"] = relationship("Location", back_populates="roads")

    target_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    target: Mapped["Location"] = relationship("Location", back_populates="roads")


class ArmedForces(Base):
    __tablename__ = 'armed_forces'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesMember(Base):
    __tablename__ = 'armed_forces_member'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesPermission(Base):
    __tablename__ = 'armed_forces_permission'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesRank(Base):
    __tablename__ = 'armed_forces_rank'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesRequest(Base):
    __tablename__ = 'armed_forces_request'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesSquad(Base):
    __tablename__ = 'armed_forces_squad'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesSquadMember(Base):
    __tablename__ = 'armed_forces_squad_member'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class ArmedForcesSquadPositions(Base):
    __tablename__ = 'armed_forces_squad_position'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)


class Achievement(Base):
    __tablename__ = 'achievements'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
