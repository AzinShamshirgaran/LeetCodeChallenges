#https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands, obstacles) -> int:

        pos=[0,0]
        attitude = "N"
        for move in commands:

            if move == -1:
                if attitude == "N":
                    attitude ="E"
                elif attitude == "E":
                        attitude = "S"
                elif attitude == "S":
                    attitude = "W"
                else:
                    attitude = "N"
            elif move == -2:
                if attitude == "N":
                    attitude ="W"
                elif attitude == "W":
                        attitude = "S"
                elif attitude == "S":
                    attitude = "E"
                else:
                    attitude = "N"
            elif move > 0 & move < 10:
                if attitude == "N":
                    lst_obs=[]
                    for obs in obstacles:
                        if obs[1] > pos [1] & pos[0]==obs[0]:
                            lst_obs.append(obs)
                    if lst_obs:
                       obs_tmp = lst_obs[0]
                       for obsl in range(1,lst_obs):
                          if obsl[1] < obs_tmp[1]:
                            obs_tmp = obsl

                       pos[1] = obs_tmp[1]-1
                    pos[1]=pos[1]+move
                elif attitude == "W":
                    lst_obs=[]
                    for obs in obstacles:
                        if obs[0] < pos [0] & pos[1]==obs[1]:
                            lst_obs.append(obs)
                    if lst_obs:
                       obs_tmp = lst_obs[0]
                       for obsl in range(1,lst_obs):
                          if obsl[0] > obs_tmp[0]:
                            obs_tmp = obsl

                       pos[0] = obs_tmp[0]+1
                    pos[0]=pos[0]-move
                elif attitude == "S":
                    lst_obs=[]
                    for obs in obstacles:
                        if obs[1] < pos [1] & pos[1]==obs[1]:
                            lst_obs.append(obs)
                    if lst_obs:
                       obs_tmp = lst_obs[0]
                       for obsl in range(1,lst_obs):
                          if obsl[1] > obs_tmp[1]:
                            obs_tmp = obsl

                       pos[1] = obs_tmp[1]+1
                    pos[1]=pos[1]-move
                else:
                    lst_obs=[]
                    for obs in obstacles:
                        if obs[0] > pos [0] & pos[1]==obs[1]:
                            lst_obs.append(obs)
                    if lst_obs:
                       obs_tmp = lst_obs[0]
                       for obsl in range(1,lst_obs):
                         if obsl[0] < obs_tmp[0]:
                            obs_tmp = obsl

                       pos[0] = obs_tmp[0]-1
                    pos[0]=pos[0]+move
        print(pos)
        return pos[0]*pos[0]+pos[1]*pos[1]






if __name__ == '__main__':
    commands = [4,-1,4,-2,4]
    obstacles=[[2,4]]
    print(Solution().robotSim(commands, obstacles))