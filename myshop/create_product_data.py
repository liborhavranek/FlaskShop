import csv

products = [
    {'product_name': 'Iphone 13 Stříbrný',
     "price": 799,
     "discount": 5,
     "stock": 20,
     "size": 6.1,
     "size_units": "in",
     "weight": 174,
     "weight_units": "g",
     "color": "stříbrná",
     "subheading": "Nový iPhone 13 - Výkonný a stylový mobilní telefon",
     "description": "Popis produktu: Nový iPhone 13 přináší vysoký výkon a stylový design. Disponuje 6,1palcovým "
                    "Liquid Retina displejem s True Tone technologií a špičkovým fotoaparátem, který vám umožní "
                    "snímat neuvěřitelně detailní fotografie a videa. Procesor A15 Bionic zaručí hladký chod a "
                    "výkonná baterie vám umožní používat telefon až 19 hodin. iPhone 13 je také odolný vůči "
                    "vode a prachu a podporuje nejnovější verzi operačního systému iOS.",
     "brand_id": 1,
     "category_id": 1,
     "visit_count": 350,
     "product_image": "test_image_iphone_13_1.jpeg"
     },

    {'product_name': 'iPhone 13 Pro',
     'price': 899,
     'discount': 5,
     'stock': 100,
     'size': 6.1,
     'size_units': 'in',
     'weight': 204,
     'weight_units': 'g',
     'color': 'stříbrná',
     'subheading': 'Vylepšený iPhone 13 Pro - Profesionální výkon a funkce',
     'description': 'Popis produktu: iPhone 13 Pro je nejnovější vlajkovou lodí značky Apple. Tento mobilní telefon'
                    ' nabízí profesionální výkon a funkce, díky kterým můžete svůj život zlepšit. Telefon má velký'
                    ' 6,1palcový Super Retina XDR displej s ProMotion technologií, který zobrazuje '
                    'výrazné a detailní barvy. Díky pokročilému systému fotoaparátů s trojitým objektivem můžete'
                    ' snímat skvělé fotografie a videa s vysokým rozlišením, a to i v podmínkách s nízkým'
                    ' osvětlením. Nový procesor A15 Bionic zajišťuje hladký chod a neuvěřitelnou zábavu. '
                    'Telefon obsahuje také vysoce výkonnou baterii, která umožní až 22 hodin hovoru nebo až 75 '
                    'hodin poslechu hudby. Nový iPhone 13 Pro je navíc odolný vůči vodě a prachu, takže vás '
                    'nezklame ani v náročných podmínkách.',
     'brand_id': 1,
     'category_id': 1,
     "visit_count": 850,
     'product_image': 'test_image_iphone_13_pro_1.jpeg'},

    {'product_name': 'Iphone 13 pro Max',
     "price": 999,
     "discount": 5,
     "stock": 10,
     "size": 6.7,
     "size_units": "in",
     "weight": 238,
     "weight_units": "g",
     "color": "cerna",
     "subheading": "Nový iPhone 13 Pro Max - Výkon a kvalita bez kompromisů",
     "description": "Popis produktu: Nový iPhone 13 Pro Max je špičkou v oblasti mobilních telefonů, který nabízí"
                    " nejvyšší výkon a kvalitu bez kompromisů. Disponuje nejmodernějšími technologiemi a funkcemi, "
                    "které zajistí hladký chod a neuvěřitelnou zábavu. Telefon má velký 6,7palcový"
                    " Super Retina XDR displej s ProMotion technologií, který zobrazuje výrazné a detailní barvy."
                    " Díky pokročilému systému fotoaparátů můžete snímat skvělé fotografie a videa s vysokým"
                    " rozlišením, a to i v podmínkách s nízkým osvětlením. Telefon obsahuje nejnovější procesor"
                    " A15 Bionic a vysoce výkonnou baterii, která umožní až 28 hodin hovoru nebo až 95 hodin"
                    " poslechu hudby. Nový iPhone 13 Pro Max je navíc odolný vůči vodě a prachu, takže vás"
                    " nezklame ani v náročných podmínkách.",
     "brand_id": 1,
     "category_id": 1,
     "visit_count": 1358,
     "product_image": "test_image_iphone_13_pro_max_1.jpeg"
     },

    # add the rest of the products here...
]

# open the file in 'w' mode (write mode)
with open('products.csv', 'w', newline='') as file:
    # create a writer object
    writer = csv.writer(file)

    # write the header row
    writer.writerow(products[0].keys())

    # write the data rows
    for product in products:
        writer.writerow(product.values())
