from main import Asiento, Motor, Auto


def testAtributosMotor():
	Motor(4, "electrico", 142)
	assert(True)
	
def testAtributosAsiento():
	Asiento("blanco", 5000, 435)
	assert(True)
	
def testAtributosAuto():
	Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)
	assert(True)
