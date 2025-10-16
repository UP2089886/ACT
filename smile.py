	import matplotlib.pyplot as plt
	
	
	face = plt.Circle((0, 0), 1, color='yellow', ec='black')
	
	
	left_eye = plt.Circle((-0.3, 0.3), 0.1, color='black')
	right_eye = plt.Circle((0.3, 0.3), 0.1, color='black')

	import numpy as np
	x = np.linspace(-0.5, 0.5, 100)
	y = 0.5 * (x ** 2) - 0.5  # Parabola shape for smile

	fig, ax = plt.subplots()
	ax.add_patch(face)
	ax.add_patch(left_eye)
	ax.add_patch(right_eye)
	ax.plot(x, y, color='black', linewidth=3)

	ax.set_aspect('equal')
	ax.axis('off')
	plt.xlim(-1.2, 1.2)
	plt.ylim(-1.2, 1.2)

	plt.show()

