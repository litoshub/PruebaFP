'''
Created on 19 dic 2024

@author: carlo
'''
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional, Set, List
from entrega3.E_grafo import E_Grafo
from entrega3.Recorrido import bfs

# Ejercicio 1: Implementación del tipo Gen
@dataclass(frozen=True)
class Gen:
    """
    Representa un gen en el sistema.
    """
    _id: int
    _nombre: str
    _tipo: str
    _num_mutaciones: int
    _loc_cromosoma: str
    
    _xx_num: int = 0
    
    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def num_mutaciones(self) -> int:
        return self._num_mutaciones

    @property
    def loc_cromosoma(self) -> str:
        return self._loc_cromosoma

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> Gen:
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser positivo")
        if not all([nombre, tipo, loc_cromosoma]):
            raise ValueError("Ningún campo puede estar vacío")

        Gen._xx_num += 1
        return Gen(Gen._xx_num, nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(linea: str) -> Gen:
        try:
            nombre, tipo, num_mutaciones_str, loc_cromosoma = linea.strip().split(',')
            num_mutaciones = int(num_mutaciones_str)
            return Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)
        except Exception as e:
            raise ValueError(f"Error al parsear la línea: {str(e)}")

    def __str__(self) -> str:
        return f"({self._id} - {self._nombre} - tipo: {self._tipo} - mutaciones: {self._num_mutaciones} - loc: {self._loc_cromosoma})"

# Ejercicio 2: Implementación del tipo RelacionGenAGen
@dataclass(frozen=True)
class RelacionGenAGen:
    """
    Representa una relación entre dos genes en el sistema.
    """
    _id: int
    _score: float
    _tipo_relacion: str
    _publicacion: Optional[str]
    
    _xx_num: int = 0

    @property
    def id(self) -> int:
        return self._id

    @property
    def score(self) -> float:
        return self._score

    @property
    def tipo_relacion(self) -> str:
        return self._tipo_relacion

    @property
    def publicacion(self) -> Optional[str]:
        return self._publicacion

    @staticmethod
    def of(score: float, tipo_relacion: str, publicacion: Optional[str] = None) -> RelacionGenAGen:
        if not 0 <= score <= 1:
            raise ValueError("El score debe estar entre 0 y 1")
        if not tipo_relacion:
            raise ValueError("El tipo de relación no puede estar vacío")

        RelacionGenAGen._xx_num += 1
        return RelacionGenAGen(RelacionGenAGen._xx_num, score, tipo_relacion, publicacion)

    @staticmethod
    def parse(linea: str) -> RelacionGenAGen:
        try:
            score = float(linea.strip())
            # Por defecto, si el score es positivo es "activacion", si es negativo es "inhibicion"
            tipo_relacion = "activacion" if score >= 0 else "inhibicion"
            # Usamos el valor absoluto del score para mantenerlo entre 0 y 1
            score = abs(score)
            
            return RelacionGenAGen.of(score, tipo_relacion)
        except Exception as e:
            raise ValueError(f"Error al parsear la línea: {str(e)}")

    def __str__(self) -> str:
        publicacion_str = f" - pub: {self._publicacion}" if self._publicacion else ""
        return f"({self._id} - score: {self._score} - tipo: {self._tipo_relacion}{publicacion_str})"

# Ejercicio 3: Implementación del tipo RedGenica
class RedGenica(E_Grafo[Gen, RelacionGenAGen]):
    """
    Representa una red génica como un grafo donde los nodos son genes
    y las aristas son relaciones entre ellos.
    """
    def __init__(self, es_dirigido: bool = True):
        super().__init__(es_dirigido)
        self._genes_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = True) -> RedGenica:
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(archivo_genes: str, archivo_relaciones: str) -> RedGenica:
        red = RedGenica()

        # Cargar genes
        with open(archivo_genes, 'r', encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    gen = Gen.parse(linea.strip())
                    red.add_vertex(gen)
                    red._genes_nombre[gen.nombre] = gen

        # Cargar relaciones
        with open(archivo_relaciones, 'r', encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    gen1_nombre, gen2_nombre, score = linea.strip().split(',')
                    gen1 = red._genes_nombre.get(gen1_nombre)
                    gen2 = red._genes_nombre.get(gen2_nombre)
                    
                    if gen1 and gen2:
                        relacion = RelacionGenAGen.parse(score)
                        red.add_edge(gen1, gen2, relacion)

        return red

    def genes_relacionados_directamente(self, gen: Gen) -> Set[Gen]:
        return self.successors(gen)

    def genes_relacionados_indirectamente(self, gen: Gen, max_saltos: int) -> Set[Gen]:
        if max_saltos < 1:
            return set()

        genes_relacionados = set()
        visitados = {gen}
        nivel_actual = {gen}
        
        for _ in range(max_saltos):
            siguiente_nivel = set()
            for gen_actual in nivel_actual:
                for gen_relacionado in self.successors(gen_actual):
                    if gen_relacionado not in visitados:
                        siguiente_nivel.add(gen_relacionado)
                        genes_relacionados.add(gen_relacionado)
                        visitados.add(gen_relacionado)
            
            if not siguiente_nivel:
                break
                
            nivel_actual = siguiente_nivel

        return genes_relacionados

    def camino_relacion(self, gen1: Gen, gen2: Gen) -> Optional[List[Gen]]:
        """
        Encuentra el camino más corto entre dos genes usando BFS.
        """
        if gen1 not in self.vertex_set() or gen2 not in self.vertex_set():
            return None
        camino = bfs(self, gen1, gen2)
        return camino if camino else None

    def __str__(self) -> str:
        resultado = []
        for gen in self.vertex_set():
            relaciones = []
            for gen_relacionado in self.successors(gen):
                relacion = self.edge_weight(gen, gen_relacionado)
                if relacion:
                    relaciones.append(f"{gen_relacionado.nombre}: {relacion}")
            resultado.append(f"{gen.nombre} -> {', '.join(relaciones)}")
        return "\n".join(resultado)

def test_red_genica():
    """
    Test para verificar la funcionalidad de la red génica.
    """
    print("Test Red Génica")
    print("-" * 50)

    try:
        # Crear la red génica usando los archivos
        red = RedGenica.parse("genes.txt", "red_genes.txt")

        # Test 1: Verificar la creación de genes
        print("\nGenes en la red:")
        for gen in sorted(red.vertex_set(), key=lambda g: g.nombre):
            print(f"- {gen}")

        # Test 2: Verificar las relaciones de TP53
        gen_tp53 = red._genes_nombre["TP53"]
        print("\nGenes relacionados directamente con TP53:")
        directos = red.genes_relacionados_directamente(gen_tp53)
        for gen in sorted(directos, key=lambda g: g.nombre):
            print(f"- {gen.nombre}")

        # Test 3: Verificar relaciones indirectas de TP53
        print("\nGenes relacionados indirectamente con TP53 (max 2 saltos):")
        indirectos = red.genes_relacionados_indirectamente(gen_tp53, 2)
        for gen in sorted(indirectos, key=lambda g: g.nombre):
            print(f"- {gen.nombre}")

        # Test 4: Encontrar camino entre TP53 y PTEN
        gen_pten = red._genes_nombre["PTEN"]
        print("\nCamino desde TP53 hasta PTEN:")
        camino = red.camino_relacion(gen_tp53, gen_pten)
        if camino:
            print(" -> ".join(gen.nombre for gen in camino))
        else:
            print("No existe camino")

    except FileNotFoundError as e:
        print(f"Error: No se encontró alguno de los archivos necesarios: {e}")
    except Exception as e:
        print(f"Error durante la ejecución del test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_red_genica()