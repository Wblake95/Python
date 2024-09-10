#/usr/bin/env python

def take_magic_damage(health, resist, amp, spell_power):
	total_damage = spell_power * amp - resist
	health = health - total_damage
	if health >= 0: 
		return health
	else:
		health = 0
		return health
