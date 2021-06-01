from selenium import webdriver
import time
# A program to purchase a PS5 in the range of $800-$900 on Ebay. Fill your info here and you just have to click once(Confirm and Pay) to buy a PS5 on Ebay.
#success!
#Ebay might prompt you to verify you're not a bot. If you fill it out once it shouldn't pop up again when you run the program.
 class PS5bot:

	def __init__(self, fn, ln, add, add2, e_mail, phone, credit_number, credit_exp, ccv,
		range_to, range_from):
		self.fn = fn
		self.ln = ln
		self.e_mail = e_mail
		self.add = add
		self.add2 = add2
		self.phone = phone
		self.credit_number = credit_number
		self.credit_exp = credit_exp
		self.ccv = ccv
		self.range_to = range_to
		self.range_from = range_from
		self.driver = webdriver.Chrome()
		self.driver.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=ps5&_sacat=0')

	def find_item(self):
		price_range_to = ('#s0-14-11-0-1-2-6-0-6\[3\]-0-textrange-5-textbox')
		price_range_from = ('#s0-14-11-0-1-2-6-0-6\[3\]-0-textrange-9-textbox')
		price_range_arrow = ('#s0-14-11-0-1-2-6-0-6\[3\]-0-textrange > div > button > span')
		buy_it_now_bubble = ('#x-refine__group__4 > ul > li:nth-child(4) > div > a > div > span > input')
		select_item = ('#srp-river-results > ul > li:nth-child(2) > div > div.s-item__image-section > div > a > div > img')
		self.filldata(price_range_to, self.range_to)
		self.filldata(price_range_from, self.range_from)
		self.select_button(price_range_arrow)
		self.select_button(buy_it_now_bubble)
		self.select_button(select_item)

	def fill_shipping(self):
		buy_it_now = ('#binBtn_btn')
		no_thanks = ('#ADDON_0 > div > div.adndesc.addon-overlay-body > div > div.adnactions > div > button.addonbtn.addonnothx.addon-overlay-close-button') # deny protection
		check_out_as_guest = ('#sbin-gxo-btn')
		first_name = ('#firstName')
		last_name = ('#lastName')
		address = ('#addressLine1')
		address2 = ('#addressLine2')
		city = ('#city') # autofill
		state = ('#stateOrProvince') # autofill
		zip_code = ('#postalCode') # autofill
		email = ('#email')
		conf_email = ('#emailConfirm')
		phone_num = ('#phoneNumber')
		done_button = ('#mainContent > div.two-column.container.no-gutters > div > div.left-column.col-7.col-lg-8 > section.module.shipping-address.auto-address-container > div:nth-child(3) > div > div > div > div.address-form > div.view-visible > form > div > div > div > button')
		use_this_address = ('#mainContent > div.two-column.container.no-gutters > div > div.left-column.col-7.col-lg-8 > section.module.shipping-address.auto-address-container > div:nth-child(3) > div > div > div > div.address-form > div.view-visible > div > div > div.addresses > div.provided-address > div.address-action > button')
		self.select_button(buy_it_now)
		self.select_button(no_thanks)
		self.select_button(check_out_as_guest)
		self.filldata(first_name, self.fn)
		self.filldata(last_name, self.ln)
		self.filldata(address, self.add)
		self.filldata(address2, self.add2)
		self.filldata(email, self.e_mail)
		self.filldata(conf_email, self.e_mail)
		self.filldata(phone_num, self.phone)
		self.select_button(done_button)
		self.select_button(use_this_address)

	def fill_credit(self): 
		credit_button = ('#srs1')
		card_num = ('#cardNumber')
		cc_exp_date = ('#cardExpiryDate')
		sec_code = ('#securityCode')
		cc_first_name = ('#cardHolderFirstName')
		cc_last_name = ('#cardHolderLastName')
		cc_done_button = ('#credit-card-details > div.form-actions > div > div.form-action.ADD_CARD > button')
		self.select_button(credit_button)
		self.filldata(card_num, self.credit_number)
		self.filldata(cc_exp_date, self.credit_exp)
		self.filldata(sec_code, self.ccv)
		self.filldata(cc_first_name, self.fn)
		self.filldata(cc_last_name, self.ln)
		self.select_button(cc_done_button)

	def filldata(self, field, data):
		try:
			self.driver.find_element_by_css_selector(field).send_keys(data)
			pass
		except Exception:
			time.sleep(1)
			self.filldata(field, data)

	def select_button(self, css):
		try:
			self.driver.find_element_by_css_selector(css).click()
		except Exception:
			time.sleep(1)
			self.select_button(css)

if __name__ == "__main__":
	personal_info = dict(
		fn = "Jared",
		ln = "Smith",
		e_mail = "youreemail@gmail.com",
		add = "Your address.",
		add2 = "4",
		phone = "5555555555",
		credit_number = "4444444444444444",
		credit_exp = "0321",
		ccv = "800",
		range_to = "800",
		range_from = "900",
		)

bot = PS5bot(**personal_info)
bot.find_item()
bot.fill_shipping()
bot.fill_credit()

