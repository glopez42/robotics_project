
from coppelia import Coppelia
from robot import ACMR
import math

# euclidean distance between individual and goal
def get_euclidean_distance(pos1, pos2):
    return math.sqrt((pos2[0]-pos1[0])**2 + (pos2[1]-pos1[1])**2)

def main(args=None):
    coppelia = Coppelia()
    robot = ACMR(coppelia.sim, 'ACMR')
    coppelia.start_simulation()
    goalPosition = coppelia.sim.getObjectPosition(coppelia.sim.getObject(f'/goal'))
    distance = get_euclidean_distance(goalPosition, robot.get_actual_position())
    print(f"Initial distance to goal: {distance}")

    params = [
            0.343038846947356,
            7.59395293302817,
            -0.017140772827689475,
            5.928119785928505
    ]

    for _ in range(1):
        robot.set_movement_params(params)
        start = coppelia.sim.getSimulationTime()
        t = 0
        while (t) < 20:
            angles = robot.calculate_angles(t)
            for n in range(robot.N_parts-1):
                robot.set_joint(n,angles[n])

            t = coppelia.sim.getSimulationTime() - start

        distance = get_euclidean_distance(goalPosition, robot.get_actual_position())
        print(f"Final distance to goal: {distance}")
        robot.reset_position()

    coppelia.stop_simulation()

if __name__ == '__main__':
    main()
