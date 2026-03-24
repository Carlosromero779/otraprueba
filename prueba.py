from abc import ABC, abstractmethod

# 1. El Producto Abstracto: Define la interfaz común para todos los documentos.
class DocumentoMedico(ABC):
    @abstractmethod
    def generar_contenido(self) -> str:
        pass

# 2. Los Productos Concretos: Las implementaciones específicas de cada documento.
class Receta(DocumentoMedico):
    def generar_contenido(self) -> str:
        return "{ Datos: [Ibuprofeno 400mg, Reposo por 3 días] }"

class ResultadoLaboratorio(DocumentoMedico):
    def generar_contenido(self) -> str:
        return "{ Datos: [Hemoglobina: 14.5 g/dL, Leucocitos: 7.2 x10^3/uL] }"

# 3. El Creador (La Fábrica Abstracta): Declara el factory method.
class CreadorDocumento(ABC):
    
    # Este es el Factory Method que las subclases implementarán
    @abstractmethod
    def crear_documento(self) -> DocumentoMedico:
        pass

    # El creador tiene lógica central que usa el producto, sin saber qué producto es
    def procesar_y_guardar(self) -> str:
        # 1. Llama al factory method para obtener un objeto DocumentoMedico
        documento = self.crear_documento()
        
        # 2. Usa el objeto (el código no sabe si es Receta o ResultadoLaboratorio)
        contenido = documento.generar_contenido()
        
        return f"Guardando en el historial del paciente el siguiente registro: {contenido}"

# 4. Los Creadores Concretos: Sobrescriben el factory method para devolver un producto específico.
class CreadorReceta(CreadorDocumento):
    def crear_documento(self) -> DocumentoMedico:
        return Receta()

class CreadorLaboratorio(CreadorDocumento):
    def crear_documento(self) -> DocumentoMedico:
        return ResultadoLaboratorio()

# --- Uso del código (El Cliente) ---

def logica_de_la_aplicacion(creador: CreadorDocumento):
    # El cliente solo interactúa con el creador a través de su interfaz base.
    print(creador.procesar_y_guardar())

if __name__ == "__main__":
    print("Médico solicitando una receta:")
    logica_de_la_aplicacion(CreadorReceta())
    
    print("\nLaboratorista subiendo resultados:")
    logica_de_la_aplicacion(CreadorLaboratorio())