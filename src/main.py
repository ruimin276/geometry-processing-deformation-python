import polyscope as ps

# Initialize polyscope
ps.init()

### Register a point cloud
# `my_points` is a Nx3 numpy array
ps.register_point_cloud("my points", my_points)

### Register a mesh
# `verts` is a Nx3 numpy array of vertex positions
# `faces` is a Fx3 array of indices, or a nested list
ps.register_surface_mesh("my mesh", verts, faces, smooth_shade=True)

# Add a scalar function and a vector function defined on the mesh
# vertex_scalar is a length V numpy array of values
# face_vectors is an Fx3 array of vectors per face
ps.get_surface_mesh("my mesh").add_scalar_quantity("my_scalar", 
        vertex_scalar, defined_on='vertices', cmap='blues')
ps.get_surface_mesh("my mesh").add_vector_quantity("my_vector", 
        face_vectors, defined_on='faces', color=(0.2, 0.5, 0.5))

# View the point cloud and mesh we just registered in the 3D UI
ps.show()