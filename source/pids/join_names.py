import csv
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import SDO
from kurra.sparql import query
from pathlib import Path

g = Graph()

# with open("iris.csv") as f:
#     data = csv.reader(f, delimiter=",")
#     data.__next__()
#
#     for row in data:
#         g.add((
#             URIRef(row[0]),
#             SDO.distribution,
#             Literal(row[1])
#         ))
#
# with open("names-gsq.csv") as f:
#     data = csv.reader(f, delimiter=",")
#     data.__next__()
#
#     for row in data:
#         g.add((
#             URIRef(row[0]),
#             SDO.name,
#             Literal(row[1])
#         ))
#
# with open("names-gssa.csv") as f:
#     data = csv.reader(f, delimiter=",")
#     data.__next__()
#
#     for row in data:
#         g.add((
#             URIRef(row[0]),
#             SDO.name,
#             Literal(row[1])
#         ))
#
# with open("names-gswa.csv") as f:
#     data = csv.reader(f, delimiter=",")
#     data.__next__()
#
#     for row in data:
#         g.add((
#             URIRef(row[0]),
#             SDO.name,
#             Literal(row[1])
#         ))
#
# with open("names-icsm.csv") as f:
#     data = csv.reader(f, delimiter=",")
#     data.__next__()
#
#     for row in data:
#         g.add((
#             URIRef(row[0]),
#             SDO.name,
#             Literal(row[1])
#         ))

g.parse("names.ttl")

# g.serialize(destination="names.ttl", format="longturtle")

q = """
    PREFIX pid: <https://linked.data.gov.au/def/pid/>
    
    SELECT (COUNT(?c) AS ?count)
    WHERE {
        ?c a pid:PID .
    }
    """

a = int(query(g, q, return_python=True, return_bindings_only=True)[0]["count"]["value"])
print(a)

q = """
    PREFIX pid: <https://linked.data.gov.au/def/pid/>
    PREFIX schema: <https://schema.org/>

    SELECT *
    WHERE {
        ?c a pid:PID ;
            schema:name ?n ;
        .
        
        FILTER (?n = "")
    }
    """

no_name = []
for row in query(g, q, return_python=True, return_bindings_only=True):
    no_name.append(row["c"]["value"])
print(len(no_name))


