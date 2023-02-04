import colour
from entity import Item
from components.consumables import Magazine

"""
GLOCK 9mm
"""

glock_mag_9mm = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Magazine 9mm - Standard Capacity",
    weight=0.096,
    stacking=None,
    description='9mm Glock magazine - 17 round capacity',
    usable_properties=Magazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=['9mm', ],
        mag_capacity=17,
        magazine_size='small',
        ap_to_load=300,
    )
)

glock_mag_9mm_33 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Magazine 9mm - Extended",
    weight=0.15,
    stacking=None,
    description='extended 9mm Glock magazine - 33 round capacity',
    usable_properties=Magazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=['9mm', ],
        mag_capacity=33,
        magazine_size='medium',
        ap_to_load=330,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        spread_mod=1.03,
        equip_ap_mod=1.06,
    )
)

glock_mag_9mm_50 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Drum 9mm - 50 Rounds",
    weight=0.6,
    stacking=None,
    description='9mm Glock drum - 50 round capacity',
    usable_properties=Magazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=['9mm', ],
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.15,
        spread_mod=1.09,
        equip_ap_mod=1.18,
        failure_chance=2,
    )
)

glock_mag_9mm_100 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Glock Beta Mag 9mm - 100 Rounds",
    weight=1.36,
    stacking=None,
    description='9mm Glock Beta Mag - 100 round capacity',
    usable_properties=Magazine(
        magazine_type='Glock 9mm',
        compatible_bullet_type=['9mm', ],
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.21,
        ap_distance_cost_mod=1.23,
        spread_mod=1.16,
        equip_ap_mod=1.25,
        failure_chance=3,
    )
)

"""
MAC 10 45
"""

mac10_mag_45 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Magazine",
    weight=0.34,
    stacking=None,
    description='M10/45 magazine .45 ACP - 30 round capacity. Originally made for the M3 grease gun and '
                'later retrofitted for the M10/45.',
    usable_properties=Magazine(
        magazine_type='M10/45',
        compatible_bullet_type=['.45 ACP', ],
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
    )
)

mac10_mag_45_extended = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/45 Extended Magazine",
    weight=0.4,
    stacking=None,
    description='M10/45 magazine .45 ACP - 40 round capacity. An original magazine modified for greater capacity',
    usable_properties=Magazine(
        magazine_type='M10/45',
        compatible_bullet_type=['.45 ACP', ],
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.05,
        spread_mod=1.03,
        equip_ap_mod=1.05,
    )
)

mac10_mag_9 = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="M10/9 Magazine",
    weight=0.32,
    stacking=None,
    description='M10/9 Magazine 9mm - 32 round capacity',
    usable_properties=Magazine(
        magazine_type='M10/9',
        compatible_bullet_type=['9mm', ],
        mag_capacity=32,
        magazine_size='medium',
        ap_to_load=300,
    )
)

"""
Mosin Nagant
"""

mosin_nagant = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Magazine",
    weight=0.23,
    stacking=None,
    description='An aftermarket "Archangel" 10 round capacity polymer magazine for 7.62x54R Mosin-Nagant rifles '
                'designed by ProMag',
    usable_properties=Magazine(
        magazine_type='Mosin-Nagant',
        compatible_bullet_type=['7.62x54R', ],
        mag_capacity=10,
        magazine_size='large',
        ap_to_load=500,
    )
)

mosin_clip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Mosin-Nagant Clip",
    weight=0.0085,
    stacking=None,
    description='A 5 round capacity clip for Mosin-Nagant rifles',
    usable_properties=Magazine(
        magazine_type='Mosin-Nagant Clip',
        compatible_bullet_type=['7.62x54R', ],
        mag_capacity=5,
        magazine_size='small',
        ap_to_load=500,
    )
)

"""
SKS
"""

sks_clip = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="SKS Clip",
    weight=0.011,
    stacking=None,
    description='A 10 round capacity stripper clip for SKS rifles',
    usable_properties=Magazine(
        magazine_type='SKS Clip',
        compatible_bullet_type=['7.62x39', ],
        mag_capacity=10,
        magazine_size='small',
        ap_to_load=500,
    )
)


"""
AK 7.62x39
"""

ak762_30rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 7.62x39 30 Round Magazine",
    weight=0.37,
    stacking=None,
    description='A steel 30 round capacity 7.62x39 AK magazine',
    usable_properties=Magazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=['7.62x39', ],
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
    )
)

ak762_40rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 7.62x39 40 Round Magazine",
    weight=0.46,
    stacking=None,
    description='A steel 40 round capacity 7.62x39 AK magazine designed for RPK light machine guns',
    usable_properties=Magazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=['7.62x39', ],
        mag_capacity=40,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.04,
        ap_distance_cost_mod=1.03,
        spread_mod=1.02,
        equip_ap_mod=1.05,
    )
)

ak762_60rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AC-Unity AK 7.62x39 Quad Magazine",
    weight=0.35,
    stacking=None,
    description='A polymer 60 round capacity 7.62x39 AK quad stack magazine',
    usable_properties=Magazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=['7.62x39', ],
        mag_capacity=60,
        magazine_size='medium',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.08,
        spread_mod=1.05,
        equip_ap_mod=1.06,
        failure_chance=2,
    )
)

ak762_75rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 7.62x39 75 Round Drum Magazine",
    weight=0.2,
    stacking=None,
    description='75 round capacity 7.62x39 AK drum magazine',
    usable_properties=Magazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=['7.62x39', ],
        mag_capacity=75,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.11,
        ap_distance_cost_mod=1.12,
        spread_mod=1.09,
        equip_ap_mod=1.15,
        failure_chance=3,
    )
)

ak762_100rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 7.62x39 100 Round Drum",
    weight=1.3,
    stacking=None,
    description='100 round capacity 7.62x39 AK drum magazine',
    usable_properties=Magazine(
        magazine_type='AK 7.62x39',
        compatible_bullet_type=['7.62x39', ],
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.2,
        ap_distance_cost_mod=1.22,
        spread_mod=1.16,
        equip_ap_mod=1.25,
        failure_chance=3,
    )
)

"""
AK 5.45x39
"""

ak545_30rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 5.45x39 Magazine",
    weight=0.215,
    stacking=None,
    description='Standard 30 round capacity 5.45x39 AK magazine',
    usable_properties=Magazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=['5.45x39', ],
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
    )
)

ak545_45rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="RPK-74 5.45x39 Magazine",
    weight=0.3,
    stacking=None,
    description='45 round capacity 5.45x39 AK magazine designed for RPK-74 light machine guns',
    usable_properties=Magazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=['5.45x39', ],
        mag_capacity=45,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.04,
        spread_mod=1.03,
        equip_ap_mod=1.07,
    )
)

ak545_60rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 5.45x39 Quad Magazine",
    weight=0.3,
    stacking=None,
    description='60 round capacity 5.45x39 AK quad stack magazine',
    usable_properties=Magazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=['5.45x39', ],
        mag_capacity=60,
        magazine_size='medium',
        ap_to_load=500,
        target_acquisition_ap_mod=1.06,
        ap_distance_cost_mod=1.06,
        spread_mod=1.05,
        equip_ap_mod=1.05,
        failure_chance=2,
    )
)

ak545_100rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="RPK-16 5.45x39 95 Round Drum",
    weight=0.68,
    stacking=None,
    description='95 round capacity 5.45x39 AK drum magazine intended for the RPK-16',
    usable_properties=Magazine(
        magazine_type='AK 5.45x39',
        compatible_bullet_type=['5.45x39', ],
        mag_capacity=95,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.19,
        ap_distance_cost_mod=1.2,
        spread_mod=1.15,
        equip_ap_mod=1.25,
        failure_chance=3,
    )
)

"""
AK 5.56x45
"""

ak556_30rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AK 5.56x45 Magazine",
    weight=0.215,
    stacking=None,
    description='Standard 30 round capacity 5.56x45 AK magazine made for the AK-101',
    usable_properties=Magazine(
        magazine_type='AK 5.56x45',
        compatible_bullet_type=['5.56x45', ],
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
    )
)

"""
STANAG
"""

stanag_30rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="STANAG 30 Round Magazine",
    weight=0.117,
    stacking=None,
    description='Standard 30 round capacity STANAG magazine',
    usable_properties=Magazine(
        magazine_type='STANAG',
        compatible_bullet_type=['5.56x45', '.300 Blackout'],
        mag_capacity=30,
        magazine_size='medium',
        ap_to_load=300,
    )
)

stanag_40rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="STANAG 40 Round Magazine",
    weight=0.2,
    stacking=None,
    description='40 round capacity STANAG magazine',
    usable_properties=Magazine(
        magazine_type='STANAG',
        compatible_bullet_type=['5.56x45', '.300 Blackout'],
        mag_capacity=40,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.03,
        ap_distance_cost_mod=1.02,
        spread_mod=1.02,
        equip_ap_mod=1.04,
    )
)

stanag_50rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="STANAG 50 Round Drum Magazine",
    weight=0.9,
    stacking=None,
    description='50 round capacity STANAG drum magazine designed by F5-MFG',
    usable_properties=Magazine(
        magazine_type='STANAG',
        compatible_bullet_type=['5.56x45', '.300 Blackout'],
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=400,
        target_acquisition_ap_mod=1.06,
        ap_distance_cost_mod=1.06,
        spread_mod=1.05,
        equip_ap_mod=1.09,
        failure_chance=1,
    )
)

stanag_60rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="STANAG 60 Round Magazine",
    weight=0.18,
    stacking=None,
    description='60 round capacity STANAG quad stack magazine designed by SureFire',
    usable_properties=Magazine(
        magazine_type='STANAG',
        compatible_bullet_type=['5.56x45', '.300 Blackout'],
        mag_capacity=60,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.07,
        spread_mod=1.04,
        equip_ap_mod=1.07,
        failure_chance=2,
    )
)

stanag_100rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="STANAG Beta C 100 Round Drum Magazine",
    weight=1.81,
    stacking=None,
    description='100 round capacity STANAG Beta C drum magazine',
    usable_properties=Magazine(
        magazine_type='STANAG',
        compatible_bullet_type=['5.56x45', '.300 Blackout'],
        mag_capacity=60,
        magazine_size='large',
        ap_to_load=600,
        target_acquisition_ap_mod=1.18,
        ap_distance_cost_mod=1.18,
        spread_mod=1.13,
        equip_ap_mod=1.25,
        failure_chance=3,
    )
)

"""
AR-10
"""

ar10_20rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 7.62x51 20 Round Magazine",
    weight=0.17,
    stacking=None,
    description='A polymer 20 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=Magazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=['7.62x51', ],
        mag_capacity=20,
        magazine_size='medium',
        ap_to_load=300,
    )
)

ar10_25rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 7.62x51 25 Round Magazine",
    weight=0.206,
    stacking=None,
    description='A polymer 25 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=Magazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=['7.62x51', ],
        mag_capacity=25,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.02,
        ap_distance_cost_mod=1.01,
        spread_mod=1.01,
        equip_ap_mod=1.02,
    )
)

ar10_40rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 7.62x51 40 Round Magazine",
    weight=0.226,
    stacking=None,
    description='A polymer 40 round 7.62x51 magazine for AR-10 type rifles',
    usable_properties=Magazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=['7.62x51', ],
        mag_capacity=40,
        magazine_size='large',
        ap_to_load=400,
        target_acquisition_ap_mod=1.05,
        ap_distance_cost_mod=1.04,
        spread_mod=1.04,
        equip_ap_mod=1.06,
        failure_chance=1,
    )
)

ar10_50rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="AR-10 7.62x51 50 Round Drum Magazine",
    weight=0.771,
    stacking=None,
    description='A polymer 50 round 7.62x51 drum magazine for AR-10 type rifles',
    usable_properties=Magazine(
        magazine_type='AR10 7.62x51',
        compatible_bullet_type=['7.62x51', ],
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.07,
        ap_distance_cost_mod=1.06,
        spread_mod=1.06,
        equip_ap_mod=1.12,
        failure_chance=2,
    )
)

"""
Calico
"""

calico_9mm_50rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Calico 9mm 50 Round Magazine",
    weight=0.5,
    stacking=None,
    description='50 round capacity 9mm helical magazine by Calico',
    usable_properties=Magazine(
        magazine_type='Calico 9mm',
        compatible_bullet_type=['9mm', ],
        mag_capacity=50,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.13,
        ap_distance_cost_mod=1.17,
        spread_mod=1.09,
        equip_ap_mod=1.14,
        failure_chance=1,
    )
)

calico_9mm_100rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Calico 9mm 100 Round Magazine",
    weight=1.03,
    stacking=None,
    description='100 round capacity 9mm helical magazine by Calico',
    usable_properties=Magazine(
        magazine_type='Calico 9mm',
        compatible_bullet_type=['9mm', ],
        mag_capacity=100,
        magazine_size='large',
        ap_to_load=700,
        target_acquisition_ap_mod=1.23,
        ap_distance_cost_mod=1.25,
        spread_mod=1.16,
        equip_ap_mod=1.3,
        failure_chance=1,
    )
)

"""
Suomi M31
"""

m31_9mm_36rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Suomi M31 9mm 36 Round Magazine",
    weight=0.34,
    stacking=None,
    description='36 round capacity 9mm magazine designed for the Suomi M31 submachinegun',
    usable_properties=Magazine(
        magazine_type='Suomi M31',
        compatible_bullet_type=['9mm', ],
        mag_capacity=36,
        magazine_size='medium',
        ap_to_load=300,
        target_acquisition_ap_mod=1.02,
        ap_distance_cost_mod=1.03,
        spread_mod=1.01,
        equip_ap_mod=1.03,
    )
)

m31_9mm_71rd = Item(
    x=0, y=0,
    char="!",
    fg_colour=colour.LIGHT_GRAY,
    name="Suomi M31 9mm 71 Round Drum",
    weight=0.68,
    stacking=None,
    description='71 round capacity 9mm drug magazine designed for the Suomi M31 submachinegun',
    usable_properties=Magazine(
        magazine_type='Suomi M31',
        compatible_bullet_type=['9mm', ],
        mag_capacity=71,
        magazine_size='large',
        ap_to_load=500,
        target_acquisition_ap_mod=1.16,
        ap_distance_cost_mod=1.18,
        spread_mod=1.13,
        equip_ap_mod=1.22,
        failure_chance=2,
    )
)

magazine_dict = {
    "Glock 9mm": ((glock_mag_9mm, 2), (glock_mag_9mm_33, 1))
}
