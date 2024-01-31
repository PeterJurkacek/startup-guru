import graphviz
from pathlib import Path

def render_dot_to_png(dot_file_path, output_png_path):
    # Read the .dot file
    with open(dot_file_path, 'r') as dot_file:
        dot_data = dot_file.read()

    # Create a Graph object from the DOT data
    graph = graphviz.Source(dot_data, dot_file_path)

    # Render the graph to a PNG file
    graph.render(filename=output_png_path, format='png', cleanup=True)

if __name__ == "__main__":
    dot_file_path = 'slides/img/image_retrieval.dot'
    output_png_path = Path(dot_file_path).with_suffix(".png")

    render_dot_to_png(dot_file_path, output_png_path)
