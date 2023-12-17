if held_keys["w"]:
    self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt
else:
     self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt * 2
if held_keys["a"]:
    self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt
else:
     self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt * 2
if held_keys["s"]:
    self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt
else:
     self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt * 2
if held_keys["d"]:
    self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt
else:
     self.velocity_z +=10 * time.dt if y_ray.hit else 2 * time.dt * 2

