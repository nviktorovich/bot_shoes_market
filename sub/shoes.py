class Shoes:
	Brands = {'Adidas': ('Gazelle', 'Hamburg', 'EQT', 'ZX 8000', 'Yeezy 500'), 'Fila': ('Disruptor II', 'Sandals')}
	Models = ['Gazelle', 'Hamburg', 'EQT', 'ZX 8000', 'Yeezy 500', 'Disruptor II', 'Sandals']

	Colors = {
		'Gazelle':
			[('Pink White', 'price1', "https://sun9-58.userapi.com/c857132/v857132148/146369/3TqvJmG63r4.jpg"),
			 ('Blue White', 'price2', 'https://media.endclothing.com/media/catalog/product/0/7/07-08-2019_adidas_gazelle_blue_white_ee5511_ja_1.jpg'),
			 ('Sky Blue', 'price3', 'https://sun9-12.userapi.com/c856120/v856120148/212906/NAb5LelEzDk.jpg'),
			 ('White', 'price4', 'https://www.northernthreads.co.uk/images/adidas-originals-gazelle-white-gum-p35717-557923_image.jpg'),
			 ('Black White', 'price5', 'https://www.80scasualclassics.co.uk/images/adidas-gazelle-trainers-black-white-p5397-74103_zoom.jpg'),
			 ('Red White', 'price6', 'https://www.80scasualclassics.co.uk/images/adidas-gazelle-trainers-red-white-p5761-70715_image.jpg'),
			 ('Green', 'Price7', 'https://sun9-43.userapi.com/c855120/v855120148/21d5b3/UjsA9QkPjGo.jpg'),
			 ('Gray Black', 'Price8', 'https://sun9-17.userapi.com/c857332/v857332148/d89c7/7btWlNYAJRQ.jpg')
			 ],
		'Hamburg':
			[('Pink', 'price', 'https://sun9-33.userapi.com/c205620/v205620148/d6a32/ImHXIiKAMaE.jpg'),
			 ('Blue', 'price', 'https://sun9-3.userapi.com/c857336/v857336148/14bd27/yscbBgmSKTU.jpg'),
			 ('Classic', 'price', 'https://sun9-44.userapi.com/c857728/v857728148/1b64e4/av40_obDd7s.jpg'),
			 ('Triple Black', 'price', 'https://sun9-15.userapi.com/c850220/v850220462/1ee65/m2rpSjJtndU.jpg'),
			 ('Red', 'price', 'https://www.stuartslondon.com/images/hamburg-red-white-p31001-109442_zoom.jpg')
			 ],
		'EQT':
			[('Red Gray White', 'price', 'https://images.ua.prom.st/1215176577_w640_h640_adidas-eqt-cushion.jpg'),
			 ('Black White', 'price', 'https://stockx.imgix.net/adidas-EQT-Support-93-17-Black-White-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1543951666'),
			 ('Green Black White', 'price', 'https://stockx.imgix.net/Adidas-EQT-Support-ADV-Core-Black-Green-Vintage.jpg?fit=fill&bg=FFFFFF&w=700&h=500&auto=format,compress&q=90&dpr=2&trim=color&updated_at=1538080256')
			 ],
		'ZX 8000':
			[('Aqua', 'price', 'https://media.endclothing.com/media/f_auto,w_600,h_600/prodmedia/media/catalog/product/2/0/20-12-2019_adidas_zx8000og_aquayellow_eg8784_aj_1.jpg'),
			 ('Aqua Orange', 'price', 'https://sun9-32.userapi.com/impf/c206528/v206528224/b5f54/k90IfmSHZEU.jpg?size=639x0&quality=90&sign=dee0f9e5c6aabafa567ed87daa36f58b'),
			 ('Gray Green', 'price', 'https://www.atlanticsurvivalgear.ca/images/ca1/Adidas%20zx%208000%20schwarz%20grau%20gr%20n%20schuhe%20Online%20bestellen%201032.jpg')
			 ],
		'Yeezy 500':
			[('Gray', 'price', 'https://yeezyboost.store/image/cache/catalog/foto/yeezy-boost-folder/yeezy500/dh1iiafvmaai8vm-1000x1340.jpg'),
			 ('Beige', 'price', 'https://images.ua.prom.st/1261499077_w640_h2048_1256160480_w800_h640_1219__pid728608023_588aad1f.png?PIMAGE_ID=1261499077')
			 ],
		'Disruptor II':
			[('White', 'price', 'https://i.ebayimg.com/images/g/IZcAAOSwWk1ds7kI/s-l640.jpg'),
			 ('Black', 'price', 'https://imgs.inkfrog.com/pix/baybayshoes/Fila-Disruptor-Black-White-Red-1.jpg'),
			 ('Winter White', 'price', 'https://images.ua.prom.st/1391205418_w640_h640_fila-disruptor-ii.jpg'),
			 ('Winter Black', 'price', 'https://sneakers-kross.com.ua/content/images/41/fila-disruptor-ii-black-fur-winter-98163105654161_small11.jpg'),
			 ('White Premium', 'price', 'https://imgs.inkfrog.com/pix/baybayshoes/Womens-Fila-Disruptor-2-Premium-White-White-1.jpg'),
			 ('Black Premium', 'price', 'https://i.ebayimg.com/images/g/zfEAAOSwroJcdEUs/s-l300.jpg'),
			 ('White Pink', 'price', 'https://cross-city.ru/upload/iblock/5e5/fila-disruptor-ii-white-pink_p139_1.jpg'),
			 ('Black suede', 'price', 'https://images.ru.prom.st/728637820_w640_h640_muzhskie-krossovki-fila.jpg'),
			 ],
		'Sandals':
			[('White', 'price', 'https://sun9-27.userapi.com/impf/c206828/v206828916/ac313/LiRz5LVpUDU.jpg?size=0x640&quality=90&sign=005ce9701b9320ca3500d79a66738bf7'),
			 ('Black White', 'price', 'https://images.ua.prom.st/1197241433_w640_h640_fila-disruptor-sandals.jpg'),
			 ('Pink Black', 'price', 'https://sun9-60.userapi.com/impf/c857016/v857016583/1263e7/g02xBJtkZv8.jpg?size=0x800&quality=90&sign=b86f58bedbb94c3a924db49041e1a58f'),
			 ('White Red Blue', 'price', 'https://www.londonstore.it/img/8719477171992_P.jpg'),
			 ('Black Gold', 'price', 'https://scamper.com.ua/content/images/44/bosonizhki-fila-disruptor-sandals-black-gold-59434697306608_small11.jpg'),
			 ]
	}
