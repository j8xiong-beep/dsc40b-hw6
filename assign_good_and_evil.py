def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    # TODO: Implement the assign_good_and_evil function

    labels = {}

    for start in graph.nodes:
        if start not in labels:
            labels[start] = 'good'
            queue = [start]

            while queue:
                node = queue.pop(0)

                for neighbor in graph.neighbors(node):
                    if labels[node] == 'good':
                        other = 'evil'
                    else:
                        other = 'good'

                    if neighbor not in labels:
                        labels[neighbor] = other
                        queue.append(neighbor)
                    elif labels[neighbor] != other:
                        return None

    return labels
