'''Command Handler.'''

def compile_commands(commands: list, cleanUp=True) -> str:
	'''Compiles a list of commands into a single command. (1.12+)

	commands: the list of commands to be compiled
	cleanUp: bool, whether to clean up the temporary mincarts afterwards
	'''
	template = ('summon falling_block ~ ~1 ~ {Block:glass,Time:1,Passengers:[{'
		'id:falling_block,Block:redstone_block,Time:1,Passengers:[{'
		'id:falling_block,Block:activator_rail,Time:1,Passengers:['
		'%s'
		']}]}]}'
	)

	clr = [
		('setblock ~ ~1 ~ command_block 0 0 '
		'{Command:\\"fill ~ ~-3 ~ ~ ~1 ~ air\\"}'),
		'setblock ~ ~2 ~ redstone_block',
		'kill @e[type=commandblock_minecart,r=1]',
	]

	cmds = commands + (clr if cleanUp else [])
	new_cmds = [f'{{id:commandblock_minecart,Command:\"{i}\"}}' for i in cmds]
	content = ','.join(new_cmds)

	return template%(content,)

# Test Command
print(compile_commands(['fill ~%d ~%d ~%d ~%d ~%d ~%d wool %d'%(*([20-i]*3), *([20+i]*3), i) for i in range(16, -1, -1)]))