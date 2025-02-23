from dataclasses import dataclass
from abc import ABC

from typing import Callable, TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from ..Rac2Interface import Rac2Interface


@dataclass
class ItemData(ABC):
    item_id: int
    name: str


@dataclass
class EquipmentData(ItemData):
    offset: int


# Gadgets/Items
HELI_PACK = EquipmentData(1, "Heli-Pack", 2)
THRUSTER_PACK = EquipmentData(2, "Thruster-Pack", 3)
MAPPER = EquipmentData(3, "Mapper", 5)
ARMOR_MAGNETIZER = EquipmentData(4, "Armor Magnetizer", 7)
LEVITATOR = EquipmentData(5, "Levitator", 8)
SWINGSHOT = EquipmentData(6, "Swingshot", 13)
GRAVITY_BOOTS = EquipmentData(7, "Gravity Boots", 19)
GRIND_BOOTS = EquipmentData(8, "Grindboots", 20)
GLIDER = EquipmentData(9, "Glider", 21)
DYNAMO = EquipmentData(10, "Dynamo", 36)
ELECTROLYZER = EquipmentData(11, "Electrolyzer", 38)
THERMANATOR = EquipmentData(12, "Thermanator", 39)
TRACTOR_BEAM = EquipmentData(13, "Tractor Beam", 46)
QWARK_STATUETTE = EquipmentData(14, "Qwark Statuette", 49)
BOX_BREAKER = EquipmentData(15, "Box Breaker", 50)
INFILTRATOR = EquipmentData(16, "Infiltrator", 51)
CHARGE_BOOTS = EquipmentData(17, "Charge Boots", 54)
HYPNOMATIC = EquipmentData(18, "Hypnomatic", 55)


@dataclass
class WeaponData(EquipmentData):
    pass


# Weapons
CLANK_ZAPPER = WeaponData(101, "Clank Zapper", 0x09)
BOMB_GLOVE = WeaponData(102, "Bomb Glove", 0x0C)
VISIBOMB_GUN = WeaponData(103, "Visibomb Gun", 0x0E)
SHEEPINATOR = WeaponData(104, "Sheepinator", 0x10)
DECOY_GLOVE = WeaponData(105, "Decoy Glove", 0x11)
TESLA_CLAW = WeaponData(106, "Tesla Claw", 0x12)
CHOPPER = WeaponData(107, "Chopper", 0x16)
PULSE_RIFLE = WeaponData(108, "Pulse Rifle", 0x17)
SEEKER_GUN = WeaponData(109, "Seeker Gun", 0x18)
HOVERBOMB_GUN = WeaponData(110, "Hoverbomb Gun", 0x19)
BLITZ_GUN = WeaponData(111, "Blitz Gun", 0x1A)
MINIROCKET_TUBE = WeaponData(112, "Minirocket Tube", 0x1B)
PLASMA_COIL = WeaponData(113, "Plasma Coil", 0x1C)
LAVA_GUN = WeaponData(114, "Lava Gun", 0x1D)
LANCER = WeaponData(115, "Lancer", 0x1E)
SYNTHENOID = WeaponData(116, "Synthenoid", 0x1F)
SPIDERBOT_GLOVE = WeaponData(117, "Spiderbot Glove", 0x20)
BOUNCER = WeaponData(118, "Bouncer", 0x25)
MINITURRET_GLOVE = WeaponData(119, "Miniturret Glove", 0x29)
GRAVITY_BOMB = WeaponData(120, "Gravity Bomb", 0x2A)
ZODIAC = WeaponData(121, "Zodiac", 0x2B)
RYNO_II = WeaponData(122, "RYNO II", 0x2C)
SHIELD_CHARGER = WeaponData(123, "Shield Charger", 0x2D)
WALLOPER = WeaponData(124, "Walloper", 0x35)

HEAVY_LANCER = WeaponData(125, "Heavy Lancer", 0x3C)
KILONOID = WeaponData(126, "Kilonoid", 0x3D)
PLASMA_STORM = WeaponData(127, "Plasma Storm", 0x3E)
METEOR_GUN = WeaponData(128, "Meteor Gun", 0x3F)
MEGATURRET_GLOVE = WeaponData(129, "Megaturret Glove", 0x40)
MULTISTAR = WeaponData(130, "Multi-Star", 0x41)
VAPORIZER = WeaponData(131, "Vaporizer", 0x42)
HK_22 = WeaponData(132, "HK-22", 0x43)
BLITZ_CANNON = WeaponData(133, "Blitz Cannon", 0x44)
MEGAROCKET_CANNON = WeaponData(134, "Megarocket Cannon", 0x45)
TETRABOMB_GUN = WeaponData(135, "Tetrabomb Gun", 0x46)
MINI_NUKE = WeaponData(136, "Mini-Nuke", 0x47)
BLACK_SHEEPINATOR = WeaponData(137, "Black Sheepinator", 0x48)
CLANK_SHOCKER = WeaponData(138, "Clank Shocker", 0x49)
HEAVY_BOUNCER = WeaponData(139, "Heavy Bouncer", 0x4C)
TESLA_BARRIER = WeaponData(140, "Tesla Barrier", 0x4D)
TANKBOT_GLOVE = WeaponData(141, "Tankbot Glove", 0x4E)

MEGA_HEAVY_LANCER = WeaponData(142, "Mega Heavy Lancer", 0x4F)
MEGA_MINI_NUKE = WeaponData(143, "Mega Mini-Nuke", 0x51)
MEGA_MULTISTAR = WeaponData(144, "Mega Multi-Star", 0x53)
MEGA_HK_22 = WeaponData(145, "Mega HK-22", 0x55)
MEGA_VAPORIZER = WeaponData(146, "Mega Vaporizer", 0x57)
MEGA_MEGATURRET_GLOVE = WeaponData(147, "Mega Megaturret Glove", 0x59)
MEGA_BLITZ_CANNON = WeaponData(148, "Mega Blitz Cannon", 0x5B)
MEGA_KILONOID = WeaponData(149, "Mega Kilonoid", 0x5D)
MEGA_METEOR_GUN = WeaponData(150, "Mega Meteor Gun", 0x5F)
MEGA_HEAVY_BOUNCER = WeaponData(151, "Mega Heavy Bouncer", 0x61)
MEGA_MEGAROCKET_CANNON = WeaponData(152, "Mega Megarocket Cannon", 0x63)
MEGA_PLASMA_STORM = WeaponData(153, "Mega Plasma Storm", 0x65)
MEGA_TETRABOMB_GUN = WeaponData(154, "Mega Tetrabomb Gun", 0x67)
MEGA_TANKBOT_GLOVE = WeaponData(155, "Mega Tankbot Glove", 0x69)
MEGA_TESLA_BARRIER = WeaponData(156, "Mega Tesla Barrier", 0x6B)
MEGA_TESLA_CLAW = WeaponData(157, "Mega Tesla Claw", 0x72)
MEGA_BOMB_GLOVE = WeaponData(158, "Mega Bomb Glove", 0x73)
MEGA_WALLOPER = WeaponData(159, "Mega Walloper", 0x74)
MEGA_VISIBOMB_GUN = WeaponData(160, "Mega Visibomb Gun", 0x75)
MEGA_DECOY_GLOVE = WeaponData(161, "Mega Decoy Glove", 0x76)

ULTRA_HEAVY_LANCER = WeaponData(162, "Ultra Heavy Lancer", 0x50)
ULTRA_MINI_NUKE = WeaponData(163, "Ultra Mini-Nuke", 0x52)
ULTRA_MULTISTAR = WeaponData(164, "Ultra Multi-Star", 0x54)
ULTRA_HK_22 = WeaponData(165, "Ultra HK-22", 0x56)
ULTRA_VAPORIZER = WeaponData(166, "Ultra Vaporizer", 0x58)
ULTRA_MEGATURRET_GLOVE = WeaponData(167, "Ultra Megaturret Glove", 0x5A)
ULTRA_BLITZ_CANNON = WeaponData(168, "Ultra Blitz Cannon", 0x5C)
ULTRA_KILONOID = WeaponData(169, "Ultra Kilonoid", 0x5E)
ULTRA_METEOR_GUN = WeaponData(170, "Ultra Meteor Gun", 0x60)
ULTRA_HEAVY_BOUNCER = WeaponData(171, "Ultra Heavy Bouncer", 0x62)
ULTRA_MEGAROCKET_CANNON = WeaponData(172, "Ultra Megarocket Cannon", 0x64)
ULTRA_PLASMA_STORM = WeaponData(173, "Ultra Plasma Storm", 0x66)
ULTRA_TETRABOMB_GUN = WeaponData(174, "Ultra Tetrabomb Gun", 0x68)
ULTRA_TANKBOT_GLOVE = WeaponData(175, "Ultra Tankbot Glove", 0x6A)
ULTRA_TESLA_BARRIER = WeaponData(176, "Ultra Tesla Barrier", 0x6C)


@dataclass
class CoordData(ItemData):
    planet_number: int


# Coordinates
OOZLA_COORDS = CoordData(201, "Oozla Coordinates", 1)
MAKTAR_NEBULA_COORDS = CoordData(202, "Maktar Nebula Coordinates", 2)
ENDAKO_COORDS = CoordData(203, "Endako Coordinates", 3)
BARLOW_COORDS = CoordData(204, "Barlow Coordinates", 4)
FELTZIN_SYSTEM_COORDS = CoordData(205, "Feltzin System Coordinates", 5)
NOTAK_COORDS = CoordData(206, "Notak Coordinates", 6)
SIBERIUS_COORDS = CoordData(207, "Siberius Coordinates", 7)
TABORA_COORDS = CoordData(208, "Tabora Coordinates", 8)
DOBBO_COORDS = CoordData(209, "Dobbo Coordinates", 9)
HRUGIS_CLOUD_COORDS = CoordData(210, "Hrugis Cloud Coordinates", 10)
JOBA_COORDS = CoordData(211, "Joba Coordinates", 11)
TODANO_COORDS = CoordData(212, "Todano Coordinates", 12)
BOLDAN_COORDS = CoordData(213, "Boldan Coordinates", 13)
ARANOS_PRISON_COORDS = CoordData(214, "Aranos Prison Coordinates", 14)
GORN_COORDS = CoordData(215, "Gorn Coordinates", 15)
SNIVELAK_COORDS = CoordData(216, "Snivelak Coordinates", 16)
SMOLG_COORDS = CoordData(217, "Smolg Coordinates", 17)
DAMOSEL_COORDS = CoordData(218, "Damosel Coordinates", 18)
GRELBIN_COORDS = CoordData(219, "Grelbin Coordinates", 19)
YEEDIL_COORDS = CoordData(220, "Yeedil Coordinates", 20)


@dataclass
class CollectableData(ItemData):
    max_capacity: int


# Collectables
PLATINUM_BOLT = CollectableData(301, "Platinum Bolt", 40)
NANOTECH_BOOST = CollectableData(302, "Nanotech Boost", 10)
HYPNOMATIC_PART = CollectableData(303, "Hypnomatic Part", 3)


@dataclass
class ProgressiveUpgradeData(ItemData):
    progressive_names: list[str]
    get_level_func: Callable[['Rac2Interface'], int]
    set_level_func: Callable[['Rac2Interface', int], bool]


WRENCH_UPGRADE = ProgressiveUpgradeData(401, "OmniWrench Upgrade", ["OmniWrench 10000", "OmniWrench 12000"],
                                        lambda interface: interface.get_wrench_level(),
                                        lambda interface, level: interface.set_wrench_level(level))

ARMOR_UPGRADE = ProgressiveUpgradeData(402, "Armor Upgrade", ["Tetrafiber Armor", "Duraplate Armor",
                                                              "Electrosteel Armor", "Carbonox Armor"],
                                       lambda interface: interface.get_armor_level(),
                                       lambda interface, level: interface.set_armor_level(level))

EQUIPMENT: Sequence[EquipmentData] = [
    HELI_PACK,
    THRUSTER_PACK,
    MAPPER,
    ARMOR_MAGNETIZER,
    LEVITATOR,
    SWINGSHOT,
    GRAVITY_BOOTS,
    GRIND_BOOTS,
    GLIDER,
    DYNAMO,
    ELECTROLYZER,
    THERMANATOR,
    TRACTOR_BEAM,
    QWARK_STATUETTE,
    BOX_BREAKER,
    INFILTRATOR,
    CHARGE_BOOTS,
    HYPNOMATIC,
]
WEAPONS: Sequence[EquipmentData] = [
    CLANK_ZAPPER,
    BOMB_GLOVE,
    VISIBOMB_GUN,
    SHEEPINATOR,
    DECOY_GLOVE,
    TESLA_CLAW,
    CHOPPER,
    PULSE_RIFLE,
    SEEKER_GUN,
    HOVERBOMB_GUN,
    BLITZ_GUN,
    MINIROCKET_TUBE,
    PLASMA_COIL,
    LAVA_GUN,
    LANCER,
    SYNTHENOID,
    SPIDERBOT_GLOVE,
    BOUNCER,
    MINITURRET_GLOVE,
    GRAVITY_BOMB,
    ZODIAC,
    RYNO_II,
    SHIELD_CHARGER,
    WALLOPER
]
COORDS: Sequence[CoordData] = [
    OOZLA_COORDS,
    MAKTAR_NEBULA_COORDS,
    ENDAKO_COORDS,
    BARLOW_COORDS,
    FELTZIN_SYSTEM_COORDS,
    NOTAK_COORDS,
    SIBERIUS_COORDS,
    TABORA_COORDS,
    DOBBO_COORDS,
    HRUGIS_CLOUD_COORDS,
    JOBA_COORDS,
    TODANO_COORDS,
    BOLDAN_COORDS,
    ARANOS_PRISON_COORDS,
    GORN_COORDS,
    SNIVELAK_COORDS,
    SMOLG_COORDS,
    DAMOSEL_COORDS,
    GRELBIN_COORDS,
    YEEDIL_COORDS,
]
STARTABLE_COORDS: Sequence[CoordData] = [
    OOZLA_COORDS,
    MAKTAR_NEBULA_COORDS,
    ENDAKO_COORDS,
    FELTZIN_SYSTEM_COORDS,
    NOTAK_COORDS,
    TODANO_COORDS,
]
COLLECTABLES: Sequence[CollectableData] = [
    PLATINUM_BOLT,
    NANOTECH_BOOST,
    HYPNOMATIC_PART,
]
UPGRADES: Sequence[ProgressiveUpgradeData] = [
    WRENCH_UPGRADE,
    ARMOR_UPGRADE
]
ALL: Sequence[ItemData] = [*EQUIPMENT, *WEAPONS, *COORDS, *COLLECTABLES, *UPGRADES]
QUICK_SELECTABLE: Sequence[ItemData] = [
    *WEAPONS,
    SWINGSHOT,
    DYNAMO,
    THERMANATOR,
    TRACTOR_BEAM,
    HYPNOMATIC,
]


def from_id(item_id: int) -> ItemData:
    matching = [item for item in ALL if item.item_id == item_id]
    assert len(matching) > 0, f"No item data with id '{item_id}'."
    assert len(matching) < 2, f"Multiple item data with id '{item_id}'. Please report."
    return matching[0]


def from_name(item_name: str) -> ItemData:
    matching = [item for item in ALL if item.name == item_name]
    assert len(matching) > 0, f"No item data with name '{item_name}'."
    assert len(matching) < 2, f"Multiple item data with name '{item_name}'. Please report."
    return matching[0]


def coord_for_planet(number: int) -> CoordData:
    matching = [coord for coord in COORDS if coord.planet_number == number]
    assert len(matching) > 0, f"No coords for planet number '{number}'."
    assert len(matching) < 2, f"Multiple coords for planet number '{number}'. Please report."
    return matching[0]
