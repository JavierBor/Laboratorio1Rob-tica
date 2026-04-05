from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

#Seleccionamos las ruedas del robot
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

#Evitar la detención del robot
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

#Ponemos una velocidad inicial
left_motor.setVelocity(2.0)
right_motor.setVelocity(2.0)

#Ajustamos velocidades mientras el robot corre
while robot.step(timestep) != -1:

    #Alterar estos valores (ahora mismo va recto)
    left_motor.setVelocity(2.0)
    right_motor.setVelocity(2.0)