import csv

products = [
    {
        "product_name": "iPhone 13 Pro Max 1T černá",
        "price": 47390,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 1024,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "černá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 512 GB černá",
        "price": 41190,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "černá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 256 GB černá",
        "price": 35590,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "černá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 128 GB černá",
        "price": 29991,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "černá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

{
    "product_name": "iPhone 13 Pro 512 GB černá",
    "price": 35299,
    "discount": 0,
    "stock": 25,
    "display_size": 6.1,
    "display_resolution": "2532 x 1170",
    "operating_system": "iOS",
    "operating_memory": 6,
    "memory": 512,
    "height": 146.7,
    "height_units": "mm",
    "width": 71.5,
    "width_units": "mm",
    "depth": 7.65,
    "depth_units": "mm",
    "weight": 204,
    "weight_units": "g",
    "battery_capacity": 3095,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 12,
    "back_camera": 12,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Apple A15 Bionic",
    "processor_cores": 6,
    "esim": True,
    "color": "černá",
    "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
    "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                   "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                   " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                   "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                   "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                   "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                   " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                   "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
    "brand_id": 1,
    "category_id": 1,
    "visit_count": 900,
    "product_image": "test_image_iphone_13_pro_1.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "iPhone 13 Pro 256 GB černá",
    "price": 31299,
    "discount": 0,
    "stock": 25,
    "display_size": 6.1,
    "display_resolution": "2532 x 1170",
    "operating_system": "iOS",
    "operating_memory": 6,
    "memory": 256,
    "height": 146.7,
    "height_units": "mm",
    "width": 71.5,
    "width_units": "mm",
    "depth": 7.65,
    "depth_units": "mm",
    "weight": 204,
    "weight_units": "g",
    "battery_capacity": 3095,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 12,
    "back_camera": 12,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Apple A15 Bionic",
    "processor_cores": 6,
    "esim": True,
    "color": "černá",
    "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
    "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                   "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                   " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                   "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                   "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                   "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                   " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                   "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
    "brand_id": 1,
    "category_id": 1,
    "visit_count": 900,
    "product_image": "test_image_iphone_13_pro_1.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "iPhone 13 Pro 128 GB černá",
    "price": 28389,
    "discount": 0,
    "stock": 25,
    "display_size": 6.1,
    "display_resolution": "2532 x 1170",
    "operating_system": "iOS",
    "operating_memory": 6,
    "memory": 128,
    "height": 146.7,
    "height_units": "mm",
    "width": 71.5,
    "width_units": "mm",
    "depth": 7.65,
    "depth_units": "mm",
    "weight": 204,
    "weight_units": "g",
    "battery_capacity": 3095,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 12,
    "back_camera": 12,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Apple A15 Bionic",
    "processor_cores": 6,
    "esim": True,
    "color": "černá",
    "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
    "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                   "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                   " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                   "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                   "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                   "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                   " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                   "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
    "brand_id": 1,
    "category_id": 1,
    "visit_count": 900,
    "product_image": "test_image_iphone_13_pro_1.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "iPhone 13 512 GB černá",
    "price": 26490,
    "discount": 0,
    "stock": 15,
    "display_size": 6.1,
    "display_resolution": "2532 x 1170",
    "operating_system": "iOS",
    "operating_memory": 6,
    "memory": 512,
    "height": 146.7,
    "height_units": "mm",
    "width": 71.5,
    "width_units": "mm",
    "depth": 7.65,
    "depth_units": "mm",
    "weight": 173,
    "weight_units": "g",
    "battery_capacity": 2942,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 12,
    "back_camera": 12,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Apple A15 Bionic",
    "processor_cores": 6,
    "esim": True,
    "color": "černá",
    "subheading": "Kompaktní, výkonný a stylový iPhone 13",
    "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                   " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                   "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                   "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                   "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                   "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                   "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                   "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                   "takže vás nenechá na holičkách ani v náročných podmínkách.",
    "brand_id": 1,
    "category_id": 1,
    "visit_count": 899,
    "product_image": "test_image_iphone_13_1.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "iPhone 13 256 GB černá",
    "price": 21490,
    "discount": 0,
    "stock": 15,
    "display_size": 6.1,
    "display_resolution": "2532 x 1170",
    "operating_system": "iOS",
    "operating_memory": 6,
    "memory": 256,
    "height": 146.7,
    "height_units": "mm",
    "width": 71.5,
    "width_units": "mm",
    "depth": 7.65,
    "depth_units": "mm",
    "weight": 173,
    "weight_units": "g",
    "battery_capacity": 2942,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 12,
    "back_camera": 12,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Apple A15 Bionic",
    "processor_cores": 6,
    "esim": True,
    "color": "černá",
    "subheading": "Kompaktní, výkonný a stylový iPhone 13",
    "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                   " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                   "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                   "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                   "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                   "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                   "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                   "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                   "takže vás nenechá na holičkách ani v náročných podmínkách.",
    "brand_id": 1,
    "category_id": 1,
    "visit_count": 899,
    "product_image": "test_image_iphone_13_1.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "iPhone 13 128 GB černá",
    "price": 21490,
    "discount": 0,
    "stock": 15,
    "display_size": 6.1,
    "display_resolution": "2532 x 1170",
    "operating_system": "iOS",
    "operating_memory": 6,
    "memory": 128,
    "height": 146.7,
    "height_units": "mm",
    "width": 71.5,
    "width_units": "mm",
    "depth": 7.65,
    "depth_units": "mm",
    "weight": 173,
    "weight_units": "g",
    "battery_capacity": 2942,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 12,
    "back_camera": 12,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Apple A15 Bionic",
    "processor_cores": 6,
    "esim": True,
    "color": "černá",
    "subheading": "Kompaktní, výkonný a stylový iPhone 13",
    "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                   " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                   "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                   "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                   "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                   "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                   "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                   "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                   "takže vás nenechá na holičkách ani v náročných podmínkách.",
    "brand_id": 1,
    "category_id": 1,
    "visit_count": 899,
    "product_image": "test_image_iphone_13_1.jpeg",
    'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 1T modrá",
        "price": 47390,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 1024,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 512 GB modrá",
        "price": 41190,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 256 GB modrá",
        "price": 35590,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 128 GB modrá",
        "price": 29991,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro 512 GB modrá",
        "price": 35299,
        "discount": 0,
        "stock": 25,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 204,
        "weight_units": "g",
        "battery_capacity": 3095,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
        "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 900,
        "product_image": "test_image_iphone_13_pro_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro 256 GB modrá",
        "price": 31299,
        "discount": 0,
        "stock": 25,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 204,
        "weight_units": "g",
        "battery_capacity": 3095,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
        "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 900,
        "product_image": "test_image_iphone_13_pro_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro 128 GB modrá",
        "price": 28389,
        "discount": 0,
        "stock": 25,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 204,
        "weight_units": "g",
        "battery_capacity": 3095,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
        "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 900,
        "product_image": "test_image_iphone_13_pro_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 512 GB modrá",
        "price": 26490,
        "discount": 0,
        "stock": 15,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 173,
        "weight_units": "g",
        "battery_capacity": 2942,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Kompaktní, výkonný a stylový iPhone 13",
        "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                       " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                       "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                       "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                       "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                       "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                       "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                       "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                       "takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 899,
        "product_image": "test_image_iphone_13_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 256 GB modrá",
        "price": 21490,
        "discount": 0,
        "stock": 15,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 173,
        "weight_units": "g",
        "battery_capacity": 2942,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Kompaktní, výkonný a stylový iPhone 13",
        "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                       " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                       "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                       "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                       "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                       "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                       "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                       "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                       "takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 899,
        "product_image": "test_image_iphone_13_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 128 GB modrá",
        "price": 21490,
        "discount": 0,
        "stock": 15,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 173,
        "weight_units": "g",
        "battery_capacity": 2942,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "modrá",
        "subheading": "Kompaktní, výkonný a stylový iPhone 13",
        "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                       " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                       "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                       "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                       "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                       "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                       "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                       "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                       "takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 899,
        "product_image": "test_image_iphone_13_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 1T zelená",
        "price": 47390,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 1024,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 512 GB zelená",
        "price": 41190,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 256 GB zelená",
        "price": 35590,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro Max 128 GB zelená",
        "price": 29991,
        "discount": 0,
        "stock": 20,
        "display_size": 6.7,
        "display_resolution": "2778 x 1284",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 160.8,
        "height_units": "mm",
        "width": 78.1,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 238,
        "weight_units": "g",
        "battery_capacity": 4352,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro Max",
        "description": "iPhone 13 Pro Max je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má velký 6,7palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 28 hodin hovoru nebo až 95 hodin poslechu hudby. Nový iPhone 13 Pro Max je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 1358,
        "product_image": "test_image_iphone_13_pro_max_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro 512 GB zelená",
        "price": 35299,
        "discount": 0,
        "stock": 25,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 204,
        "weight_units": "g",
        "battery_capacity": 3095,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
        "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 900,
        "product_image": "test_image_iphone_13_pro_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro 256 GB zelená",
        "price": 31299,
        "discount": 0,
        "stock": 25,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 204,
        "weight_units": "g",
        "battery_capacity": 3095,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
        "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 900,
        "product_image": "test_image_iphone_13_pro_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 Pro 128 GB zelená",
        "price": 28389,
        "discount": 0,
        "stock": 25,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 204,
        "weight_units": "g",
        "battery_capacity": 3095,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Výkonný, kvalitní a spolehlivý iPhone 13 Pro",
        "description": "iPhone 13 Pro je špičkový mobilní telefon nabízející nejvyšší výkon a kvalitu "
                       "bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, které zajistí hladký chod"
                       " a neuvěřitelnou zábavu. Telefon má 6,1palcový displej Super Retina XDR s technologií "
                       "ProMotion, který zobrazuje výrazné a detailní barvy. S pokročilým systémem fotoaparátů můžete "
                       "zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým "
                       "osvětlením. Telefon obsahuje nejnovější procesor A15 Bionic a výkonnou baterii, která umožní"
                       " až 22 hodin hovoru nebo až 75 hodin poslechu hudby. Nový iPhone 13 Pro je také odolný "
                       "vůči vodě a prachu, takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 900,
        "product_image": "test_image_iphone_13_pro_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 512 GB zelená",
        "price": 26490,
        "discount": 0,
        "stock": 15,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 512,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 173,
        "weight_units": "g",
        "battery_capacity": 2942,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Kompaktní, výkonný a stylový iPhone 13",
        "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                       " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                       "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                       "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                       "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                       "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                       "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                       "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                       "takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 899,
        "product_image": "test_image_iphone_13_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 256 GB zelená",
        "price": 21490,
        "discount": 0,
        "stock": 15,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 256,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 173,
        "weight_units": "g",
        "battery_capacity": 2942,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Kompaktní, výkonný a stylový iPhone 13",
        "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                       " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                       "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                       "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                       "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                       "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                       "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                       "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                       "takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 899,
        "product_image": "test_image_iphone_13_1.jpeg",
        'product_type': "Mobile",
    },

    {
        "product_name": "iPhone 13 128 GB zelená",
        "price": 21490,
        "discount": 0,
        "stock": 15,
        "display_size": 6.1,
        "display_resolution": "2532 x 1170",
        "operating_system": "iOS",
        "operating_memory": 6,
        "memory": 128,
        "height": 146.7,
        "height_units": "mm",
        "width": 71.5,
        "width_units": "mm",
        "depth": 7.65,
        "depth_units": "mm",
        "weight": 173,
        "weight_units": "g",
        "battery_capacity": 2942,
        "memory_card_slot": False,
        "face_id": True,
        "touch_screen": True,
        "front_camera": 12,
        "back_camera": 12,
        "convertible": False,
        "wifi": True,
        "bluetooth": True,
        "nfc": True,
        "processor": "Apple A15 Bionic",
        "processor_cores": 6,
        "esim": True,
        "color": "zelená",
        "subheading": "Kompaktní, výkonný a stylový iPhone 13",
        "description": "iPhone 13 je jedním z nejnovějších mobilních telefonů od společnosti Apple. Disponuje"
                       " kompaktním 6,1palcovým displejem Super Retina XDR, který zobrazuje krásné a detailní "
                       "obrázky. Telefon je vybaven výkonným procesorem A15 Bionic, který zajišťuje plynulý chod "
                       "a vysokou výkonnost. Telefon má velkou vnitřní paměť 128GB a operační paměť 6GB, takže "
                       "můžete ukládat své oblíbené aplikace, hry, fotografie a videa. S pokročilým systémem "
                       "fotoaparátů můžete zachytit skvělé fotografie a videa s vysokým rozlišením, a to i v "
                       "podmínkách s nízkým osvětlením. Telefon obsahuje také nejnovější verzi operačního systému "
                       "iOS, která nabízí mnoho užitečných funkcí. Nový iPhone 13 je také odolný vůči vodě a prachu, "
                       "takže vás nenechá na holičkách ani v náročných podmínkách.",
        "brand_id": 1,
        "category_id": 1,
        "visit_count": 899,
        "product_image": "test_image_iphone_13_1.jpeg",
        'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 512GB/12GB černá",
    "price": 41849,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 12,
    "memory": 512,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_black.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 256GB/12GB černá",
    "price": 35299,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 12,
    "memory": 256,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_black.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 512GB/8GB černá",
    "price": 26999,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 512,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_black.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 256GB/8GB černá",
    "price": 26999,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 256,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_black.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Flip3 5G 8GB/512GB černá",
    "price": 26999,
    "discount": 0,
    "stock": 50,
    "display_size": 6.7,
    "display_resolution": "2640 x 1080",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 512,
    "height": 166.0,
    "height_units": "mm",
    "width": 72.2,
    "width_units": "mm",
    "depth": 6.9,
    "depth_units": "mm",
    "weight": 183,
    "weight_units": "g",
    "battery_capacity": 3300,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Elegantní skládací telefon s inovativním designem",
    "description": "Samsung Galaxy Z Flip3 5G je elegantní a inovativní skládací telefon, který "
    "si zamilují všichni, kteří chtějí být výjimeční. Skvěle se hodí pro všechny, "
    "kteří chtějí mít vždy nejmodernější technologie a stylový design. Skládací mechanismus "
    "telefonu je navržen tak, aby byl telefon snadno přenosný a zároveň poskytoval co největší"
    " zobrazovací plochu. S velkým 6,7palcovým displejem Full HD+ vám telefon nabídne "
    "výjimečně ostrý obraz a perfektní zážitek z přehrávání videí a her. Telefon je "
    "vybaven nejmodernějším procesorem Qualcomm Snapdragon 888, díky kterému bude vaše "
    "práce i zábava hladká a bez prodlev. Můžete se těšit také na výkonnou baterii, "
    "která vám umožní pracovat i hrát si po celý den. Dále nabídne telefon také "
    "velmi kvalitní fotoaparát s 12 MP, který vám umožní pořídit dokonalé fotografie. "
    "Vychutnejte si svět na plné koule s novým Samsung Galaxy Z Flip3 5G.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 740,
    "product_image": "test_image_samsung_galaxy_z_flip_balck.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Flip3 5G 8GB/256GB černá",
    "price": 24999,
    "discount": 0,
    "stock": 50,
    "display_size": 6.7,
    "display_resolution": "2640 x 1080",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 256,
    "height": 166.0,
    "height_units": "mm",
    "width": 72.2,
    "width_units": "mm",
    "depth": 6.9,
    "depth_units": "mm",
    "weight": 183,
    "weight_units": "g",
    "battery_capacity": 3300,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Elegantní skládací telefon s inovativním designem",
    "description": "Samsung Galaxy Z Flip3 5G je elegantní a inovativní skládací telefon, který "
    "si zamilují všichni, kteří chtějí být výjimeční. Skvěle se hodí pro všechny, "
    "kteří chtějí mít vždy nejmodernější technologie a stylový design. Skládací mechanismus "
    "telefonu je navržen tak, aby byl telefon snadno přenosný a zároveň poskytoval co největší"
    " zobrazovací plochu. S velkým 6,7palcovým displejem Full HD+ vám telefon nabídne "
    "výjimečně ostrý obraz a perfektní zážitek z přehrávání videí a her. Telefon je "
    "vybaven nejmodernějším procesorem Qualcomm Snapdragon 888, díky kterému bude vaše "
    "práce i zábava hladká a bez prodlev. Můžete se těšit také na výkonnou baterii, "
    "která vám umožní pracovat i hrát si po celý den. Dále nabídne telefon také "
    "velmi kvalitní fotoaparát s 12 MP, který vám umožní pořídit dokonalé fotografie. "
    "Vychutnejte si svět na plné koule s novým Samsung Galaxy Z Flip3 5G.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 740,
    "product_image": "test_image_samsung_galaxy_z_flip_balck.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Flip3 5G 8GB/128GB černá",
    "price": 21999,
    "discount": 0,
    "stock": 50,
    "display_size": 6.7,
    "display_resolution": "2640 x 1080",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 128,
    "height": 166.0,
    "height_units": "mm",
    "width": 72.2,
    "width_units": "mm",
    "depth": 6.9,
    "depth_units": "mm",
    "weight": 183,
    "weight_units": "g",
    "battery_capacity": 3300,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "černá",
    "subheading": "Elegantní skládací telefon s inovativním designem",
    "description": "Samsung Galaxy Z Flip3 5G je elegantní a inovativní skládací telefon, který "
    "si zamilují všichni, kteří chtějí být výjimeční. Skvěle se hodí pro všechny, "
    "kteří chtějí mít vždy nejmodernější technologie a stylový design. Skládací mechanismus "
    "telefonu je navržen tak, aby byl telefon snadno přenosný a zároveň poskytoval co největší"
    " zobrazovací plochu. S velkým 6,7palcovým displejem Full HD+ vám telefon nabídne "
    "výjimečně ostrý obraz a perfektní zážitek z přehrávání videí a her. Telefon je "
    "vybaven nejmodernějším procesorem Qualcomm Snapdragon 888, díky kterému bude vaše "
    "práce i zábava hladká a bez prodlev. Můžete se těšit také na výkonnou baterii, "
    "která vám umožní pracovat i hrát si po celý den. Dále nabídne telefon také "
    "velmi kvalitní fotoaparát s 12 MP, který vám umožní pořídit dokonalé fotografie. "
    "Vychutnejte si svět na plné koule s novým Samsung Galaxy Z Flip3 5G.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 740,
    "product_image": "test_image_samsung_galaxy_z_flip_balck.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 512GB/12GB fialová",
    "price": 41849,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 12,
    "memory": 512,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 256GB/12GB fialová",
    "price": 35299,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 12,
    "memory": 256,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 512GB/8GB fialová",
    "price": 26999,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 512,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Fold3 5G 256GB/8GB fialová",
    "price": 26999,
    "discount": 0,
    "stock": 15,
    "display_size": 7.6,
    "display_resolution": "2208 x 1768",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 256,
    "height": 158.2,
    "height_units": "mm",
    "width": 128.1,
    "width_units": "mm",
    "depth": 6.4,
    "depth_units": "mm",
    "weight": 271,
    "weight_units": "g",
    "battery_capacity": 4400,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Revolutionary foldable phone from Samsung",
    "description": "The Samsung Galaxy Z Fold3 5G is the latest and greatest foldable smartphone from Samsung. "
    "It features a 7.6 inch foldable Dynamic AMOLED display with a resolution of 2208 x 1768 pixels. "
    "The phone runs on Android and is powered by the Qualcomm Snapdragon 888 processor. It comes "
    "with 12GB of RAM and 512GB of internal storage. The phone has a triple camera setup on the "
    "back with a 12MP wide, 12MP ultrawide, and 12MP telephoto lens. On the front, there is a 10MP "
    "selfie camera. The Galaxy Z Fold3 5G is also 5G capable and has a 4400mAh battery. "
    "It is a truly innovative phone that redefines what is possible in terms of mobile technology.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 977,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Flip3 5G 8GB/512GB fialová",
    "price": 26999,
    "discount": 0,
    "stock": 50,
    "display_size": 6.7,
    "display_resolution": "2640 x 1080",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 512,
    "height": 166.0,
    "height_units": "mm",
    "width": 72.2,
    "width_units": "mm",
    "depth": 6.9,
    "depth_units": "mm",
    "weight": 183,
    "weight_units": "g",
    "battery_capacity": 3300,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Elegantní skládací telefon s inovativním designem",
    "description": "Samsung Galaxy Z Flip3 5G je elegantní a inovativní skládací telefon, který "
    "si zamilují všichni, kteří chtějí být výjimeční. Skvěle se hodí pro všechny, "
    "kteří chtějí mít vždy nejmodernější technologie a stylový design. Skládací mechanismus "
    "telefonu je navržen tak, aby byl telefon snadno přenosný a zároveň poskytoval co největší"
    " zobrazovací plochu. S velkým 6,7palcovým displejem Full HD+ vám telefon nabídne "
    "výjimečně ostrý obraz a perfektní zážitek z přehrávání videí a her. Telefon je "
    "vybaven nejmodernějším procesorem Qualcomm Snapdragon 888, díky kterému bude vaše "
    "práce i zábava hladká a bez prodlev. Můžete se těšit také na výkonnou baterii, "
    "která vám umožní pracovat i hrát si po celý den. Dále nabídne telefon také "
    "velmi kvalitní fotoaparát s 12 MP, který vám umožní pořídit dokonalé fotografie. "
    "Vychutnejte si svět na plné koule s novým Samsung Galaxy Z Flip3 5G.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 740,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Samsung Galaxy Z Flip3 5G 8GB/256GB fialová",
    "price": 24999,
    "discount": 0,
    "stock": 50,
    "display_size": 6.7,
    "display_resolution": "2640 x 1080",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 256,
    "height": 166.0,
    "height_units": "mm",
    "width": 72.2,
    "width_units": "mm",
    "depth": 6.9,
    "depth_units": "mm",
    "weight": 183,
    "weight_units": "g",
    "battery_capacity": 3300,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Elegantní skládací telefon s inovativním designem",
    "description": "Samsung Galaxy Z Flip3 5G je elegantní a inovativní skládací telefon, který "
    "si zamilují všichni, kteří chtějí být výjimeční. Skvěle se hodí pro všechny, "
    "kteří chtějí mít vždy nejmodernější technologie a stylový design. Skládací mechanismus "
    "telefonu je navržen tak, aby byl telefon snadno přenosný a zároveň poskytoval co největší"
    " zobrazovací plochu. S velkým 6,7palcovým displejem Full HD+ vám telefon nabídne "
    "výjimečně ostrý obraz a perfektní zážitek z přehrávání videí a her. Telefon je "
    "vybaven nejmodernějším procesorem Qualcomm Snapdragon 888, díky kterému bude vaše "
    "práce i zábava hladká a bez prodlev. Můžete se těšit také na výkonnou baterii, "
    "která vám umožní pracovat i hrát si po celý den. Dále nabídne telefon také "
    "velmi kvalitní fotoaparát s 12 MP, který vám umožní pořídit dokonalé fotografie. "
    "Vychutnejte si svět na plné koule s novým Samsung Galaxy Z Flip3 5G.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 740,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },


    {
    "product_name": "Samsung Galaxy Z Flip3 5G 8GB/128GB fialová",
    "price": 21999,
    "discount": 0,
    "stock": 50,
    "display_size": 6.7,
    "display_resolution": "2640 x 1080",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 128,
    "height": 166.0,
    "height_units": "mm",
    "width": 72.2,
    "width_units": "mm",
    "depth": 6.9,
    "depth_units": "mm",
    "weight": 183,
    "weight_units": "g",
    "battery_capacity": 3300,
    "memory_card_slot": False,
    "face_id": False,
    "touch_screen": True,
    "front_camera": 10,
    "back_camera": 12,
    "convertible": True,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 888",
    "processor_cores": 8,
    "esim": False,
    "color": "fialová",
    "subheading": "Elegantní skládací telefon s inovativním designem",
    "description": "Samsung Galaxy Z Flip3 5G je elegantní a inovativní skládací telefon, který "
    "si zamilují všichni, kteří chtějí být výjimeční. Skvěle se hodí pro všechny, "
    "kteří chtějí mít vždy nejmodernější technologie a stylový design. Skládací mechanismus "
    "telefonu je navržen tak, aby byl telefon snadno přenosný a zároveň poskytoval co největší"
    " zobrazovací plochu. S velkým 6,7palcovým displejem Full HD+ vám telefon nabídne "
    "výjimečně ostrý obraz a perfektní zážitek z přehrávání videí a her. Telefon je "
    "vybaven nejmodernějším procesorem Qualcomm Snapdragon 888, díky kterému bude vaše "
    "práce i zábava hladká a bez prodlev. Můžete se těšit také na výkonnou baterii, "
    "která vám umožní pracovat i hrát si po celý den. Dále nabídne telefon také "
    "velmi kvalitní fotoaparát s 12 MP, který vám umožní pořídit dokonalé fotografie. "
    "Vychutnejte si svět na plné koule s novým Samsung Galaxy Z Flip3 5G.",
    "brand_id": 2,
    "category_id": 1,
    "visit_count": 740,
    "product_image": "test_image_samsung_galaxy_z_flip_purple.jpg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Xiaomi Mi 13 256GB/8GB černá",
    "price": 19499,
    "discount": 0,
    "stock": 50,
    "display_size": 6.81,
    "display_resolution": "3200 x 1440",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 256,
    "height": 164.3,
    "height_units": "mm",
    "width": 74.6,
    "width_units": "mm",
    "depth": 7.8,
    "depth_units": "mm",
    "weight": 187,
    "weight_units": "g",
    "battery_capacity": 4800,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 20,
    "back_camera": 108,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 8",
    "processor_cores": 8,
    "esim": True,
    "color": "černá",
    "subheading": "Xiaomi Mi 13 s neuvěřitelným výkonem",
    "description": "Xiaomi Mi 13 přináší neuvěřitelný výkon, který zaručí skvělou zkušenost s chytrým telefonem. "
                    "Má velký 6,81palcový AMOLED displej s rozlišením 3200 x 1440, který poskytuje křišťálově"
                   " čisté vizuální zážitky. S poháněním od procesoru Qualcomm Snapdragon 8 Gen 1 a 8 GB operační "
                   "paměti můžete užívat rychlý a plynulý výkon s operačním systémem MIUI 13 "
                   "(založený na Androidu 13) předinstalovaným. Zachyťte úchvatné fotografie a videa s "
                   "trojitým fotoaparátem 108 MP a natočte nádherná selfie s předním fotoaparátem 20 MP. Telefon "
                   "má interní úložiště o velikosti 256 GB, které poskytuje dostatek místa pro ukládání všech "
                   "aplikací, fotografií a videí. S baterií o kapacitě 4800 mAh můžete být připojeni celý den "
                   "bez nutnosti nabíjení. Xiaomi Mi 13 má také podporu Wi-Fi, "
                    "Bluetooth, NFC a eSIM, což z něj dělá kompletní balíček chytrého telefonu.",
    "brand_id": 3,
    "category_id": 1,
    "visit_count": 587,
    "product_image": "test_image_xiaomi_13_black.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Xiaomi Mi 13 256GB/12GB černá",
    "price": 27499,
    "discount": 0,
    "stock": 50,
    "display_size": 6.81,
    "display_resolution": "3200 x 1440",
    "operating_system": "Android",
    "operating_memory": 12,
    "memory": 256,
    "height": 164.3,
    "height_units": "mm",
    "width": 74.6,
    "width_units": "mm",
    "depth": 7.8,
    "depth_units": "mm",
    "weight": 187,
    "weight_units": "g",
    "battery_capacity": 4800,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 20,
    "back_camera": 108,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 8",
    "processor_cores": 8,
    "esim": True,
    "color": "černá",
    "subheading": "Xiaomi Mi 13 s neuvěřitelným výkonem",
    "description": "Xiaomi Mi 13 přináší neuvěřitelný výkon, který zaručí skvělou zkušenost s chytrým telefonem. "
                    "Má velký 6,81palcový AMOLED displej s rozlišením 3200 x 1440, který poskytuje křišťálově"
                   " čisté vizuální zážitky. S poháněním od procesoru Qualcomm Snapdragon 8 Gen 1 a 8 GB operační "
                   "paměti můžete užívat rychlý a plynulý výkon s operačním systémem MIUI 13 "
                   "(založený na Androidu 13) předinstalovaným. Zachyťte úchvatné fotografie a videa s "
                   "trojitým fotoaparátem 108 MP a natočte nádherná selfie s předním fotoaparátem 20 MP. Telefon "
                   "má interní úložiště o velikosti 256 GB, které poskytuje dostatek místa pro ukládání všech "
                   "aplikací, fotografií a videí. S baterií o kapacitě 4800 mAh můžete být připojeni celý den "
                   "bez nutnosti nabíjení. Xiaomi Mi 13 má také podporu Wi-Fi, "
                    "Bluetooth, NFC a eSIM, což z něj dělá kompletní balíček chytrého telefonu.",
    "brand_id": 3,
    "category_id": 1,
    "visit_count": 587,
    "product_image": "test_image_xiaomi_13_black.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Xiaomi Mi 13 256GB/8GB zelená",
    "price": 19499,
    "discount": 0,
    "stock": 50,
    "display_size": 6.81,
    "display_resolution": "3200 x 1440",
    "operating_system": "Android",
    "operating_memory": 8,
    "memory": 256,
    "height": 164.3,
    "height_units": "mm",
    "width": 74.6,
    "width_units": "mm",
    "depth": 7.8,
    "depth_units": "mm",
    "weight": 187,
    "weight_units": "g",
    "battery_capacity": 4800,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 20,
    "back_camera": 108,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 8",
    "processor_cores": 8,
    "esim": True,
    "color": "zelená",
    "subheading": "Xiaomi Mi 13 s neuvěřitelným výkonem",
    "description": "Xiaomi Mi 13 přináší neuvěřitelný výkon, který zaručí skvělou zkušenost s chytrým telefonem. "
                    "Má velký 6,81palcový AMOLED displej s rozlišením 3200 x 1440, který poskytuje křišťálově"
                   " čisté vizuální zážitky. S poháněním od procesoru Qualcomm Snapdragon 8 Gen 1 a 8 GB operační "
                   "paměti můžete užívat rychlý a plynulý výkon s operačním systémem MIUI 13 "
                   "(založený na Androidu 13) předinstalovaným. Zachyťte úchvatné fotografie a videa s "
                   "trojitým fotoaparátem 108 MP a natočte nádherná selfie s předním fotoaparátem 20 MP. Telefon "
                   "má interní úložiště o velikosti 256 GB, které poskytuje dostatek místa pro ukládání všech "
                   "aplikací, fotografií a videí. S baterií o kapacitě 4800 mAh můžete být připojeni celý den "
                   "bez nutnosti nabíjení. Xiaomi Mi 13 má také podporu Wi-Fi, "
                    "Bluetooth, NFC a eSIM, což z něj dělá kompletní balíček chytrého telefonu.",
    "brand_id": 3,
    "category_id": 1,
    "visit_count": 587,
    "product_image": "test_image_xiaomi_13_green.jpeg",
    'product_type': "Mobile",
    },

    {
    "product_name": "Xiaomi Mi 13 256GB/12GB zelená",
    "price": 27499,
    "discount": 0,
    "stock": 50,
    "display_size": 6.81,
    "display_resolution": "3200 x 1440",
    "operating_system": "Android",
    "operating_memory": 12,
    "memory": 256,
    "height": 164.3,
    "height_units": "mm",
    "width": 74.6,
    "width_units": "mm",
    "depth": 7.8,
    "depth_units": "mm",
    "weight": 187,
    "weight_units": "g",
    "battery_capacity": 4800,
    "memory_card_slot": False,
    "face_id": True,
    "touch_screen": True,
    "front_camera": 20,
    "back_camera": 108,
    "convertible": False,
    "wifi": True,
    "bluetooth": True,
    "nfc": True,
    "processor": "Qualcomm Snapdragon 8",
    "processor_cores": 8,
    "esim": True,
    "color": "zelená",
    "subheading": "Xiaomi Mi 13 s neuvěřitelným výkonem",
    "description": "Xiaomi Mi 13 přináší neuvěřitelný výkon, který zaručí skvělou zkušenost s chytrým telefonem. "
                    "Má velký 6,81palcový AMOLED displej s rozlišením 3200 x 1440, který poskytuje křišťálově"
                   " čisté vizuální zážitky. S poháněním od procesoru Qualcomm Snapdragon 8 Gen 1 a 8 GB operační "
                   "paměti můžete užívat rychlý a plynulý výkon s operačním systémem MIUI 13 "
                   "(založený na Androidu 13) předinstalovaným. Zachyťte úchvatné fotografie a videa s "
                   "trojitým fotoaparátem 108 MP a natočte nádherná selfie s předním fotoaparátem 20 MP. Telefon "
                   "má interní úložiště o velikosti 256 GB, které poskytuje dostatek místa pro ukládání všech "
                   "aplikací, fotografií a videí. S baterií o kapacitě 4800 mAh můžete být připojeni celý den "
                   "bez nutnosti nabíjení. Xiaomi Mi 13 má také podporu Wi-Fi, "
                    "Bluetooth, NFC a eSIM, což z něj dělá kompletní balíček chytrého telefonu.",
    "brand_id": 3,
    "category_id": 1,
    "visit_count": 587,
    "product_image": "test_image_xiaomi_13_green.jpeg",
    'product_type': "Mobile",
    },

]

# open the file in 'w' mode (write mode)
with open('mobile_products.csv', 'w', newline='') as file:
    # create a writer object
    writer = csv.writer(file)

    # write the header row
    writer.writerow(products[0].keys())

    # write the data rows
    for product in products:
        writer.writerow(product.values())
