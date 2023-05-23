import csv

products = [
 {
  "product_name": "Macbook Pro 512GB Stříbrný",
  "price": 25896,
  "discount": 0,
  "stock": 10,
  "display_size": 13.3,
  "display_resolution": "2560 x 1600",
  "operating_system": "macOS",
  "operating_memory": 8,
  "description": "Macbook Pro je výkonný a univerzální notebook navržený pro profesionály a náročné uživatele. "
                 "S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že zvládnete "
                 "jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Díky Retina displeji "
                 "si užijete nádherné podrobnosti a živé barvy ve vysokém rozlišení. Přesné a ostré obrazy vás přenáší "
                 "do světa, kde se každý detail zobrazuje s ohromující jasností. Procesor Intel Core i7 a 4 jádra "
                 "vám poskytují dostatečnou sílu pro plynulý běh náročných aplikací a multitasking. Spoléhejte na "
                 "rychlé odezvy a plynulé přepínání mezi různými úkoly bez zbytečných prodlev. Grafická karta AMD "
                 "Radeon Pro 5500M s 4 GB paměti vám umožňuje vytvářet a upravovat grafiku a videa s precizností. "
                 "Prohlížejte si své projekty ve vysokém rozlišení a sledujte, jak se vám tvorba stává živou.SSD "
                 "kapacitou 512 GB poskytuje rychlé načítání systému a aplikací, a to vše s dostatečným úložným "
                 "prostorem pro vaše soubory a dokumenty. Můžete se spolehnout na rychlý a efektivní přístup k vašim"
                 " datům. Macbook Pro je vyroben z odolného hliníku, který zajišťuje dlouhodobou spolehlivost a "
                 "odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení notebooku a využití při práci"
                 " nebo na cestách. S Macbook Pro získáte výkonný a spolehlivý notebook, který vám umožní realizovat"
                 " vaše profesionální ambice a těšit se z kvalitního multimediálního zážitku.",
  "subheading": "Prožijte prvotřídní výkon a úžasné vizuální efekty s Macbook Pro.",
  "visit_count": 14560,
  "product_type": "Notebook",
  "brand_id": 1,
  "category_id": 4,
  "display_frequency": 144,
  "display_nits": 1600,
  "display_type": "Retina",
  "processor": "Intel Core i7",
  "processor_cores": 4,
  "graphics_card": "AMD Radeon Pro 5500M",
  "graphics_memory": 4,
  "ssd_capacity": 512,
  "hdd_capacity": 0,
  "ssd": True,
  "hdd": False,
  "light_keyboard": True,
  "num_keyboard": False,
  "touch_screen": False,
  "fingerprint_reader": False,
  "memory_card_reader": False,
  "usb_c_charging": True,
  "battery_capacity": 58,
  "construction": "celokovový",
  "height": 0.61,
  "height_units": "mm",
  "width": 11.97,
  "width_units": "mm",
  "depth": 8.36,
  "depth_units": "mm",
  "weight": 3.02,
  "weight_units": "kg",
  "color": "stříbrná",
  "usb_ports": 4,
  "hdmi_ports": 1,
  "audio_jack": True,
  "usb_3_0": True,
  "usb_2_0": False,
  "cd_dvd_drive": False,
  "product_image": "test_image_mac_book_pro.jpeg",
 },

 {
        "product_name": "Macbook Pro 512GB/8GB Stříbrný",
        "price": 35621,
        "discount": 0,
        "stock": 10,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 8,
        "description": "Macbook Pro je výkonný a univerzální notebook navržený pro profesionály a náročné uživatele. "
                       "S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že zvládnete "
                       "jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Díky Retina displeji "
                       "si užijete nádherné podrobnosti a živé barvy ve vysokém rozlišení. Přesné a ostré obrazy "
                       "vás přenáší do světa, kde se každý detail zobrazuje s ohromující jasností. Procesor"
                       " Intel Core i7 a 4 jádra vám poskytují dostatečnou sílu pro plynulý běh náročných"
                       " aplikací a multitasking. Spoléhejte na rychlé odezvy a plynulé přepínání mezi"
                       " různými úkoly bez zbytečných prodlev. Grafická karta AMD "
                       "Radeon Pro 5500M s 4 GB paměti vám umožňuje vytvářet a upravovat "
                       "grafiku a videa s precizností. "
                       "Prohlížejte si své projekty ve vysokém rozlišení a sledujte, jak se vám tvorba stává živou"
                       "vyroben z odolného hliníku, který zajišťuje dlouhodobou spolehlivost a "
                       "odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení "
                       "notebooku a využití při práci"
                       " nebo na cestách. S Macbook Pro získáte výkonný a spolehlivý notebook, který vám "
                       "umožní realizovat"
                       " vaše profesionální ambice a těšit se z kvalitního multimediálního zážitku.",
        "subheading": "Prožijte prvotřídní výkon a úžasné vizuální efekty s Macbook Pro.",
        "visit_count": 14560,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 144,
        "display_nits": 1600,
        "display_type": "Retina",
        "processor": "Intel Core i7",
        "processor_cores": 4,
        "graphics_card": "AMD Radeon Pro 5500M",
        "graphics_memory": 4,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 3.02,
        "weight_units": "kg",
        "color": "stříbrná",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },

 {
        "product_name": "Macbook Pro 512GB/16GB Stříbrný",
        "price": 35621,
        "discount": 0,
        "stock": 10,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 16,
        "description": "Macbook Pro je výkonný a univerzální notebook navržený pro profesionály a náročné uživatele. "
                       "S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že zvládnete "
                       "jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Díky Retina displeji "
                       "si užijete nádherné podrobnosti a živé barvy ve vysokém rozlišení. Přesné a ostré obrazy "
                       "vás přenáší do světa, kde se každý detail zobrazuje s ohromující jasností. Procesor"
                       " Intel Core i7 a 4 jádra vám poskytují dostatečnou sílu pro plynulý běh náročných"
                       " aplikací a multitasking. Spoléhejte na rychlé odezvy a plynulé přepínání mezi"
                       " různými úkoly bez zbytečných prodlev. Grafická karta AMD "
                       "Radeon Pro 5500M s 4 GB paměti vám umožňuje vytvářet a upravovat "
                       "grafiku a videa s precizností. "
                       "Prohlížejte si své projekty ve vysokém rozlišení a sledujte, jak se vám tvorba stává živou"
                       "vyroben z odolného hliníku, který zajišťuje dlouhodobou spolehlivost a "
                       "odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení "
                       "notebooku a využití při práci"
                       " nebo na cestách. S Macbook Pro získáte výkonný a spolehlivý notebook, který vám "
                       "umožní realizovat"
                       " vaše profesionální ambice a těšit se z kvalitního multimediálního zážitku.",
        "subheading": "Prožijte prvotřídní výkon a úžasné vizuální efekty s Macbook Pro.",
        "visit_count": 14560,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 144,
        "display_nits": 1600,
        "display_type": "Retina",
        "processor": "Intel Core i7",
        "processor_cores": 4,
        "graphics_card": "AMD Radeon Pro 5500M",
        "graphics_memory": 4,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 3.02,
        "weight_units": "kg",
        "color": "stříbrná",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },

 {
  "product_name": "Macbook Pro M1 512GB/8GB Stříbrný",
  "price": 43758,
  "discount": 0,
  "stock": 15,
  "display_size": 13.3,
  "display_resolution": "2560 x 1600",
  "operating_system": "macOS",
  "operating_memory": 8,
  "description":   "Macbook Pro s čipem M1 je výkonný a univerzální notebook navržený pro profesionály a náročné "
                   "uživatele. S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že"
                   " zvládnete jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Retina "
                   "displej nabízí nádherné detaily a živé barvy ve vysokém rozlišení, ponoří vás do světa, "
                   "kde se každý detail zobrazuje s ohromující jasností. Čip M1, první čip od Applu "
                   "navržený speciálně pro Mac, poskytuje výjimečnou energetickou efektivitu a výkon,"
                   " umožňuje plynulý multitasking a bezproblémové provádění náročných úkolů. Integrovaná 8-jádrová GPU"
                   " zajišťuje rychlé zpracování grafiky, umožňuje vám tvořit a upravovat grafiku a videa s"
                   " precizností. Sledujte své projekty ve vysokém rozlišení a sledujte, jak se vaše tvorba stává "
                   "živou. S kapacitou 512 GB SSD poskytuje Macbook Pro rychlé načítání systému a aplikací, "
                   "a to vše s dostatečným úložným prostorem pro vaše soubory a dokumenty. Zažijte rychlý a "
                   "efektivní přístup k vašim datům. Macbook Pro je vyroben z odolného hliníku, což zajišťuje "
                   "dlouhodobou spolehlivost a odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení"
                   "notebooku a využití při práci nebo na cestách. S Macbook Pro M1 získáte výkonný a spolehlivý "
                   "notebook, který vám umožní naplnit vaše profesionální ambice a těšit se z kvalitního "
                   "multimediálního zážitku.",
  "subheading": "Zažijte špičkový výkon a ohromující obraz s Macbookem Pro M1.",
  "visit_count": 12540,
  "product_type": "Notebook",
  "brand_id": 1,
  "category_id": 4,
  "display_frequency": 60,
  "display_nits": 500,
  "display_type": "Retina",
  "processor": "Apple M1",
  "processor_cores": 8,
  "graphics_card": "Apple M1",
  "graphics_memory": 8,
  "ssd_capacity": 512,
  "hdd_capacity": 0,
  "ssd": True,
  "hdd": False,
  "light_keyboard": True,
  "num_keyboard": False,
  "touch_screen": False,
  "fingerprint_reader": False,
  "memory_card_reader": False,
  "usb_c_charging": True,
  "battery_capacity": 58,
  "construction": "celokovový",
  "height": 0.61,
  "height_units": "mm",
  "width": 11.97,
  "width_units": "mm",
  "depth": 8.36,
  "depth_units": "mm",
  "weight": 1.4,
  "weight_units": "kg",
  "color": "stříbrná",
  "usb_ports": 4,
  "hdmi_ports": 1,
  "audio_jack": True,
  "usb_3_0": True,
  "usb_2_0": False,
  "cd_dvd_drive": False,
  "product_image": "test_image_mac_book_pro.jpeg"
 },

 {
  "product_name": "Macbook Pro M1 512GB/16GB Stříbrný",
  "price": 47623,
  "discount": 0,
  "stock": 15,
  "display_size": 13.3,
  "display_resolution": "2560 x 1600",
  "operating_system": "macOS",
  "operating_memory": 16,
  "description":   "Macbook Pro s čipem M1 je výkonný a univerzální notebook navržený pro profesionály a náročné "
                   "uživatele. S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že"
                   " zvládnete jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Retina "
                   "displej nabízí nádherné detaily a živé barvy ve vysokém rozlišení, ponoří vás do světa, "
                   "kde se každý detail zobrazuje s ohromující jasností. Čip M1, první čip od Applu "
                   "navržený speciálně pro Mac, poskytuje výjimečnou energetickou efektivitu a výkon,"
                   " umožňuje plynulý multitasking a bezproblémové provádění náročných úkolů. Integrovaná 8-jádrová GPU"
                   " zajišťuje rychlé zpracování grafiky, umožňuje vám tvořit a upravovat grafiku a videa s"
                   " precizností. Sledujte své projekty ve vysokém rozlišení a sledujte, jak se vaše tvorba stává "
                   "živou. S kapacitou 512 GB SSD poskytuje Macbook Pro rychlé načítání systému a aplikací, "
                   "a to vše s dostatečným úložným prostorem pro vaše soubory a dokumenty. Zažijte rychlý a "
                   "efektivní přístup k vašim datům. Macbook Pro je vyroben z odolného hliníku, což zajišťuje "
                   "dlouhodobou spolehlivost a odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení"
                   "notebooku a využití při práci nebo na cestách. S Macbook Pro M1 získáte výkonný a spolehlivý "
                   "notebook, který vám umožní naplnit vaše profesionální ambice a těšit se z kvalitního "
                   "multimediálního zážitku.",
  "subheading": "Zažijte špičkový výkon a ohromující obraz s Macbookem Pro M1.",
  "visit_count": 12540,
  "product_type": "Notebook",
  "brand_id": 1,
  "category_id": 4,
  "display_frequency": 60,
  "display_nits": 500,
  "display_type": "Retina",
  "processor": "Apple M1",
  "processor_cores": 8,
  "graphics_card": "Apple M1",
  "graphics_memory": 8,
  "ssd_capacity": 512,
  "hdd_capacity": 0,
  "ssd": True,
  "hdd": False,
  "light_keyboard": True,
  "num_keyboard": False,
  "touch_screen": False,
  "fingerprint_reader": False,
  "memory_card_reader": False,
  "usb_c_charging": True,
  "battery_capacity": 58,
  "construction": "celokovový",
  "height": 0.61,
  "height_units": "mm",
  "width": 11.97,
  "width_units": "mm",
  "depth": 8.36,
  "depth_units": "mm",
  "weight": 1.4,
  "weight_units": "kg",
  "color": "stříbrná",
  "usb_ports": 4,
  "hdmi_ports": 1,
  "audio_jack": True,
  "usb_3_0": True,
  "usb_2_0": False,
  "cd_dvd_drive": False,
  "product_image": "test_image_mac_book_pro.jpeg"
 },
 {
    "product_name": "Macbook Air M1 512GB/16GB Stříbrný",
    "price": 32999,
    "discount": 0,
    "stock": 10,
    "display_size": 13.3,
    "display_resolution": "2560 x 1600",
    "operating_system": "macOS",
    "operating_memory": 16,
    "description": "Macbook Air s čipem M1 je výkonný a přenosný notebook navržený pro každodenní použití a mobilitu. "
    "Díky svému špičkovému výkonu a ohromujícímu zobrazení budete mít jistotu, že zvládnete každý úkol "
    "a budete mít plynulý přístup k nejnovějším aplikacím a programům. Retina displej nabízí vysoké "
    "rozlišení a živé barvy, které vás pohltí a umožní vám vnímat každý detail s úchvatnou jasností. "
    "Čip M1, první čip navržený speciálně pro Mac od společnosti Apple, poskytuje vynikající energetickou "
    "účinnost a výkon, což umožňuje plynulé multitasking a snadné zvládnutí náročných úkolů. Díky integrované "
    "7-jádrové GPU můžete rychle zpracovávat grafiku a tvořit a upravovat grafiku a videa s vysokou přesností. "
    "Prohlížejte si své projekty vysokým rozlišením a sledujte, jak ožívají vaše vize. S kapacitou 512 GB SSD "
    "poskytuje Macbook Air rychlé načítání systému a aplikací a dostatek úložného prostoru pro vaše soubory a "
    "dokumenty. Zažijte rychlý a efektivní přístup ke svým datům. Macbook Air je vyroben z odolného hliníkového "
    "těla, které zajišťuje dlouhodobou spolehlivost a odolnost. Jeho tenký a lehký design vám umožní snadné "
    "přenášení a používání notebooku všude, kde jste. S Macbookem Air M1 získáte výkonný a spolehlivý notebook, "
    "který vám umožní naplnit vaše každodenní potřeby a vychutnat si vysokou kvalitu multimediálního zážitku.",
    "subheading": "Zažijte výkonnost a pohodlí s Macbookem Air M1.",
    "visit_count": 9823,
    "product_type": "Notebook",
    "brand_id": 1,
    "category_id": 4,
    "display_frequency": 60,
    "display_nits": 400,
    "display_type": "Retina",
    "processor": "Apple M1",
    "processor_cores": 8,
    "graphics_card": "Apple M1",
    "graphics_memory": 7,
    "ssd_capacity": 512,
    "hdd_capacity": 0,
    "ssd": True,
    "hdd": False,
    "light_keyboard": True,
    "num_keyboard": False,
    "touch_screen": False,
    "fingerprint_reader": False,
    "memory_card_reader": False,
    "usb_c_charging": True,
    "battery_capacity": 49.9,
    "construction": "celokovový",
    "height": 0.41,
    "height_units": "mm",
    "width": 11.97,
    "width_units": "mm",
    "depth": 8.36,
    "depth_units": "mm",
    "weight": 1.29,
    "weight_units": "kg",
    "color": "stříbrná",
    "usb_ports": 2,
    "hdmi_ports": 1,
    "audio_jack": True,
    "usb_3_0": True,
    "usb_2_0": False,
    "cd_dvd_drive": False,
    "product_image": "test_image_mac_book_pro.jpeg"
 },

    {
        "product_name": "Macbook Pro 512GB Šedý",
        "price": 25896,
        "discount": 0,
        "stock": 10,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 8,
        "description": "Macbook Pro je výkonný a univerzální notebook navržený pro profesionály a náročné uživatele. "
                       "S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že zvládnete "
                       "jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Díky Retina displeji "
                       "si užijete nádherné podrobnosti a živé barvy ve vysokém rozlišení. Přesné a ostré obrazy vás přenáší "
                       "do světa, kde se každý detail zobrazuje s ohromující jasností. Procesor Intel Core i7 a 4 jádra "
                       "vám poskytují dostatečnou sílu pro plynulý běh náročných aplikací a multitasking. Spoléhejte na "
                       "rychlé odezvy a plynulé přepínání mezi různými úkoly bez zbytečných prodlev. Grafická karta AMD "
                       "Radeon Pro 5500M s 4 GB paměti vám umožňuje vytvářet a upravovat grafiku a videa s precizností. "
                       "Prohlížejte si své projekty ve vysokém rozlišení a sledujte, jak se vám tvorba stává živou.SSD "
                       "kapacitou 512 GB poskytuje rychlé načítání systému a aplikací, a to vše s dostatečným úložným "
                       "prostorem pro vaše soubory a dokumenty. Můžete se spolehnout na rychlý a efektivní přístup k vašim"
                       " datům. Macbook Pro je vyroben z odolného hliníku, který zajišťuje dlouhodobou spolehlivost a "
                       "odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení notebooku a využití při práci"
                       " nebo na cestách. S Macbook Pro získáte výkonný a spolehlivý notebook, který vám umožní realizovat"
                       " vaše profesionální ambice a těšit se z kvalitního multimediálního zážitku.",
        "subheading": "Prožijte prvotřídní výkon a úžasné vizuální efekty s Macbook Pro.",
        "visit_count": 14560,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 144,
        "display_nits": 1600,
        "display_type": "Retina",
        "processor": "Intel Core i7",
        "processor_cores": 4,
        "graphics_card": "AMD Radeon Pro 5500M",
        "graphics_memory": 4,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 3.02,
        "weight_units": "kg",
        "color": "šedá",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg",
    },

    {
        "product_name": "Macbook Pro 512GB/8GB Šedý",
        "price": 35621,
        "discount": 0,
        "stock": 10,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 8,
        "description": "Macbook Pro je výkonný a univerzální notebook navržený pro profesionály a náročné uživatele. "
                       "S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že zvládnete "
                       "jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Díky Retina displeji "
                       "si užijete nádherné podrobnosti a živé barvy ve vysokém rozlišení. Přesné a ostré obrazy "
                       "vás přenáší do světa, kde se každý detail zobrazuje s ohromující jasností. Procesor"
                       " Intel Core i7 a 4 jádra vám poskytují dostatečnou sílu pro plynulý běh náročných"
                       " aplikací a multitasking. Spoléhejte na rychlé odezvy a plynulé přepínání mezi"
                       " různými úkoly bez zbytečných prodlev. Grafická karta AMD "
                       "Radeon Pro 5500M s 4 GB paměti vám umožňuje vytvářet a upravovat "
                       "grafiku a videa s precizností. "
                       "Prohlížejte si své projekty ve vysokém rozlišení a sledujte, jak se vám tvorba stává živou"
                       "vyroben z odolného hliníku, který zajišťuje dlouhodobou spolehlivost a "
                       "odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení "
                       "notebooku a využití při práci"
                       " nebo na cestách. S Macbook Pro získáte výkonný a spolehlivý notebook, který vám "
                       "umožní realizovat"
                       " vaše profesionální ambice a těšit se z kvalitního multimediálního zážitku.",
        "subheading": "Prožijte prvotřídní výkon a úžasné vizuální efekty s Macbook Pro.",
        "visit_count": 14560,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 144,
        "display_nits": 1600,
        "display_type": "Retina",
        "processor": "Intel Core i7",
        "processor_cores": 4,
        "graphics_card": "AMD Radeon Pro 5500M",
        "graphics_memory": 4,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 3.02,
        "weight_units": "kg",
        "color": "šedá",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },

    {
        "product_name": "Macbook Pro 512GB/16GB Šedý",
        "price": 35621,
        "discount": 0,
        "stock": 10,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 16,
        "description": "Macbook Pro je výkonný a univerzální notebook navržený pro profesionály a náročné uživatele. "
                       "S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že zvládnete "
                       "jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Díky Retina displeji "
                       "si užijete nádherné podrobnosti a živé barvy ve vysokém rozlišení. Přesné a ostré obrazy "
                       "vás přenáší do světa, kde se každý detail zobrazuje s ohromující jasností. Procesor"
                       " Intel Core i7 a 4 jádra vám poskytují dostatečnou sílu pro plynulý běh náročných"
                       " aplikací a multitasking. Spoléhejte na rychlé odezvy a plynulé přepínání mezi"
                       " různými úkoly bez zbytečných prodlev. Grafická karta AMD "
                       "Radeon Pro 5500M s 4 GB paměti vám umožňuje vytvářet a upravovat "
                       "grafiku a videa s precizností. "
                       "Prohlížejte si své projekty ve vysokém rozlišení a sledujte, jak se vám tvorba stává živou"
                       "vyroben z odolného hliníku, který zajišťuje dlouhodobou spolehlivost a "
                       "odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení "
                       "notebooku a využití při práci"
                       " nebo na cestách. S Macbook Pro získáte výkonný a spolehlivý notebook, který vám "
                       "umožní realizovat"
                       " vaše profesionální ambice a těšit se z kvalitního multimediálního zážitku.",
        "subheading": "Prožijte prvotřídní výkon a úžasné vizuální efekty s Macbook Pro.",
        "visit_count": 14560,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 144,
        "display_nits": 1600,
        "display_type": "Retina",
        "processor": "Intel Core i7",
        "processor_cores": 4,
        "graphics_card": "AMD Radeon Pro 5500M",
        "graphics_memory": 4,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 3.02,
        "weight_units": "kg",
        "color": "šedá",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },

    {
        "product_name": "Macbook Pro M1 512GB/8GB Šedý",
        "price": 43758,
        "discount": 0,
        "stock": 15,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 8,
        "description": "Macbook Pro s čipem M1 je výkonný a univerzální notebook navržený pro profesionály a náročné "
                       "uživatele. S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že"
                       " zvládnete jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Retina "
                       "displej nabízí nádherné detaily a živé barvy ve vysokém rozlišení, ponoří vás do světa, "
                       "kde se každý detail zobrazuje s ohromující jasností. Čip M1, první čip od Applu "
                       "navržený speciálně pro Mac, poskytuje výjimečnou energetickou efektivitu a výkon,"
                       " umožňuje plynulý multitasking a bezproblémové provádění náročných úkolů. Integrovaná 8-jádrová GPU"
                       " zajišťuje rychlé zpracování grafiky, umožňuje vám tvořit a upravovat grafiku a videa s"
                       " precizností. Sledujte své projekty ve vysokém rozlišení a sledujte, jak se vaše tvorba stává "
                       "živou. S kapacitou 512 GB SSD poskytuje Macbook Pro rychlé načítání systému a aplikací, "
                       "a to vše s dostatečným úložným prostorem pro vaše soubory a dokumenty. Zažijte rychlý a "
                       "efektivní přístup k vašim datům. Macbook Pro je vyroben z odolného hliníku, což zajišťuje "
                       "dlouhodobou spolehlivost a odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení"
                       "notebooku a využití při práci nebo na cestách. S Macbook Pro M1 získáte výkonný a spolehlivý "
                       "notebook, který vám umožní naplnit vaše profesionální ambice a těšit se z kvalitního "
                       "multimediálního zážitku.",
        "subheading": "Zažijte špičkový výkon a ohromující obraz s Macbookem Pro M1.",
        "visit_count": 12540,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 60,
        "display_nits": 500,
        "display_type": "Retina",
        "processor": "Apple M1",
        "processor_cores": 8,
        "graphics_card": "Apple M1",
        "graphics_memory": 8,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 1.4,
        "weight_units": "kg",
        "color": "šedá",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },

    {
        "product_name": "Macbook Pro M1 512GB/16GB Šedý",
        "price": 47623,
        "discount": 0,
        "stock": 15,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 16,
        "description": "Macbook Pro s čipem M1 je výkonný a univerzální notebook navržený pro profesionály a náročné "
                       "uživatele. S jeho špičkovým výkonem a ohromujícím vizuálním zážitkem si můžete být jistí, že"
                       " zvládnete jakýkoli úkol a projdete se plynule nejnovějšími aplikacemi a programy. Retina "
                       "displej nabízí nádherné detaily a živé barvy ve vysokém rozlišení, ponoří vás do světa, "
                       "kde se každý detail zobrazuje s ohromující jasností. Čip M1, první čip od Applu "
                       "navržený speciálně pro Mac, poskytuje výjimečnou energetickou efektivitu a výkon,"
                       " umožňuje plynulý multitasking a bezproblémové provádění náročných úkolů. Integrovaná 8-jádrová GPU"
                       " zajišťuje rychlé zpracování grafiky, umožňuje vám tvořit a upravovat grafiku a videa s"
                       " precizností. Sledujte své projekty ve vysokém rozlišení a sledujte, jak se vaše tvorba stává "
                       "živou. S kapacitou 512 GB SSD poskytuje Macbook Pro rychlé načítání systému a aplikací, "
                       "a to vše s dostatečným úložným prostorem pro vaše soubory a dokumenty. Zažijte rychlý a "
                       "efektivní přístup k vašim datům. Macbook Pro je vyroben z odolného hliníku, což zajišťuje "
                       "dlouhodobou spolehlivost a odolnost. Jeho kompaktní a lehký design vám umožňuje snadné přenášení"
                       "notebooku a využití při práci nebo na cestách. S Macbook Pro M1 získáte výkonný a spolehlivý "
                       "notebook, který vám umožní naplnit vaše profesionální ambice a těšit se z kvalitního "
                       "multimediálního zážitku.",
        "subheading": "Zažijte špičkový výkon a ohromující obraz s Macbookem Pro M1.",
        "visit_count": 12540,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 60,
        "display_nits": 500,
        "display_type": "Retina",
        "processor": "Apple M1",
        "processor_cores": 8,
        "graphics_card": "Apple M1",
        "graphics_memory": 8,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 58,
        "construction": "celokovový",
        "height": 0.61,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 1.4,
        "weight_units": "kg",
        "color": "šedá",
        "usb_ports": 4,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },
    {
        "product_name": "Macbook Air M1 512GB/16GB Šedý",
        "price": 32999,
        "discount": 0,
        "stock": 10,
        "display_size": 13.3,
        "display_resolution": "2560 x 1600",
        "operating_system": "macOS",
        "operating_memory": 16,
        "description": "Macbook Air s čipem M1 je výkonný a přenosný notebook navržený pro každodenní použití a mobilitu. "
                       "Díky svému špičkovému výkonu a ohromujícímu zobrazení budete mít jistotu, že zvládnete každý úkol "
                       "a budete mít plynulý přístup k nejnovějším aplikacím a programům. Retina displej nabízí vysoké "
                       "rozlišení a živé barvy, které vás pohltí a umožní vám vnímat každý detail s úchvatnou jasností. "
                       "Čip M1, první čip navržený speciálně pro Mac od společnosti Apple, poskytuje vynikající energetickou "
                       "účinnost a výkon, což umožňuje plynulé multitasking a snadné zvládnutí náročných úkolů. Díky integrované "
                       "7-jádrové GPU můžete rychle zpracovávat grafiku a tvořit a upravovat grafiku a videa s vysokou přesností. "
                       "Prohlížejte si své projekty vysokým rozlišením a sledujte, jak ožívají vaše vize. S kapacitou 512 GB SSD "
                       "poskytuje Macbook Air rychlé načítání systému a aplikací a dostatek úložného prostoru pro vaše soubory a "
                       "dokumenty. Zažijte rychlý a efektivní přístup ke svým datům. Macbook Air je vyroben z odolného hliníkového "
                       "těla, které zajišťuje dlouhodobou spolehlivost a odolnost. Jeho tenký a lehký design vám umožní snadné "
                       "přenášení a používání notebooku všude, kde jste. S Macbookem Air M1 získáte výkonný a spolehlivý notebook, "
                       "který vám umožní naplnit vaše každodenní potřeby a vychutnat si vysokou kvalitu multimediálního zážitku.",
        "subheading": "Zažijte výkonnost a pohodlí s Macbookem Air M1.",
        "visit_count": 9823,
        "product_type": "Notebook",
        "brand_id": 1,
        "category_id": 4,
        "display_frequency": 60,
        "display_nits": 400,
        "display_type": "Retina",
        "processor": "Apple M1",
        "processor_cores": 8,
        "graphics_card": "Apple M1",
        "graphics_memory": 7,
        "ssd_capacity": 512,
        "hdd_capacity": 0,
        "ssd": True,
        "hdd": False,
        "light_keyboard": True,
        "num_keyboard": False,
        "touch_screen": False,
        "fingerprint_reader": False,
        "memory_card_reader": False,
        "usb_c_charging": True,
        "battery_capacity": 49.9,
        "construction": "celokovový",
        "height": 0.41,
        "height_units": "mm",
        "width": 11.97,
        "width_units": "mm",
        "depth": 8.36,
        "depth_units": "mm",
        "weight": 1.29,
        "weight_units": "kg",
        "color": "šedá",
        "usb_ports": 2,
        "hdmi_ports": 1,
        "audio_jack": True,
        "usb_3_0": True,
        "usb_2_0": False,
        "cd_dvd_drive": False,
        "product_image": "test_image_mac_book_pro.jpeg"
    },

 {
    "product_name": "MSI Katana 15 B12VFK-1016XCZ",
    "price": 29990,
    "discount": 0,
    "stock": 5,
    "display_size": 15.6,
    "display_resolution": "1920 x 1080",
    "operating_system": "Windows 10",
    "operating_memory": 16,
    "description": "Notebook MSI Katana 15 B12VFK-1016XCZ je výkonný a mobilní notebook navržený pro herní a pracovní "
    "účely. Díky svému vysokému výkonu a ergonomickému designu vám poskytuje přesně to, co potřebujete "
    "pro hraní her a práci na cestách. Displej s úhlopříčkou 15,6 palce a rozlišením 1920 x 1080 pixelů "
    "nabízí ostrý a detailní obraz, který vám umožní plně se ponořit do hraní her a sledování videí. "
    "S operační pamětí o velikosti 16 GB budete mít dostatek prostoru pro plynulý běh náročných aplikací "
    "a her. Notebook je vybaven procesorem Intel Core i7, který poskytuje vysoký výkon a rychlost pro "
    "náročné úlohy. S grafickou kartou NVIDIA GeForce RTX 3060 si můžete užít plynulé a detailní zobrazení "
    "grafiky ve hrách a při práci s grafickými programy. S SSD kapacitou 512 GB získáte dostatek prostoru pro "
    "ukládání her, aplikací a souborů. Notebook je vybaven praktickými rozhraními, včetně USB portů pro připojení "
    "externích zařízení, HDMI portu pro připojení externího monitoru a audio jacku pro připojení sluchátek. "
    "Váha notebooku je 2,3 kg, což zajišťuje snadnou přenosnost a použití na cestách. S notebookem MSI Katana "
    "15 B12VFK-1016XCZ získáte výkonný a kompaktní notebook, který splní vaše potřeby při hraní her i práci.",
    "subheading": "Výkonný a mobilní notebook pro herní a pracovní účely.",
    "visit_count": 5821,
    "product_type": "Notebook",
    "brand_id": 8,
    "category_id": 4,
    "display_frequency": 144,
    "display_nits": 300,
    "display_type": "IPS",
    "processor": "Intel Core i7",
    "processor_cores": 6,
    "graphics_card": "NVIDIA GeForce RTX 3060",
    "graphics_memory": 6,
    "ssd_capacity": 512,
    "hdd_capacity": 0,
    "ssd": True,
    "hdd": False,
    "light_keyboard": True,
    "num_keyboard": False,
    "touch_screen": False,
    "fingerprint_reader": False,
    "memory_card_reader": False,
    "usb_c_charging": True,
    "battery_capacity": 65,
    "construction": "celokovový",
    "height": 2.29,
    "height_units": "cm",
    "width": 35.9,
    "width_units": "cm",
    "depth": 24.8,
    "depth_units": "cm",
    "weight": 2.3,
    "weight_units": "kg",
    "color": "černá",
    "usb_ports": 4,
    "hdmi_ports": 1,
    "audio_jack": True,
    "usb_3_0": True,
    "usb_2_0": False,
    "cd_dvd_drive": False,
    "product_image": "test_image_msi_katana.jpeg"
    },

 {
    "product_name": "MSI Alpha 17 B5EEK-029CZ",
    "price": 25990,
    "discount": 0,
    "stock": 8,
    "display_size": 17.3,
    "display_resolution": "1920 x 1080",
    "operating_system": "Windows 10 Home",
    "operating_memory": 16,
    "description": "MSI Alpha 17 B5EEK-029CZ je výkonný herní notebook s 17.3-palcovým displejem a "
                   "vysokým rozlišením 1920 x 1080. Je vybaven procesorem AMD Ryzen 7 a 16 GB operační paměti, "
                   "které poskytují dostatečný výkon pro hraní "
                   "náročných her a provádění multitaskingu. Notebook disponuje 512 GB SSD pro rychlé načítání systému "
                   "a aplikací a také pro dostatečný úložný prostor pro vaše soubory a hry. "
                   "Grafická karta NVIDIA GeForce "
                   "RTX 3060 s 6 GB paměti zajišťuje plynulé a detailní zobrazení grafiky ve hrách. "
                   "MSI Alpha 17 B5EEK-029CZ "
                   "je vyroben z kvalitních materiálů, které zajišťují odolnost a dlouhodobou spolehlivost. "
                   "Jeho stylový design "
                   "a RGB podsvícení klávesnice přispívají k atraktivnímu vzhledu. Notebook je vybaven "
                   "různými porty, včetně "
                   "USB, HDMI a audio konektorů, pro snadné připojení periferních zařízení. S MSI Alpha 17 "
                   "B5EEK-029CZ získáte "
                   "výkonný herní notebook, který vám umožní vychutnat si hraní her a provádění náročných úkolů.",
    "subheading": "Vychutnejte si hraní her s MSI Alpha 17 B5EEK-029CZ",
    "visit_count": 18392,
    "product_type": "Notebook",
    "brand_id": 8,
    "category_id": 4,
    "display_frequency": 144,
    "display_nits": 300,
    "display_type": "IPS",
    "processor": "AMD Ryzen 7",
    "processor_cores": 8,
    "graphics_card": "NVIDIA GeForce RTX 3060",
    "graphics_memory": 6,
    "ssd_capacity": 512,
    "hdd_capacity": 0,
    "ssd": True,
    "hdd": False,
    "light_keyboard": True,
    "num_keyboard": False,
    "touch_screen": False,
    "fingerprint_reader": False,
    "memory_card_reader": False,
    "usb_c_charging": True,
    "battery_capacity": 51,
    "construction": "plastový",
    "height": 2.66,
    "height_units": "cm",
    "width": 39.7,
    "width_units": "cm",
    "depth": 27,
    "depth_units": "cm",
    "weight": 2.6,
    "weight_units": "kg",
    "color": "černá",
    "usb_ports": 4,
    "hdmi_ports": 1,
    "audio_jack": True,
    "usb_3_0": True,
    "usb_2_0": True,
    "cd_dvd_drive": False,
    "product_image": "test_image_msi_katana.jpeg"
 },

    {
    "product_name": "MSI Crosshair 15 B12UGZ-072CZ",
    "price": 31990,
    "discount": 0,
    "stock": 10,
    "display_size": 15.6,
    "display_resolution": "1920 x 1080",
    "operating_system": "Windows 10 Home",
    "operating_memory": 16,
    "description": "MSI Crosshair 15 B12UGZ-072CZ je výkonný herní notebook s 15.6-palcovým displejem a vysokým rozlišením 1920 x 1080. "
    "Je vybaven procesorem Intel Core i7 a 16 GB operační paměti, které poskytují dostatečný výkon pro hraní náročných her "
    "a provádění multitaskingu. Notebook disponuje 512 GB SSD pro rychlé načítání systému a aplikací a také pro dostatečný "
    "úložný prostor pro vaše soubory a hry. Grafická karta NVIDIA GeForce RTX 3060 s 6 GB paměti zajišťuje plynulé a detailní "
    "zobrazení grafiky ve hrách. MSI Crosshair 15 B12UGZ-072CZ je vyroben z kvalitních materiálů, které zajišťují odolnost "
    "a dlouhodobou spolehlivost. Jeho stylový design a RGB podsvícení klávesnice přispívají k atraktivnímu vzhledu. "
    "Notebook je vybaven různými porty, včetně USB, HDMI a audio konektorů, pro snadné připojení periferních zařízení. "
    "S MSI Crosshair 15 B12UGZ-072CZ získáte výkonný herní notebook, který vám umožní vychutnat si hraní her a provádění "
    "náročných úkolů.",
    "subheading": "Vychutnejte si hraní her s MSI Crosshair 15 B12UGZ-072CZ",
    "visit_count": 12450,
    "product_type": "Notebook",
    "brand_id": 8,
    "category_id": 4,
    "display_frequency": 144,
    "display_nits": 300,
    "display_type": "IPS",
    "processor": "Intel Core i7",
    "processor_cores": 8,
    "graphics_card": "NVIDIA GeForce RTX 3060",
    "graphics_memory": 6,
    "ssd_capacity": 512,
    "hdd_capacity": 0,
    "ssd": True,
    "hdd": False,
    "light_keyboard": True,
    "num_keyboard": False,
    "touch_screen": False,
    "fingerprint_reader": False,
    "memory_card_reader": False,
    "usb_c_charging": True,
    "battery_capacity": 51,
    "construction": "plastový",
    "height": 2.39,
    "height_units": "cm",
    "width": 35.72,
    "width_units": "cm",
    "depth": 24.76,
    "depth_units": "cm",
    "weight": 1.9,
    "weight_units": "kg",
    "color": "černá",
    "usb_ports": 4,
    "hdmi_ports": 1,
    "audio_jack": True,
    "usb_3_0": True,
    "usb_2_0": True,
    "cd_dvd_drive": False,
    "product_image": "test_image_msi_katana.jpeg"
    }
]


with open('notebook_products.csv', 'w', newline='') as file:
    # create a writer object
    writer = csv.writer(file)

    # write the header row
    writer.writerow(products[0].keys())

    # write the data rows
    for product in products:
        writer.writerow(product.values())
