import csv

products = [
 {
  "product_name": "Macbook Pro 512GB Stříbrný",
  "price": 2000,
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
