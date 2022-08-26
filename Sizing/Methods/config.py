

class conditions():
    def __init__(self,air_density,velocities,takeoff_d,CDmin,AR,n_z,oswald_factor,CLmax,CL_TO,prop_eff):
        self.air_density = air_density
        self.vc = velocities[0]
        self.vv = velocities[1]
        self.to_d = takeoff_d
        

class aircraft():
    def __init__(self,CDmin,AR,n_z,oswald_factor,CLmax,CL_TO,prop_eff):
        self.cdmin = CDmin
        self.AR = AR
        self.n_z = n_z
        self.e = oswald_factor
        self.clmax = CLmax
        self.cl_to = CL_TO
        self.eta_p = prop_eff