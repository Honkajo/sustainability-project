import networkx as nx
import multiprocessing

def calculate_shortest_paths(G):
    """
    Calculate all-pairs shortest paths in a graph efficiently.
    """
    # Use NetworkX's built-in all-pairs shortest path function
    all_pairs = nx.all_pairs_shortest_path(G)
    
    # Convert the result into a dictionary of dictionaries
    all_paths = {}
    for source, destinations in all_pairs:
        all_paths[source] = {dest: path for dest, path in destinations.items()}
    
    return all_paths

def parallelize_shortest_paths(G, num_processes=None):
    """
    Parallelize the calculation of shortest paths using multiple processes.
    """
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    # Split the nodes into chunks for parallel processing
    nodes = list(G.nodes())
    chunk_size = len(nodes) // num_processes
    chunks = [nodes[i*chunk_size:(i+1)*chunk_size] for i in range(num_processes)]
    
    # Define a helper function for each process
    def process_chunk(chunk):
        sub_paths = {}
        for source in chunk:
            destinations = nx.single_source_shortest_path(G, source)
            sub_paths[source] = destinations
        return sub_paths
    
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(process_chunk, chunks)
    
    # Combine the results into a single dictionary
    all_paths = {}
    for result in results:
        all_paths.update(result)
    
    return all_paths

# Example usage with a sample graph
if __name__ == "__main__":
    # Create a sample graph (e.g., Erdős-Rényi model)
    n_nodes = 10
    p_edge = 0.5
    G = nx.erdos_renyi_graph(n_nodes, p_edge)
    
    # Calculate all-pairs shortest paths
    all_paths = calculate_shortest_paths(G)

    
    # Alternatively, use parallel processing
    all_paths_parallel = parallelize_shortest_paths(G)


