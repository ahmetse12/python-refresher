#problem 1 
def calculate_buoyancy(V: int, density_fluid):
    """this calculates bu...
    takes v as volume, and density_fluid as density
    """
    g = 9.81
    B = V * density_fluid * g
    return B 

calculate_buoyancy(V = 10, density_fluid = 5)

#problem 2 
def will_it_float(v, mass):
    if v == 0: 
        return "volume can't be zero"
    elif mass / v < 1000:
        return True
    else: 
        return False

#problem 3 
def calculate_pressure(depth):
    g = 9.81
    density_water = 1000
    pressure = density_water * g * depth 
    return pressure 

#problem 4 
def calculate_acceleration(F, m):
    acceleration = F / m
    return acceleration

#problem 5
def calculate_angular_acceleration(tau, I):
    acceleration = 

#problem 6
    def calc_torque(Fmag, Fdir, r):
        """calculates a torque given its magnitude, direction, and distance from axis of rotation."""
        if r <= 0:
            raise ValueError("can't have 0 or negative radius")
        
        return r * Fmag * math.sin(Fdir)

#problem 7
    def calculate_mom_inertia(m, r):
        """calculates moment of inertia given the mass of an object and the distance from axis of rotation."""    
        return m * r * r

#problem 8
    def calculate_auv_accel(Fmag, Fdir, mass=100, volume=0.1, thruster_dist=0.5):
        """given a force and its angle, with option to change mass, volume, and thruster distance, returns the translation acceleration of the ."""    
        if mass <= 0 or volume <= 0:
            raise ValueError("can't have 0/negative mass/volume")
        #F_vertical = Fmag * math.sin(Fdir)
        #F_horizontal = Fmag * math.cos(Fdir)
        #return np.array([F_horizontal, F_vertical]) / mass
        F = Fmah*np.array([np.cos(Fdir), np.sin(Fdir)])
        return F/mass

#problem 9
    def calculate_auv_ang_accel(Fmag, Fdir, inertia=1, thruster_dist=0.5):
        """"given a force and its angle, with option to change mass, volume, and thruster distance, returns the translation acceleration of the .  """
        if inertia <= 0:
            raise ZeroDivisionError("can't divide by 0/ negative inertia")
        return Fmag * math.sin(Fdir) * thruster_dist / inertia
     

#problem 10
    def calc_auv2_accel(T, alpha, theta, mass=100):
        """given up """
        if mass <= 0: 
            raise ZeroDivisionError("can't divide by 0/negative mass")
        Thorz = T * math.sin(alpha)
        Tvert = T * math.cos(alpha)
        tothorizontal = Thorz[0] - Thorz[1] + Thorz[2] - Thorz[3]
        totvertical = Tvert[0] + Tvert[1] - Tvert[2] - Tvert[3]