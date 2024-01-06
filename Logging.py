import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
def add(x,y):
 return x+y
	
def sub (x,y):
 return x-y
	
def mul (x,y):
	return x*y
	
def div (x,y):
	return x / y
	
	
num_1 = 103
num_2 = 19
	
add_result = add(num_1, num_2)
logging.debug('Add: {} +{} = {}'.format(num_1, num_2, add_result) )
sub_result = sub(num_1, num_2)
logging.debug('Sub: {} -{} = {}'.format(num_1, num_2, sub_result) )
div_result = div(num_1, num_2)
logging.debug('Div: {} /{} = {}'.format(num_1, num_2, div_result) )

mul_result = mul(num_1, num_2)
logging.debug('Add: {} * {} = {}'.format(num_1, num_2, mul_result) )

	
	
