density = 9.80665
pressure = 998.2

def main():
    return
def water_column_height(tower_height, tank_height):

    height = tower_height + (3*tank_height/4)
    return height

def pressure_gain_from_water_height(height, density, pressure):
    pressure = (density*density*height)/1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    pressure_loss = ((-1*friction_factor)*pipe_length*density*fluid_velocity)/2000*pipe_diameter

    return pressure_loss

main()