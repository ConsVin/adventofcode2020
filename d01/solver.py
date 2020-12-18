import numpy as np
nums=np.loadtxt('data.txt').astype(int)
score=2020;
for x in nums:
	for y in nums:
		for z in nums:
			if (x+y+z)==score:
				prod=x*y*z;
				print(f"{x}+{y}+{z}={score}, prod=\n{prod}")
				exit(0)