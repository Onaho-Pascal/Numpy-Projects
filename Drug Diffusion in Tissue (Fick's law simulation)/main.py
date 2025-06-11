import numpy as np
import matplotlib.pyplot as plt
# concentration = np. linspace(0, 1, 5)
# print("Drug concentration levels:", concentration)

#simulation parameters
length = 100 # number of cells
timesteps = 100 #how many time steps to simulate
diffusion_rate = 0.1 # how quickly the drug spreads

#initialize concentration array
concentration = np.zeros(length)
concentration[length // 2] = 1.0 #how quickly the drug spreads

#store concentration history for plotting
history = [concentration.copy()]

#Diffusion simulation loop

for t in range(timesteps):
    new_concentration = concentration.copy()
    for i in range(1, length - 1):
        new_concentration[i] += diffusion_rate * (
            concentration[i - 1] + concentration[i + 1] - 2 * concentration[i]
        )
    concentration = new_concentration
    history.append(concentration.copy())

    #convert history to a Numpy array for Visualization

    #Plot the diffusion over time

    plt.imshow(history, aspect='auto', cmap='hot', interpolation='nearest')
    plt.colorbar(label="Drug Concentration")
    plt.xlabel("Position along tissue")
    plt.ylabel("Time Step")
    plt.title("1D Drug Diffusion Over Time")
    plt.show()
    plt.close()

#plot concentration profiles at different time steps
# plt.figure(figsize=(10, 6))
# for t in [0, 10, 30, 60, 99]:
#     plt.plt(history[t], label=f'Time {t}')
# plt.xlabel("Position")
# plt.ylabel("Concentration")
# plt.title("Drug Diffusion over time")
# plt.legend()
# plt.grid(True)
# plt.show()
#plt.close()