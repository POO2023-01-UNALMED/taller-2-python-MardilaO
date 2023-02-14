from main import Asiento, Motor, Auto

def testMetodoCambiarColor():
    a1 = Asiento("blanco", 5000, 435)
    a2 = Asiento("blanco", 5000, 435)
    
    a1.cambiarColor("naranja")
    a2.cambiarColor("verde")
    
    ok = False
    
    if(a1.color == "blanco" and a2.color == "verde"):
        ok = True
    assert(ok)
    
	
def testMetodoCambiarRegistro():
    m = Motor(4, "electrico", 123)
    
    m.cambiarRegistro(423)
    
    ok = False
    
    if(m.registro == 423):
        ok = True

    assert(ok)
	
def testMetodoAsignarTipo():
    m1 = Motor(4, "normal", 142)
    m2 = Motor(4, "normal", 142)
    
    m1.asignarTipo("hibrido")
    m2.asignarTipo("electrico")
    ok = False
    
    if(m1.tipo == "normal" and m2.tipo == "electrico"):
        ok = True
    assert(ok)
	
def testMetodoCantidadAsientos():
    a = Auto("model 3", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)
    
    a.asientos = [Asiento("blanco", 5000, 435),None, None, Asiento("blanco", 5000, 435), None]
    
    ok = False
    
    if(a.cantidadAsientos() == 2):
        ok = True

    assert(ok)
	
def testMetodoVerificarIntegridad():
		
    a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 32),None, None, Asiento("blanco", 5000, 32), None],
    "tesla", Motor(4, "electrico", 32), 32)
    a2 = Auto("model 3", 33000, [Asiento("blanco", 5000, 40),None, None, Asiento("blanco", 5000, 32), None],
    "tesla", Motor(4, "electrico", 32), 32)

    ok = False
		
    if(a1.verificarIntegridad() == "Auto original" and 
            a2.verificarIntegridad() == "Las piezas no son originales"):
        ok = True

    assert(ok)
