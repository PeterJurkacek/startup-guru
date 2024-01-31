import yaml
from graphviz import Graph
import itertools

# MIND = 'More than 200 readings to explain'
MIND = ''
NODE_COLOR = "#A478FF"
EDGE_COLOR = "#C7A6F3"
NODE_TXT_COLOR = "#FFFFFF"
HIGHLIGHT_COLOR = "#335C55"

idc = itertools.count()

# Load YAML data from file
# # Replace 'your_file.yaml' with the path to your YAML file
yaml_file_path = '/Users/pj/aston/projects/confs/confs/tags_0.2.1.yaml'
with open(yaml_file_path, 'r') as file:
    data = yaml.safe_load(file)
    
def parse_yaml_to_dot(tags):
    # Add nodes and edges from the YAML data
    types = []
    dentalSpecialities = []
    tnodes, anodes, cnodes = [], [], []
    tedges, aedges, cedges = [], [], []
    for t in tags:
        assert 'type' in t, f"E06:Missing type, {t['code']}"
        assert len(t['dentalSpecialities']) > 0, f"E07:Missing dentalSpecialities, {t['code']}"
        if t['name'] in ['Other']:
            continue
        # for typ in t['dentalSpecialities']:
        typ = t['type']
        tname = f"{next(idc)}_{t['code']}"
        tedges.append((typ, tname))
        tlabel = t['name']
        tnodes.append((tname, tlabel))
        types.append(typ)
        for a in t['attributes']:
            aname = f"{next(idc)}_{a['code']}"
            alabel = a['name']
            
            if alabel in ['Notes']:
                continue
            anodes.append((aname, alabel))
            aedges.append((tname, aname))
            
            if 'choices' in a:
                for c in a['choices']:
                    cname = f"{next(idc)}_{c['code']}"
                    clabel = str(c['name'])
                    cnodes.append((cname, clabel))
                    cedges.append((aname, cname))
    
    print(set(types))
    types = [(i, i) for i in (set(types))]

    # Create a directed graph using Graphviz
    # MIND = 'Readings?
    
    graph1 = create_graph(types, tnodes, anodes, cnodes, tedges, aedges, cedges, MIND, highlights=[])
    graph2 = create_graph(types, tnodes, anodes, cnodes, tedges, aedges, cedges, MIND, highlights='Decay')
        
    return graph1, graph2

def create_graph(types, tnodes, anodes, cnodes, tedges, aedges, cedges, MIND, highlights=[]):
    graph = Graph(engine='twopi')
    # Set graph attributes
    graph.attr(bgcolor='transparent')
    graph.attr(labelloc="t")
    # graph.attr(label="Mind map of Experts decisions")
    graph.attr(layout="twopi")
    graph.attr(fontname="DMSans-AID-Headline")
    graph.attr(ranksep="4.5")
    graph.attr(ratio="auto")

    # Set default edge attributes
    graph.attr('edge', penwidth='1', color=EDGE_COLOR)
    # Set default node attributes
    graph.node(MIND, fontname="DMSans-AID-Headline", fontsize='65', penwidth='0')
    graph.attr('node', style='filled', penwidth='0', fillcolor=NODE_COLOR, fontcolor=NODE_TXT_COLOR, fontname="DMSans-AID-Text")

    
    for (i, i) in types:
      graph.node(i, i, fontname="DMSans-AID-Headline", fontsize='30')
    for (i, i) in types:
        graph.edge(MIND, i)
        
    for (name, label) in tnodes:
        if label in highlights:
            graph.node(name, label, fontsize='40', shape="", fillcolor=HIGHLIGHT_COLOR, fontcolor=NODE_TXT_COLOR)
        else:
            graph.node(name, label)
        
    for (name1, name2) in tedges:
        graph.edge(name1, name2)
    
    for (name, label) in anodes:
        graph.node(name, label, fontsize='15')
    for (name1, name2) in aedges:
        graph.edge(name1, name2)
    
    for (name, label) in cnodes:
        graph.node(name, label, fontsize='10')
    for (name1, name2) in cedges:
        graph.edge(name1, name2)
    return graph

# Create DOT graph from YAML data
dot_graph1, dot_graph2  = parse_yaml_to_dot(data['tags'])

# dot_graph.view()
dot_graph1.render('expert_mind', format='png', cleanup=True)
dot_graph1.save('expert_mind.dot')

dot_graph2.render('expert_mind_2', format='png', cleanup=True)
dot_graph2.save('expert_mind_2.dot')

# Save the graph as a DOT file

# Alternatively, you can render the graph directly in Jupyter Notebook
# dot_graph.render('graph', format='png', cleanup=True)

# View the DOT file content
with open('expert_mind.dot', 'r') as file:
    dot_content = file.read()

# print(dot_content)
