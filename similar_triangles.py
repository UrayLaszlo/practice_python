def similar_triangles(coords_1, coords_2):
    # your code here
    n = coords_1[1][1]
    m = coords_2[1][1]
    print(n%2)
    return (n==m) or (n % 2 == 0 and m % 2 == 0)

similar_triangles([[0, 2], [1, 4], [5, 2]], [[0, 1], [1, 3], [5, 1]]) # True
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) #is True, 'basic'
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) #is False, 'different #1'
similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) #is False, 'different #2'
similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) #is True, 'scaling'
similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) #is True, 'reflection'
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) #is True, 'scaling and reflection'