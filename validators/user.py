from constants import EMAIL_DOMAIN_WHITELIST, CAPITAL_CHARS, SMALL_CHARS, DIGIT_CHARS

class UserValidator:

	@staticmethod
	def validate(f):
		def wrapper(self, instance):
			validator = UserValidator()
			validator.name(instance)
			validator.email(instance)
			validator.password(instance)

			return f(self, instance)

		return wrapper

	def name(self, instance):
		name = instance.name.split(' ')

		if len(name) < 2:
			raise Exception('You should provide a full name, with first and last name, which one up to 5 characters. Ex: "Michael Douglas"')

		for name_part in name:
			if len(name_part) < 3:
				raise Exception('Name "{}" is lower than 3 characters.'.format(name_part))


	def email(self, instance):
		email = instance.email.split('@')

		if len(email) < 2:
			raise Exception('Please, provide a valid e-mail. Ex: "joesmith@gmail.com"')

		recipient = email[0]
		domain = email[1]

		if len(recipient) > 64:
			raise Exception('Your e-mail recipient cannot contain more than 64 characters.')
		
		if domain not in EMAIL_DOMAIN_WHITELIST:
			raise Exception('Your e-mail domain is not allowed in our system.')

		for user in instance.users:
			if user['email'] == instance.email:
				raise Exception('This e-mail address is already in use.')

	def password(self, instance):
		u, l, d = 0, 0, 0

		if len(instance.password) < 8:
			raise Exception('Your password must have 8 characters or more.')

		for password_char in instance.password:
			if password_char in CAPITAL_CHARS:
				u += 1
			elif password_char in SMALL_CHARS:
				l += 1
			elif password_char in DIGIT_CHARS:
				d += 1
			else:
				continue

		if u < 1 or l < 1 or d < 1:
			raise Exception('Your password must have at least 1 lower case characters, 1 upper case characters and 1 digit.')


