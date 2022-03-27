from aiogram import *
from aiogram.types import Message, CallbackQuery
from key import bot, dp
import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from button.buttons import *
from times.times import *

@dp.message_handler(commands='start')
async def welcom(message: types.Message):
	await message.reply(f'Assalomu alaykum <b>{message.from_user.first_name}</b>\nRamazon oyi muborak bo`lsin', reply_markup=await provinces(), parse_mode='html')


@dp.message_handler(text = '🔙 Orqaga')
async def back(message: types.Message):
	await message.reply('🔙 Orqaga qaytdingiz', reply_markup=main_btn)

@dp.message_handler(text = '🆘 Yordam markazi')
async def back(message: types.Message):
	await message.reply('Adminga murojaat qiling: @coder_admin', reply_markup=main_btn)

@dp.message_handler(text = '➡️ Boshqa bo`limlar')
async def back(message: types.Message):
	await message.reply("Hozircha bu bo'limlar yo'q", reply_markup=main_btn)

@dp.message_handler(text = '🕠 Ramazon taqvimi')
async def ramadan(message: types.Message):
	if datetime.datetime.today().month==4:
		await message.reply('Tanlang👇', reply_markup=ramazon_btn)

	else:
		await message.reply('Hozir Ramazon oyi emas', reply_markup=main_btn)


@dp.message_handler(text = '📿 Bugungi kun')
async def times(message: types.Message):
	img = Image.open('pic/img.png')
	id = message.from_user.id
	day = datetime.datetime.today().day
	print(id)
	send = await message.answer('⏳')        ##open(TEXT_PATH, 'rb')
	await send.delete()
	file = open(f"txts/{id}.txt", "r+")
	region = file.read()
	if len(region) < 3:
		await message.reply('viloyatingizni tanlang', reply_markup=await provinces())
	if region == 'Toshkent':
		bomdod = Toshkent_sax[day]
		shom = Toshkent_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Andijon':
		bomdod = Andijon_sax[day]
		shom = Andijon_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Buxoro':
		bomdod = Buxoro_sax[day]
		shom = Buxoro_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Guliston':
		bomdod = Guliston_sax[day]
		shom = Guliston_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Samarqand':
		bomdod = Samarqand_sax[day]
		shom = Samarqand_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Namangan':
		bomdod = Namangan_sax[day]
		shom = Namangan_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Navoiy':
		bomdod = Navoiy_sax[day]
		shom = Navoiy_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Jizzax':
		bomdod = Jizzax_sax[day]
		shom = Jizzax_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Nukus':
		bomdod = Nukus_sax[day]
		shom = Nukus_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Qarshi':
		bomdod = Qarshi_sax[day]
		shom = Qarshi_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Qoqon':
		bomdod = Qoqon_sax[day]
		shom = Qoqon_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Xiva':
		bomdod = Xiva_sax[day]
		shom = Xiva_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Margilon':
		bomdod = Margilon_sax[day]
		shom = Margilon_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')



@dp.message_handler(text = '📿 Ertangi kun')
async def times(message: types.Message):
	id = message.from_user.id
	day = 1+datetime.datetime.today().day
	send = await message.answer('⏳')        ##open(TEXT_PATH, 'rb')
	await send.delete()
	file = open(f"txts/{id}.txt", "r+")
	region = file.read()
	img = Image.open('pic/img.png')
	if len(region) < 3:
		await message.reply('viloyatingizni tanlang', reply_markup=await provinces())
	if region == 'Toshkent':
		bomdod = Toshkent_sax[day]
		shom = Toshkent_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Andijon':
		bomdod = Andijon_sax[day]
		shom = Andijon_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Buxoro':
		bomdod = Buxoro_sax[day]
		shom = Buxoro_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Guliston':
		bomdod = Guliston_sax[day]
		shom = Guliston_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Samarqand':
		bomdod = Samarqand_sax[day]
		shom = Samarqand_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Namangan':
		bomdod = Namangan_sax[day]
		shom = Namangan_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Navoiy':
		bomdod = Navoiy_sax[day]
		shom = Navoiy_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Jizzax':
		bomdod = Jizzax_sax[day]
		shom = Jizzax_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Nukus':
		bomdod = Nukus_sax[day]
		shom = Nukus_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day-1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti",font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi", reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Qarshi':
		bomdod = Qarshi_sax[day]
		shom = Qarshi_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Qoqon':
		bomdod = Qoqon_sax[day]
		shom = Qoqon_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Xiva':
		bomdod = Xiva_sax[day]
		shom = Xiva_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')
	elif region == 'Margilon':
		bomdod = Margilon_sax[day]
		shom = Margilon_ift[day]
		myFont = ImageFont.truetype('mono.ttf', 48)
		I1 = ImageDraw.Draw(img)
		I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
		I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
		I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
		I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
		I1.text((300, 450), f"{region} vaqti", font=ImageFont.truetype('mono.ttf', 18), fill=(255, 0, 0))
		img.save(f"pic/{id}.png")
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'),
		                          caption=f"<b>Ramazon oyi muborak bo'lsin</b>\n\nBugun Ramazonning {day - 1} - kuni\n\n<b>Saxarlik : {bomdod}\n\nIftorlik :       {shom}\n</b>\n\nVaqtlar {region} bo`yicha ko`rsatildi",
		                          reply_markup=ramazon_btn, parse_mode='html')


@dp.message_handler(text = '🗓 Oylik taqvim')
async def monthly(message: types.Message):
	await message.reply('https://islom.uz/vaqtlar/27/4')


@dp.message_handler(text='®️ Viloyatlar')
async def provinces_handler(msg: Message):
	await msg.answer('Viloyatingizni tanlang', reply_markup=await provinces())

@dp.callback_query_handler(text = 'Toshkent')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Toshkent')
	file.close()
	await c.answer()
	await c.message.answer("Toshkent tanlandi", reply_markup=main_btn)

@dp.callback_query_handler(text = 'Andijon')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Andijon')
	file.close()
	await c.answer()
	await c.message.answer('Andijon tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text = 'Buxoro')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Buxoro')
	file.close()
	await c.answer()
	await c.message.answer('Buxoro tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text = 'Guliston')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Guliston')
	file.close()
	await c.answer()
	await c.message.answer('Guliston tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text = 'Samardand')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Samardand')
	file.close()
	await c.answer()
	await c.message.answer('Samardand tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text = 'Namangan')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Namangan')
	file.close()
	await c.answer()
	await c.message.answer('Namangan tanlandi', reply_markup=main_btn)


@dp.callback_query_handler(text = 'Navoiy')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Navoiy')
	file.close()
	await c.answer()
	await c.message.answer('Namangan tanlandi', reply_markup=main_btn)


@dp.callback_query_handler(text='Jizzax')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Jizzax')
	file.close()
	await c.answer()
	await c.message.answer('Jizzax tanlandi', reply_markup=main_btn)


@dp.callback_query_handler(text='Nukus')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Nukus')
	file.close()
	await c.answer()
	await c.message.answer('Nukus tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text='Qarshi')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Qarshi')
	file.close()
	await c.answer()
	await c.message.answer('Qarshi tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text='Qoqon')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Qoqon')
	file.close()
	await c.answer()
	await c.message.answer('Qoqon tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text='Xiva')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Xiva')
	file.close()
	await c.answer()
	await c.message.answer('Xiva tanlandi', reply_markup=main_btn)

@dp.callback_query_handler(text='Margilon')
async def region(c: CallbackQuery):
	file = open(f"txts/{c.from_user.id}.txt", "w")
	file.write('Margilon')
	file.close()
	await c.answer()
	await c.message.answer('Margilon tanlandi', reply_markup=main_btn)


if __name__ == '__main__':
	executor.start_polling(dp)
# dict_keys(['code', 'status', 'results'])
# dict_keys(['datetime', 'location', 'settings'])
# https://api.aladhan.com/v1/timingsByCity?city=Samarkand&country=Uzbekistan&method=2
# http://api.aladhan.com/v1/calendarByCity?city=Tashkent&country=Uzbekistan&method=2&day=23&month=04&year=2022
