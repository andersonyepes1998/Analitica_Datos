from faker import Faker

def crearMedicos():
    medicos=[]
    
    faker = Faker()
    
    for i in range(2000):
        medico={}
        medico['nombre']=faker.name()
        medico['cargo']=faker.job()
        medicos.append(medico)
        
    return medicos
        
    