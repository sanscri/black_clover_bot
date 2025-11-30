import enum
from typing import List
from uuid import uuid4
from sqlalchemy import BigInteger, Column, Enum, Integer, Table, Text, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from .database import Base
from sqlalchemy.dialects.postgresql import UUID

# Модель для таблицы пользователей
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)

    avatar_id: Mapped[UUID] = mapped_column(ForeignKey("avatars.id"), nullable=True)
    avatar: Mapped["Avatar"] = relationship("Avatar", back_populates="user")


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Race(Base):
    __tablename__ = 'races'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

    avatars: Mapped[list["Avatar"]] = relationship("Avatar",back_populates="race")


class Avatar(Base):
    __tablename__ = 'avatars'
     
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


    nick: Mapped[str] = mapped_column(String, nullable=False)
    race_id: Mapped[UUID] = mapped_column(ForeignKey("races.id"), nullable=False)
    race: Mapped["Race"] = relationship("Race",back_populates="avatars")

    country_id: Mapped[UUID] = mapped_column(ForeignKey("countries.id"), nullable=False)
    country: Mapped["Country"] = relationship("Country",back_populates="avatars")


    stats_id: Mapped[UUID] = mapped_column(ForeignKey("avatar_stats.id"), nullable=False)
    stats: Mapped["AvatarStats"] = relationship(back_populates="avatar")

    grimoire_id: Mapped[UUID] = mapped_column(ForeignKey("grimoire.id"), nullable=True)
    grimoire: Mapped["Grimoire"] = relationship(back_populates="avatar")


    inventory_id: Mapped[UUID] = mapped_column(ForeignKey("inventories.id"), nullable=False)
    inventory: Mapped["Inventory"] = relationship(back_populates="avatar")


    user: Mapped["User"] = relationship(back_populates="avatar")


class AvatarStats(Base):
    __tablename__ = 'avatar_stats'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    current_hp: Mapped[int] = mapped_column(BigInteger, nullable=False)
    max_hp: Mapped[int] = mapped_column(BigInteger, nullable=False)
    current_magic_power: Mapped[int] = mapped_column(BigInteger, nullable=False)
    max_magic_power: Mapped[int] = mapped_column(BigInteger, nullable=False)
    attack: Mapped[int] = mapped_column(BigInteger, nullable=False)
    defense:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    strength:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    agility:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    intelligence:  Mapped[int] = mapped_column(BigInteger, nullable=False)
    crit_chance:  Mapped[float] = mapped_column(Float, nullable=False)
    crit_damage:  Mapped[float] = mapped_column(Float, nullable=False)

    avatar: Mapped["Avatar"] = relationship(back_populates="stats")


class Inventory(Base):
    __tablename__ = 'inventories'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    avatar: Mapped["Avatar"] = relationship(back_populates="inventory")


class Devil(Base):
    __tablename__ = 'devils'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class Spirit(Base):
    __tablename__ = 'spirits'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)


class Grimoire(Base):
    __tablename__ = 'grimoire'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    magic_attribute_id: Mapped[UUID] = mapped_column(ForeignKey("magic_attributes.id"), nullable=False)
    magic_attribute: Mapped["MagicAttribute"] = relationship("MagicAttribute", back_populates="grimoire")

    avatar: Mapped["Avatar"] = relationship(back_populates="grimoire")


class MagicAttribute(Base):
    __tablename__ = 'magic_attributes'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)

    grimoire: Mapped[list["MagicAttribute"]] = relationship("Grimoire", back_populates="magic_attribute")


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

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
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

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)
    rarity: Mapped[RarityEnum] = mapped_column(PgEnum(RarityEnum, name='rarity', create_type=False), nullable=False, default=RarityEnum.GARBAGE)
    edible: Mapped[bool] = mapped_column(Boolean, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False)
    cookable: Mapped[bool] = mapped_column(Boolean, nullable=False)
    partOfCraft: Mapped[bool] = mapped_column(Boolean, nullable=False)
    craftable: Mapped[bool] = mapped_column(Boolean, nullable=False)


class Country(Base):
    __tablename__ = 'countries'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    description:  Mapped[str] = mapped_column(String, nullable=True)
    symbol: Mapped[str] = mapped_column(String, nullable=True)

    avatars: Mapped[list["Avatar"]] = relationship("Avatar", back_populates="country")


class Region(Base):
    __tablename__ = 'regions'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)

class City(Base):
    __tablename__ = 'cities'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=True)


'''

road = Table(
    "road",
    Base.metadata,
    Column("source_id", Integer, ForeignKey("locations.id"), primary_key=True),
    Column("target_id", Integer, ForeignKey("locations.id"), primary_key=True),
)


class Location(Base):
    __tablename__ = 'locations'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    duration: Mapped[str] = mapped_column(String, nullable=True)

    source: Mapped[List["Location"]] = relationship(
        "Location",
        secondary=road,
        primaryjoin=id == road.c.source_id,
        secondaryjoin=id == road.c.target_id,
        back_populates="source",
    )
    target: Mapped[List["Location"]] = relationship(
        "Location",
        secondary=road,
        primaryjoin=id == road.c.target_id,
        secondaryjoin=id == road.c.source_id,
        back_populates="target",
    )

'''

class ArmedForces(Base):
    __tablename__ = 'armed_forces'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesMember(Base):
    __tablename__ = 'armed_forces_member'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesPermission(Base):
    __tablename__ = 'armed_forces_permission'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesRank(Base):
    __tablename__ = 'armed_forces_rank'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesRequest(Base):
    __tablename__ = 'armed_forces_request'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesSquad(Base):
    __tablename__ = 'armed_forces_squad'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesSquadMember(Base):
    __tablename__ = 'armed_forces_squad_member'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class ArmedForcesSquadPositions(Base):
    __tablename__ = 'armed_forces_squad_position'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)


class Achievement(Base):
    __tablename__ = 'achievements'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

class House(Base):
    __tablename__ = 'house'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

class Furniture(Base):
    __tablename__ = 'furniture'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)