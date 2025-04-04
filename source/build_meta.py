from pathlib import Path
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import OWL, RDF, SDO, SKOS
import json

from kurra.sparql import query

DIR = Path(__file__).parent

def build_meta(f):
    f = DIR.parent / f
    new_file = DIR.resolve().parent / str(f.name).replace("-initial", "")

    g = Graph().parse(f)

    q = """
        PREFIX schema: <https://schema.org/>
    
        CONSTRUCT {
            []
                a schema:DefinedTerm ;
                schema:description ?l ;  
                schema:about ?dt ;      
            .
        }
        WHERE {
            ?dt 
                schema:location ?l ;
            .
        }
        """

    query(g, q).serialize(destination=new_file, format="longturtle")

build_meta(DIR / "dataset-initial.ttl")
build_meta(DIR / "def-initial.ttl")
build_meta(DIR / "org-initial.ttl")
build_meta(DIR / "reg-initial.ttl")