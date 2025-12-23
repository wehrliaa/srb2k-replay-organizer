#!/usr/bin/python3
#
# simple script that neatly organizes your srb2k replays

import glob # match a list of files with glob matching
import os   # file manipulation (moving, renaming...) shenanigans
import sys  # only for sys.stderr
import time # time format conversion stuff

def main():
	try:
		os.chdir("./online")
	except FileNotFoundError:
		print("ERROR: You don't have a folder for replays of online races. Go play the damn game!", file=sys.stderr)
		exit(1)
	
	replays = glob.glob("*.lmp")

	if len(replays) == 0:
		print("ERROR: No replay files were found in your \"online\" folder. Go play the damn game!", file=sys.stderr)
		exit(1)

	movecount = 0
	
	for replay in replays:
		s = replay.split("-")

		# there's probably a more efficient way to do this but i dont car
		day = time.strftime("%d", time.localtime(int(s[0])))
		month = time.strftime("%m %B", time.localtime(int(s[0])))
		year = time.strftime("%Y", time.localtime(int(s[0])))

		os.makedirs(f"aaa-organized/{year}/{month}/{day}", exist_ok=True)
		os.rename(f"{replay}", f"aaa-organized/{year}/{month}/{day}/{replay}")

		movecount += 1
	
	print(f"Done! {movecount} replays(s) moved.")

if __name__ == "__main__":
    main()
