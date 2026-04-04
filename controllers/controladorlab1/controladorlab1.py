"""controladorlab1 controller."""

from controller import Robot

# Crear la instancia del robot
robot = Robot()

# Obtener el "time step" de la simulación
timestep = int(robot.getBasicTimeStep())

# Identificar motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Configurar motores para control de velocidad
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Establecer velocidad inicial
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Bucle principal
while robot.step(timestep) != -1:
    left_motor.setVelocity(4.0)
    right_motor.setVelocity(4.0)